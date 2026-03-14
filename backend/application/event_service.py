"""
event_service.py

Caso de uso principal para recepción de eventos, procesamiento FSM
y ejecución de acciones derivadas.
"""

from __future__ import annotations

import logging
from typing import Any

from backend.application.action_executor import ActionExecutor
from backend.application.action_planner import ActionPlanner
from backend.application.dtos import ApplicationDispatchResult
from core.state_machine.definitions.fsm_definitions import FSMEvent
from core.state_machine.dispatcher import emitir_evento


logger = logging.getLogger(__name__)


class EventApplicationService:
    """
    Servicio de aplicación para procesar eventos de extremo a extremo.
    """

    def __init__(
        self,
        action_planner: ActionPlanner | None = None,
        action_executor: ActionExecutor | None = None,
    ) -> None:
        self.action_planner = action_planner or ActionPlanner()
        self.action_executor = action_executor or ActionExecutor()

    def handle_event(
        self,
        *,
        evento: FSMEvent,
        descripcion: str = "",
        source: str = "unknown",
        payload: dict[str, Any] | None = None,
        timestamp: float | None = None,
        execute_actions: bool = True,
    ) -> ApplicationDispatchResult:
        """
        Procesa un evento completo: FSM + planificación de acciones + ejecución.

        Parameters
        ----------
        evento : FSMEvent
            Evento FSM a emitir.
        descripcion : str
            Descripción legible del evento.
        source : str
            Fuente lógica del evento.
        payload : dict[str, Any] | None
            Payload del evento.
        timestamp : float | None
            Marca temporal opcional.
        execute_actions : bool
            Si es True, ejecuta automáticamente las intenciones generadas.

        Returns
        -------
        ApplicationDispatchResult
            Resultado agregado del caso de uso.
        """
        logger.info(
            "Application handle_event | event=%s source=%s description=%s",
            evento.name,
            source,
            descripcion,
        )

        fsm_process_result = emitir_evento(
            evento=evento,
            descripcion=descripcion,
            source=source,
            payload=payload,
            timestamp=timestamp,
        )

        fsm_result = self._fsm_result_to_dict(fsm_process_result)

        intents = self.action_planner.build_intents_from_fsm_result(fsm_result)

        executed_intents: list[dict[str, Any]] = []
        if execute_actions:
            for intent in intents:
                execution_result = self.action_executor.execute(intent)
                executed_intents.append(execution_result)

        return ApplicationDispatchResult(
            fsm_result=fsm_result,
            intents=intents,
            executed_intents=executed_intents,
        )

    @staticmethod
    def _fsm_result_to_dict(result: Any) -> dict[str, Any]:
        """
        Convierte FSMProcessResult a dict serializable.
        """
        source_state = getattr(result, "source_state", None)
        target_state = getattr(result, "target_state", None)
        event = getattr(result, "event", None)
        reason = getattr(result, "reason", None)

        estado_actual = (
            target_state.name
            if target_state is not None
            else (source_state.name if source_state is not None else None)
        )

        return {
            "accepted": getattr(result, "accepted", False),
            "event": event.name if event is not None else None,
            "source_state": source_state.name if source_state is not None else None,
            "target_state": target_state.name if target_state is not None else None,
            "reason": reason.name if reason is not None else None,
            "message": getattr(result, "message", ""),
            "timestamp": getattr(result, "timestamp", None),
            "source": getattr(result, "source", ""),
            "payload": getattr(result, "payload", {}),
            "estado_actual": estado_actual,
        }