"""
state_service.py

Servicios de aplicación para consulta del estado de la FSM.
"""

from __future__ import annotations

from typing import Any

from core.state_machine.fsm_controller import fsm


class StateApplicationService:
    """
    Servicio de aplicación para lectura del estado del core FSM.
    """

    def get_fsm_snapshot(self) -> dict[str, Any]:
        """
        Devuelve una instantánea serializable del estado FSM.

        Returns
        -------
        dict[str, Any]
            Snapshot del controlador FSM.
        """
        return fsm.obtener_snapshot()

    def get_current_state(self) -> str:
        """
        Devuelve el nombre del estado actual.

        Returns
        -------
        str
            Nombre del estado actual.
        """
        return fsm.obtener_estado_actual().name