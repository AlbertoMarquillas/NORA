"""
fsm_controller.py

Controlador principal de la máquina de estados finita (FSM) del sistema NORA.
Gestiona el estado actual, el contexto, el estado emocional, la cola priorizada
de eventos y el historial de transiciones del runtime actual.
"""

from __future__ import annotations

import heapq
import itertools
import logging
import time
from collections import deque
from pathlib import Path
from threading import RLock
from typing import Any

from ..definitions.fsm_conditions import FSMContext
from ..definitions.fsm_definitions import (
    FSMEvent,
    FSMProcessResult,
    FSMQueuedEvent,
    FSMRejectionReason,
    FSMState,
)
from ..definitions.fsm_emotional_states import EmotionalState, EmotionalStatus
from ..definitions.fsm_priority import DEFAULT_EVENT_PRIORITY, FSM_EVENT_PRIORITY
from ..definitions.fsm_transitions import FSM_TRANSITIONS, FSMTransitionRule


LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_PATH = LOG_DIR / "fsm.log"

logger = logging.getLogger("fsm")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


class FSMController:
    """
    Controlador principal de la FSM de NORA.

    El controlador mantiene el estado actual, el contexto operativo, el
    estado emocional, la cola de eventos priorizados y el historial reciente
    de transiciones. El core no depende de ORM, WebSocket ni framework web.

    Parameters
    ----------
    initial_state : FSMState
        Estado inicial de la FSM.
    history_limit : int
        Número máximo de transiciones conservadas en memoria.
    """

    def __init__(
        self,
        initial_state: FSMState = FSMState.INACTIVO,
        history_limit: int = 500,
    ) -> None:
        """
        Inicializa el controlador principal de la FSM.

        Parameters
        ----------
        initial_state : FSMState
            Estado inicial de la FSM.
        history_limit : int
            Límite máximo del historial en memoria.
        """
        self.estado_actual: FSMState = initial_state
        self.contexto: FSMContext = FSMContext()
        self.estado_emocional: EmotionalStatus = EmotionalStatus()
        self.event_queue: list[FSMQueuedEvent] = []
        self.historial_transiciones: deque[dict[str, Any]] = deque(maxlen=history_limit)
        self._sequence = itertools.count()
        self._lock = RLock()

    def recibir_evento(
        self,
        evento: FSMEvent,
        timestamp: float | None = None,
        source: str = "unknown",
        description: str = "",
        payload: dict[str, Any] | None = None,
    ) -> FSMQueuedEvent:
        """
        Inserta un evento en la cola de prioridad.

        Parameters
        ----------
        evento : FSMEvent
            Evento lógico a encolar.
        timestamp : float | None
            Marca temporal opcional.
        source : str
            Fuente del evento.
        description : str
            Descripción legible del evento.
        payload : dict[str, Any] | None
            Metadatos asociados.

        Returns
        -------
        FSMQueuedEvent
            Evento efectivamente encolado.
        """
        with self._lock:
            event_timestamp = time.time() if timestamp is None else timestamp
            queued_event = FSMQueuedEvent(
                event=evento,
                timestamp=event_timestamp,
                priority=FSM_EVENT_PRIORITY.get(evento, DEFAULT_EVENT_PRIORITY),
                sequence=next(self._sequence),
                source=source,
                description=description,
                payload=payload or {},
            )
            heapq.heappush(self.event_queue, queued_event)

            logger.info(
                "Evento encolado | event=%s source=%s priority=%s sequence=%s description=%s",
                evento.name,
                source,
                queued_event.priority,
                queued_event.sequence,
                description,
            )
            return queued_event

    def procesar_siguiente_evento(self) -> FSMProcessResult:
        """
        Procesa el siguiente evento disponible en la cola.

        Returns
        -------
        FSMProcessResult
            Resultado detallado del procesamiento.
        """
        with self._lock:
            self.estado_emocional.decaer()

            if not self.event_queue:
                return FSMProcessResult(
                    accepted=False,
                    source_state=self.estado_actual,
                    target_state=None,
                    event=None,
                    reason=FSMRejectionReason.QUEUE_EMPTY,
                    message="No hay eventos pendientes en la cola.",
                    timestamp=time.time(),
                )

            queued_event = heapq.heappop(self.event_queue)
            estado_origen = self.estado_actual
            clave = (estado_origen, queued_event.event)
            rule = FSM_TRANSITIONS.get(clave)

            logger.info(
                "Procesando evento | state=%s event=%s source=%s priority=%s sequence=%s",
                estado_origen.name,
                queued_event.event.name,
                queued_event.source,
                queued_event.priority,
                queued_event.sequence,
            )

            if rule is None:
                self._modular_emocion_rechazo(
                    queued_event=queued_event,
                    reason=FSMRejectionReason.NO_TRANSITION_DEFINED,
                )
                result = FSMProcessResult(
                    accepted=False,
                    source_state=estado_origen,
                    target_state=None,
                    event=queued_event.event,
                    reason=FSMRejectionReason.NO_TRANSITION_DEFINED,
                    message=(
                        f"No existe transición definida para "
                        f"{estado_origen.name} + {queued_event.event.name}."
                    ),
                    timestamp=time.time(),
                    source=queued_event.source,
                    payload=queued_event.payload,
                )
                logger.warning(result.message)
                return result

            if not self._evaluar_condiciones(rule, self.contexto):
                self._modular_emocion_rechazo(
                    queued_event=queued_event,
                    reason=FSMRejectionReason.CONDITION_FAILED,
                )
                result = FSMProcessResult(
                    accepted=False,
                    source_state=estado_origen,
                    target_state=rule.target_state,
                    event=queued_event.event,
                    reason=FSMRejectionReason.CONDITION_FAILED,
                    message=(
                        f"Condición no satisfecha para "
                        f"{estado_origen.name} + {queued_event.event.name}."
                    ),
                    timestamp=time.time(),
                    source=queued_event.source,
                    payload=queued_event.payload,
                )
                logger.warning(result.message)
                return result

            if not self._evaluar_guardias(
                rule=rule,
                estado_origen=estado_origen,
                evento=queued_event.event,
                contexto=self.contexto,
            ):
                self._modular_emocion_rechazo(
                    queued_event=queued_event,
                    reason=FSMRejectionReason.GUARD_FAILED,
                )
                result = FSMProcessResult(
                    accepted=False,
                    source_state=estado_origen,
                    target_state=rule.target_state,
                    event=queued_event.event,
                    reason=FSMRejectionReason.GUARD_FAILED,
                    message=(
                        f"Guardia rechaza la transición "
                        f"{estado_origen.name} -> {rule.target_state.name} "
                        f"por {queued_event.event.name}."
                    ),
                    timestamp=time.time(),
                    source=queued_event.source,
                    payload=queued_event.payload,
                )
                logger.warning(result.message)
                return result

            self._ejecutar_acciones(rule, queued_event, estado_origen, rule.target_state)
            self._transicionar(rule.target_state, queued_event)
            self._modular_emocion_exito(queued_event, estado_origen, rule.target_state)

            result = FSMProcessResult(
                accepted=True,
                source_state=estado_origen,
                target_state=rule.target_state,
                event=queued_event.event,
                reason=None,
                message=(
                    f"Transición aplicada: {estado_origen.name} -> "
                    f"{rule.target_state.name} por {queued_event.event.name}."
                ),
                timestamp=time.time(),
                source=queued_event.source,
                payload=queued_event.payload,
            )
            logger.info(result.message)
            return result

    def _evaluar_condiciones(
        self,
        rule: FSMTransitionRule,
        contexto: FSMContext,
    ) -> bool:
        """
        Evalúa las condiciones asociadas a una transición.

        Parameters
        ----------
        rule : FSMTransitionRule
            Regla de transición.
        contexto : FSMContext
            Contexto operativo actual.

        Returns
        -------
        bool
            True si todas las condiciones son válidas.
        """
        return all(condition(contexto) for condition in rule.conditions)

    def _evaluar_guardias(
        self,
        rule: FSMTransitionRule,
        estado_origen: FSMState,
        evento: FSMEvent,
        contexto: FSMContext,
    ) -> bool:
        """
        Evalúa las guardias asociadas a una transición.

        Parameters
        ----------
        rule : FSMTransitionRule
            Regla de transición.
        estado_origen : FSMState
            Estado actual.
        evento : FSMEvent
            Evento que se está procesando.
        contexto : FSMContext
            Contexto operativo.

        Returns
        -------
        bool
            True si todas las guardias permiten la transición.
        """
        return all(
            guard(
                estado_origen,
                evento,
                rule.target_state,
                contexto,
            )
            for guard in rule.guards
        )

    def _ejecutar_acciones(
        self,
        rule: FSMTransitionRule,
        queued_event: FSMQueuedEvent,
        estado_origen: FSMState,
        estado_destino: FSMState,
    ) -> None:
        """
        Ejecuta las acciones asociadas a una transición válida.

        Parameters
        ----------
        rule : FSMTransitionRule
            Regla de transición validada.
        queued_event : FSMQueuedEvent
            Evento en proceso.
        estado_origen : FSMState
            Estado origen.
        estado_destino : FSMState
            Estado destino.
        """
        for action in rule.actions:
            action(self.contexto, queued_event, estado_origen, estado_destino)

    def _transicionar(
        self,
        nuevo_estado: FSMState,
        queued_event: FSMQueuedEvent,
    ) -> None:
        """
        Ejecuta la transición de estado y la registra en memoria y log.

        Parameters
        ----------
        nuevo_estado : FSMState
            Estado destino.
        queued_event : FSMQueuedEvent
            Evento que provoca la transición.
        """
        estado_anterior = self.estado_actual
        self.estado_actual = nuevo_estado

        transition_record = {
            "estado_anterior": estado_anterior.name,
            "evento": queued_event.event.name,
            "estado_nuevo": nuevo_estado.name,
            "timestamp": time.time(),
            "source": queued_event.source,
            "description": queued_event.description,
            "payload": queued_event.payload,
            "priority": queued_event.priority,
            "sequence": queued_event.sequence,
        }
        self.historial_transiciones.append(transition_record)

        logger.info(
            "Transición registrada | %s --(%s)--> %s | source=%s sequence=%s",
            estado_anterior.name,
            queued_event.event.name,
            nuevo_estado.name,
            queued_event.source,
            queued_event.sequence,
        )

    def _modular_emocion_exito(
        self,
        queued_event: FSMQueuedEvent,
        estado_origen: FSMState,
        estado_destino: FSMState,
    ) -> None:
        """
        Ajusta de forma básica el estado emocional tras una transición exitosa.

        Parameters
        ----------
        queued_event : FSMQueuedEvent
            Evento procesado.
        estado_origen : FSMState
            Estado de origen.
        estado_destino : FSMState
            Estado de destino.
        """
        if estado_destino in {FSMState.ATENDIENDO, FSMState.ESCUCHANDO, FSMState.OBSERVANDO}:
            self.estado_emocional.modular(
                EmotionalState.CURIOSIDAD,
                0.15,
                trigger=f"transition:{queued_event.event.name}",
            )
        elif estado_destino in {FSMState.INTERPRETANDO, FSMState.PLANIFICANDO, FSMState.EJECUTANDO_ACCION}:
            self.estado_emocional.modular(
                EmotionalState.FOCO,
                0.20,
                trigger=f"transition:{queued_event.event.name}",
            )
        elif estado_destino in {FSMState.HABLANDO, FSMState.FINALIZANDO_INTERACCION, FSMState.INACTIVO}:
            self.estado_emocional.modular(
                EmotionalState.SATISFACCION,
                0.10,
                trigger=f"transition:{queued_event.event.name}",
            )
        elif estado_destino == FSMState.RECUPERANDOSE:
            self.estado_emocional.modular(
                EmotionalState.RECUPERACION,
                0.20,
                trigger=f"transition:{queued_event.event.name}",
            )

    def _modular_emocion_rechazo(
        self,
        queued_event: FSMQueuedEvent,
        reason: FSMRejectionReason,
    ) -> None:
        """
        Ajusta de forma básica el estado emocional ante rechazos de transición.

        Parameters
        ----------
        queued_event : FSMQueuedEvent
            Evento rechazado.
        reason : FSMRejectionReason
            Motivo del rechazo.
        """
        if reason in {
            FSMRejectionReason.GUARD_FAILED,
            FSMRejectionReason.CONDITION_FAILED,
        }:
            self.estado_emocional.modular(
                EmotionalState.DUDA,
                0.10,
                trigger=f"reject:{queued_event.event.name}",
            )
        elif reason == FSMRejectionReason.NO_TRANSITION_DEFINED:
            self.estado_emocional.modular(
                EmotionalState.ALERTA,
                0.05,
                trigger=f"reject:{queued_event.event.name}",
            )

    def actualizar_contexto(self, nuevo_contexto: FSMContext) -> None:
        """
        Sustituye el contexto completo actual.

        Parameters
        ----------
        nuevo_contexto : FSMContext
            Nuevo contexto a aplicar.
        """
        with self._lock:
            self.contexto = nuevo_contexto

    def actualizar_contexto_parcial(self, **changes: Any) -> None:
        """
        Actualiza parcialmente el contexto actual.

        Parameters
        ----------
        **changes : Any
            Campos del contexto a modificar.
        """
        with self._lock:
            self.contexto.merge(**changes)

    def actualizar_estado_emocional(
        self,
        nuevo_estado: EmotionalState,
        intensidad: float,
        *,
        trigger: str | None = None,
        valencia: float | None = None,
        activacion: float | None = None,
    ) -> None:
        """
        Actualiza el estado emocional del sistema.

        Parameters
        ----------
        nuevo_estado : EmotionalState
            Nuevo estado emocional.
        intensidad : float
            Intensidad en rango [0, 1].
        trigger : str | None, optional
            Motivo principal del cambio emocional.
        valencia : float | None, optional
            Valencia explícita.
        activacion : float | None, optional
            Activación explícita.
        """
        with self._lock:
            self.estado_emocional.actualizar(
                nuevo_estado,
                intensidad,
                trigger=trigger,
                valencia=valencia,
                activacion=activacion,
            )

    def obtener_estado_actual(self) -> FSMState:
        """
        Devuelve el estado actual de la FSM.

        Returns
        -------
        FSMState
            Estado actual.
        """
        with self._lock:
            return self.estado_actual

    def obtener_historial_transiciones(self) -> list[dict[str, Any]]:
        """
        Devuelve una copia del historial reciente de transiciones.

        Returns
        -------
        list[dict[str, Any]]
            Historial en memoria.
        """
        with self._lock:
            return list(self.historial_transiciones)

    def obtener_numero_eventos_pendientes(self) -> int:
        """
        Devuelve el número de eventos pendientes en cola.

        Returns
        -------
        int
            Número de eventos pendientes.
        """
        with self._lock:
            return len(self.event_queue)

    def obtener_eventos_pendientes(self) -> list[dict[str, Any]]:
        """
        Devuelve una vista serializable de los eventos pendientes en cola.

        Returns
        -------
        list[dict[str, Any]]
            Eventos pendientes ordenados según prioridad actual.
        """
        with self._lock:
            return [
                {
                    "event": queued.event.name,
                    "timestamp": queued.timestamp,
                    "priority": queued.priority,
                    "sequence": queued.sequence,
                    "source": queued.source,
                    "description": queued.description,
                    "payload": queued.payload,
                }
                for queued in sorted(self.event_queue)
            ]

    def obtener_snapshot(self) -> dict[str, Any]:
        """
        Devuelve una instantánea serializable del estado interno de la FSM.

        Returns
        -------
        dict[str, Any]
            Snapshot del controlador.
        """
        with self._lock:
            return {
                "estado_actual": self.estado_actual.name,
                "contexto": self.contexto.__dict__.copy(),
                "estado_emocional": self.estado_emocional.snapshot(),
                "eventos_pendientes": self.obtener_eventos_pendientes(),
                "numero_eventos_pendientes": len(self.event_queue),
                "historial_size": len(self.historial_transiciones),
            }

    def reset(self, initial_state: FSMState = FSMState.INACTIVO) -> None:
        """
        Reinicia la FSM a un estado inicial y limpia memoria volátil.

        Parameters
        ----------
        initial_state : FSMState
            Estado al que debe volver la FSM.
        """
        with self._lock:
            self.estado_actual = initial_state
            self.contexto = FSMContext()
            self.estado_emocional = EmotionalStatus()
            self.event_queue.clear()
            self.historial_transiciones.clear()
            self._sequence = itertools.count()
            logger.info("FSM reiniciada a estado %s", initial_state.name)


fsm = FSMController()