"""
contracts.py

Contratos y tipos base de la capa de aplicación.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ExecutionContext:
    """
    Contexto de ejecución del caso de uso.

    Attributes
    ----------
    source : str
        Fuente lógica del evento o acción.
    correlation_id : str | None
        Identificador opcional para trazabilidad.
    metadata : dict[str, Any]
        Metadatos auxiliares.
    """
    source: str = "unknown"
    correlation_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)