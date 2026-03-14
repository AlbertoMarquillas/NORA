"""
dtos.py

DTOs de la capa de aplicación para resultados de casos de uso.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from backend.application.intents import ActionIntent


@dataclass(slots=True)
class ApplicationDispatchResult:
    """
    Resultado agregado de un caso de uso de despacho de evento.

    Attributes
    ----------
    fsm_result : dict[str, Any]
        Resultado serializable de la FSM.
    intents : list[ActionIntent]
        Intenciones generadas tras procesar el evento.
    executed_intents : list[dict[str, Any]]
        Resultado de ejecución de intenciones.
    """
    fsm_result: dict[str, Any]
    intents: list[ActionIntent] = field(default_factory=list)
    executed_intents: list[dict[str, Any]] = field(default_factory=list)