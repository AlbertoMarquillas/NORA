"""
action_planner.py

Traduce transiciones de la FSM a intenciones ejecutables
por la capa action.
"""

from __future__ import annotations

from typing import Any, List

from backend.application.intents import ActionIntent, ActionIntentType


class ActionPlanner:
    """
    Planificador de acciones basado en resultados de la FSM.
    """

    def build_intents_from_fsm_result(
        self,
        fsm_result: dict[str, Any],
    ) -> List[ActionIntent]:
        """
        Genera intenciones ejecutables a partir del resultado FSM.
        """

        intents: List[ActionIntent] = []

        if not fsm_result.get("accepted"):
            return intents

        source_state = fsm_result.get("source_state")
        target_state = fsm_result.get("target_state")
        event = fsm_result.get("event")
        payload = fsm_result.get("payload") or {}

        # =====================================================
        # ACTIVACIÓN DE ESCUCHA
        # =====================================================

        if target_state == "ESCUCHANDO" and source_state != "ESCUCHANDO":

            intents.append(
                ActionIntent(
                    intent_type=ActionIntentType.START_LISTENING,
                    description="Activar captura de voz.",
                )
            )

        # =====================================================
        # RESPUESTA VERBAL
        # =====================================================

        if target_state == "HABLANDO":

            text = payload.get(
                "text",
                "He completado la acción y estoy lista para continuar.",
            )

            intents.append(
                ActionIntent(
                    intent_type=ActionIntentType.SPEAK_TEXT,
                    payload={"text": text},
                    description="Emitir respuesta verbal.",
                )
            )

        # =====================================================
        # FINALIZACIÓN INTERACCIÓN
        # =====================================================

        if target_state == "FINALIZANDO_INTERACCION":

            intents.append(
                ActionIntent(
                    intent_type=ActionIntentType.STOP_LISTENING,
                    description="Cerrar captura de voz.",
                )
            )

        # =====================================================
        # EJECUCIÓN DE ACCIÓN
        # =====================================================

        if target_state == "EJECUTANDO_ACCION":

            intent_name = payload.get("intent")

            if intent_name:

                intents.append(
                    ActionIntent(
                        intent_type=ActionIntentType.EXECUTE_TASK,
                        payload={
                            "intent": intent_name,
                            "parameters": payload.get("parameters", {}),
                        },
                        description="Ejecutar acción solicitada.",
                    )
                )

        return intents