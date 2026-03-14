"""
fsm_transitions.py

Definición declarativa de reglas de transición para la FSM de NORA.
Cada transición puede incluir estado destino, condiciones, guardias y
acciones asociadas a la transición.

Notas de diseño
----------------
- Este módulo solo declara reglas; no ejecuta la FSM.
- Las acciones aquí definidas son acciones internas de la FSM
  (actualización de contexto, timestamps, flags), no acciones
  externas del mundo real.
- La ejecución de acciones externas debe resolverse fuera del core,
  típicamente desde la capa application/action.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from .fsm_conditions import (
    FSMContext,
    condicion_activacion_no_inhibida,
    condicion_audio_operativo,
    condicion_escucha_no_inhibida,
    condicion_procesamiento_operativo,
    condicion_siempre,
    condicion_usuario_presente,
    condicion_vision_operativa,
)
from .fsm_definitions import FSMEvent, FSMQueuedEvent, FSMState
from .fsm_guard_clauses import (
    guardia_bloquear_ejecucion_si_acciones_inhibidas,
    guardia_bloquear_habla_si_audio_falla,
    guardia_bloquear_interpretacion_si_sin_usuario,
    guardia_bloquear_planificacion_si_procesamiento_falla,
    guardia_no_transicionar_a_escucha_si_audio_falla,
    guardia_no_transicionar_a_observacion_si_vision_falla,
    guardia_siempre_permitido,
)

ConditionFn = Callable[[FSMContext], bool]
GuardFn = Callable[[FSMState, FSMEvent, FSMState, FSMContext], bool]
ActionFn = Callable[[FSMContext, FSMQueuedEvent, FSMState, FSMState], None]


@dataclass(frozen=True)
class FSMTransitionRule:
    """
    Regla declarativa de transición de la FSM.

    Attributes
    ----------
    target_state : FSMState
        Estado destino.
    conditions : tuple[ConditionFn, ...]
        Condiciones asociadas al contexto.
    guards : tuple[GuardFn, ...]
        Guardias asociadas a la transición.
    actions : tuple[ActionFn, ...]
        Acciones a ejecutar tras validar la transición.
    """

    target_state: FSMState
    conditions: tuple[ConditionFn, ...] = field(default_factory=tuple)
    guards: tuple[GuardFn, ...] = field(default_factory=tuple)
    actions: tuple[ActionFn, ...] = field(default_factory=tuple)


# =========================================================
# ACCIONES INTERNAS DE FSM
# =========================================================


def accion_registrar_fuente_activacion(
    context: FSMContext,
    evento: FSMQueuedEvent,
    estado_origen: FSMState,
    estado_destino: FSMState,
) -> None:
    """
    Registra en el contexto la última fuente de activación y actualiza
    el timestamp del último evento.
    """
    context.ultima_fuente_activacion = evento.source
    context.ultimo_evento_ts = evento.timestamp


def accion_registrar_ultimo_evento(
    context: FSMContext,
    evento: FSMQueuedEvent,
    estado_origen: FSMState,
    estado_destino: FSMState,
) -> None:
    """
    Actualiza el timestamp del último evento procesado.
    """
    context.ultimo_evento_ts = evento.timestamp


def accion_marcar_interaccion_activa(
    context: FSMContext,
    evento: FSMQueuedEvent,
    estado_origen: FSMState,
    estado_destino: FSMState,
) -> None:
    """
    Marca el inicio o continuidad de una interacción activa.
    """
    context.interaccion_activa = True

    if context.inicio_interaccion_ts is None:
        context.inicio_interaccion_ts = evento.timestamp

    context.ultimo_evento_ts = evento.timestamp


def accion_limpiar_interaccion(
    context: FSMContext,
    evento: FSMQueuedEvent,
    estado_origen: FSMState,
    estado_destino: FSMState,
) -> None:
    """
    Limpia el contexto básico de interacción al cerrarse o abortarse.
    """
    context.interaccion_activa = False
    context.inicio_interaccion_ts = None
    context.ultima_intencion_detectada = None
    context.ultimo_evento_ts = evento.timestamp


def accion_registrar_intencion_desde_payload(
    context: FSMContext,
    evento: FSMQueuedEvent,
    estado_origen: FSMState,
    estado_destino: FSMState,
) -> None:
    """
    Registra en el contexto una intención detectada si viene en el payload.
    """
    possible_intent = evento.payload.get("intent")
    if isinstance(possible_intent, str) and possible_intent.strip():
        context.ultima_intencion_detectada = possible_intent.strip()

    context.ultimo_evento_ts = evento.timestamp


def accion_inhibir_activacion(
    context: FSMContext,
    evento: FSMQueuedEvent,
    estado_origen: FSMState,
    estado_destino: FSMState,
) -> None:
    """
    Inhibe activaciones externas.
    """
    context.activacion_inhibida = True
    context.ultimo_evento_ts = evento.timestamp


def accion_inhibir_escucha(
    context: FSMContext,
    evento: FSMQueuedEvent,
    estado_origen: FSMState,
    estado_destino: FSMState,
) -> None:
    """
    Inhibe la escucha por audio.
    """
    context.escucha_inhibida = True
    context.ultimo_evento_ts = evento.timestamp


def accion_habilitar_operacion_normal(
    context: FSMContext,
    evento: FSMQueuedEvent,
    estado_origen: FSMState,
    estado_destino: FSMState,
) -> None:
    """
    Restaura flags operativos básicos a un modo normal.
    """
    context.activacion_inhibida = False
    context.escucha_inhibida = False
    context.acciones_inhibidas = False
    context.ultimo_evento_ts = evento.timestamp


# =========================================================
# TABLA DE TRANSICIONES
# =========================================================

FSM_TRANSITIONS: dict[tuple[FSMState, FSMEvent], FSMTransitionRule] = {
    # =========================================================
    # CICLO DE VIDA DEL SISTEMA
    # =========================================================
    (FSMState.APAGADO, FSMEvent.EVT_BOOT): FSMTransitionRule(
        target_state=FSMState.INICIALIZANDO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.INICIALIZANDO, FSMEvent.EVT_INIT_COMPLETED): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_habilitar_operacion_normal, accion_limpiar_interaccion),
    ),
    (FSMState.INACTIVO, FSMEvent.EVT_SHUTDOWN): FSMTransitionRule(
        target_state=FSMState.APAGADO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),
    (FSMState.SUSPENDIDO, FSMEvent.EVT_SHUTDOWN): FSMTransitionRule(
        target_state=FSMState.APAGADO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),

    # =========================================================
    # ACTIVACIÓN DEL SISTEMA
    # =========================================================
    (FSMState.INACTIVO, FSMEvent.EVT_NFC_ACTIVATE): FSMTransitionRule(
        target_state=FSMState.ATENDIENDO,
        conditions=(condicion_activacion_no_inhibida,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_fuente_activacion, accion_marcar_interaccion_activa),
    ),
    (FSMState.INACTIVO, FSMEvent.EVT_WAKEWORD): FSMTransitionRule(
        target_state=FSMState.ATENDIENDO,
        conditions=(condicion_activacion_no_inhibida, condicion_audio_operativo),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_fuente_activacion, accion_marcar_interaccion_activa),
    ),
    (FSMState.INACTIVO, FSMEvent.EVT_PRESENCE_CONFIRMED): FSMTransitionRule(
        target_state=FSMState.ATENDIENDO,
        conditions=(condicion_activacion_no_inhibida, condicion_usuario_presente),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_fuente_activacion, accion_marcar_interaccion_activa),
    ),
    (FSMState.INACTIVO, FSMEvent.EVT_ATTENTION_GAINED): FSMTransitionRule(
        target_state=FSMState.ATENDIENDO,
        conditions=(condicion_activacion_no_inhibida, condicion_usuario_presente),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_fuente_activacion, accion_marcar_interaccion_activa),
    ),
    (FSMState.INACTIVO, FSMEvent.EVT_SCHEDULE_TRIGGERED): FSMTransitionRule(
        target_state=FSMState.ATENDIENDO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_fuente_activacion, accion_marcar_interaccion_activa),
    ),

    # =========================================================
    # ATENCIÓN INICIAL
    # =========================================================
    (FSMState.ATENDIENDO, FSMEvent.EVT_SPEECH_START): FSMTransitionRule(
        target_state=FSMState.ESCUCHANDO,
        conditions=(condicion_audio_operativo, condicion_escucha_no_inhibida),
        guards=(guardia_no_transicionar_a_escucha_si_audio_falla,),
        actions=(accion_registrar_ultimo_evento, accion_marcar_interaccion_activa),
    ),
    (FSMState.ATENDIENDO, FSMEvent.EVT_GESTURE_DETECTED): FSMTransitionRule(
        target_state=FSMState.OBSERVANDO,
        conditions=(condicion_usuario_presente, condicion_vision_operativa),
        guards=(guardia_no_transicionar_a_observacion_si_vision_falla,),
        actions=(accion_registrar_ultimo_evento, accion_marcar_interaccion_activa),
    ),
    (FSMState.ATENDIENDO, FSMEvent.EVT_READ_REQUEST_DETECTED): FSMTransitionRule(
        target_state=FSMState.OBSERVANDO,
        conditions=(condicion_vision_operativa,),
        guards=(guardia_no_transicionar_a_observacion_si_vision_falla,),
        actions=(accion_registrar_ultimo_evento, accion_marcar_interaccion_activa),
    ),
    (FSMState.ATENDIENDO, FSMEvent.EVT_IDLE_TIMEOUT): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),
    (FSMState.ATENDIENDO, FSMEvent.EVT_ATTENTION_LOST): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),

    # =========================================================
    # CAPTURA DE ENTRADA
    # =========================================================
    (FSMState.ESCUCHANDO, FSMEvent.EVT_SPEECH_RECOGNIZED): FSMTransitionRule(
        target_state=FSMState.INTERPRETANDO,
        conditions=(condicion_audio_operativo,),
        guards=(guardia_bloquear_interpretacion_si_sin_usuario,),
        actions=(
            accion_registrar_ultimo_evento,
            accion_marcar_interaccion_activa,
            accion_registrar_intencion_desde_payload,
        ),
    ),
    (FSMState.ESCUCHANDO, FSMEvent.EVT_LISTEN_TIMEOUT): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),
    (FSMState.ESCUCHANDO, FSMEvent.CMD_CANCEL_LISTENING): FSMTransitionRule(
        target_state=FSMState.ATENDIENDO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.OBSERVANDO, FSMEvent.EVT_GESTURE_COMMAND): FSMTransitionRule(
        target_state=FSMState.INTERPRETANDO,
        conditions=(condicion_usuario_presente,),
        guards=(guardia_bloquear_interpretacion_si_sin_usuario,),
        actions=(
            accion_registrar_ultimo_evento,
            accion_marcar_interaccion_activa,
            accion_registrar_intencion_desde_payload,
        ),
    ),
    (FSMState.OBSERVANDO, FSMEvent.EVT_ATTENTION_LOST): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),
    (FSMState.OBSERVANDO, FSMEvent.EVT_IDLE_TIMEOUT): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),

    # =========================================================
    # INTERPRETACIÓN
    # =========================================================
    (FSMState.INTERPRETANDO, FSMEvent.EVT_INPUT_INTERPRETED): FSMTransitionRule(
        target_state=FSMState.PLANIFICANDO,
        conditions=(condicion_procesamiento_operativo,),
        guards=(guardia_bloquear_planificacion_si_procesamiento_falla,),
        actions=(accion_registrar_ultimo_evento, accion_marcar_interaccion_activa),
    ),
    (FSMState.INTERPRETANDO, FSMEvent.EVT_PROCESS_FAILURE): FSMTransitionRule(
        target_state=FSMState.ERROR,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.INTERPRETANDO, FSMEvent.EVT_CONTEXT_LOST): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),

    # =========================================================
    # PLANIFICACIÓN
    # =========================================================
    (FSMState.PLANIFICANDO, FSMEvent.EVT_PLAN_READY): FSMTransitionRule(
        target_state=FSMState.EJECUTANDO_ACCION,
        conditions=(condicion_siempre,),
        guards=(guardia_bloquear_ejecucion_si_acciones_inhibidas,),
        actions=(accion_registrar_ultimo_evento, accion_marcar_interaccion_activa),
    ),
    (FSMState.PLANIFICANDO, FSMEvent.EVT_CONFIRMATION_REQUIRED): FSMTransitionRule(
        target_state=FSMState.ESPERANDO_CONFIRMACION,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento, accion_marcar_interaccion_activa),
    ),
    (FSMState.PLANIFICANDO, FSMEvent.EVT_PROCESS_FAILURE): FSMTransitionRule(
        target_state=FSMState.ERROR,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),

    # =========================================================
    # CONFIRMACIÓN
    # =========================================================
    (FSMState.ESPERANDO_CONFIRMACION, FSMEvent.EVT_CONFIRMATION_RECEIVED): FSMTransitionRule(
        target_state=FSMState.EJECUTANDO_ACCION,
        conditions=(condicion_siempre,),
        guards=(guardia_bloquear_ejecucion_si_acciones_inhibidas,),
        actions=(accion_registrar_ultimo_evento, accion_marcar_interaccion_activa),
    ),
    (FSMState.ESPERANDO_CONFIRMACION, FSMEvent.EVT_CONFIRMATION_REJECTED): FSMTransitionRule(
        target_state=FSMState.FINALIZANDO_INTERACCION,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.ESPERANDO_CONFIRMACION, FSMEvent.EVT_CONFIRMATION_TIMEOUT): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),

    # =========================================================
    # EJECUCIÓN
    # =========================================================
    (FSMState.EJECUTANDO_ACCION, FSMEvent.EVT_ACTION_STARTED): FSMTransitionRule(
        target_state=FSMState.EJECUTANDO_ACCION,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.EJECUTANDO_ACCION, FSMEvent.EVT_ACTION_COMPLETED): FSMTransitionRule(
        target_state=FSMState.HABLANDO,
        conditions=(condicion_audio_operativo,),
        guards=(guardia_bloquear_habla_si_audio_falla,),
        actions=(accion_registrar_ultimo_evento, accion_marcar_interaccion_activa),
    ),
    (FSMState.EJECUTANDO_ACCION, FSMEvent.EVT_ACTION_FAILED): FSMTransitionRule(
        target_state=FSMState.ERROR,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.EJECUTANDO_ACCION, FSMEvent.EVT_ACTION_TIMEOUT): FSMTransitionRule(
        target_state=FSMState.ERROR,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.EJECUTANDO_ACCION, FSMEvent.CMD_CANCEL_ACTION): FSMTransitionRule(
        target_state=FSMState.FINALIZANDO_INTERACCION,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),

    # =========================================================
    # RESPUESTA VERBAL
    # =========================================================
    (FSMState.HABLANDO, FSMEvent.EVT_SPEECH_OUTPUT_FINISHED): FSMTransitionRule(
        target_state=FSMState.FINALIZANDO_INTERACCION,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.HABLANDO, FSMEvent.EVT_ACTION_FAILED): FSMTransitionRule(
        target_state=FSMState.ERROR,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),

    # =========================================================
    # CIERRE DE INTERACCIÓN
    # =========================================================
    (FSMState.FINALIZANDO_INTERACCION, FSMEvent.EVT_INTERACTION_FINISHED): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),
    (FSMState.FINALIZANDO_INTERACCION, FSMEvent.EVT_IDLE_TIMEOUT): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_limpiar_interaccion,),
    ),

    # =========================================================
    # SUSPENSIÓN
    # =========================================================
    (FSMState.INACTIVO, FSMEvent.CMD_SUSPEND): FSMTransitionRule(
        target_state=FSMState.SUSPENDIDO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_inhibir_activacion, accion_limpiar_interaccion),
    ),
    (FSMState.ATENDIENDO, FSMEvent.CMD_SUSPEND): FSMTransitionRule(
        target_state=FSMState.SUSPENDIDO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_inhibir_activacion, accion_limpiar_interaccion),
    ),
    (FSMState.ESCUCHANDO, FSMEvent.CMD_SUSPEND): FSMTransitionRule(
        target_state=FSMState.SUSPENDIDO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_inhibir_activacion, accion_inhibir_escucha, accion_limpiar_interaccion),
    ),
    (FSMState.OBSERVANDO, FSMEvent.CMD_SUSPEND): FSMTransitionRule(
        target_state=FSMState.SUSPENDIDO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_inhibir_activacion, accion_limpiar_interaccion),
    ),
    (FSMState.SUSPENDIDO, FSMEvent.CMD_WAKE): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_habilitar_operacion_normal, accion_limpiar_interaccion),
    ),
    (FSMState.SUSPENDIDO, FSMEvent.CMD_FORCE_RESUME): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_habilitar_operacion_normal, accion_limpiar_interaccion),
    ),

    # =========================================================
    # ERROR Y RECUPERACIÓN
    # =========================================================
    (FSMState.ERROR, FSMEvent.EVT_RECOVERY_STARTED): FSMTransitionRule(
        target_state=FSMState.RECUPERANDOSE,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.ERROR, FSMEvent.CMD_FORCE_RESUME): FSMTransitionRule(
        target_state=FSMState.RECUPERANDOSE,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
    (FSMState.RECUPERANDOSE, FSMEvent.EVT_RECOVERY_SUCCESS): FSMTransitionRule(
        target_state=FSMState.INACTIVO,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_habilitar_operacion_normal, accion_limpiar_interaccion),
    ),
    (FSMState.RECUPERANDOSE, FSMEvent.EVT_ERROR_RECOVERY_TIMEOUT): FSMTransitionRule(
        target_state=FSMState.ERROR,
        conditions=(condicion_siempre,),
        guards=(guardia_siempre_permitido,),
        actions=(accion_registrar_ultimo_evento,),
    ),
}