"""
dispatcher.py

Módulo de entrada de eventos al core FSM. Se encarga de encolar un evento
y solicitar su procesamiento inmediato.

Notas
-----
El resultado devuelto corresponde al siguiente evento procesado por la FSM,
que normalmente será el recién emitido, pero podría no coincidir con él si
ya existían eventos pendientes en cola con mayor prioridad.
"""

from __future__ import annotations

import logging
from typing import Any

from core.state_machine.definitions.fsm_definitions import FSMEvent, FSMProcessResult
from core.state_machine.fsm_controller import fsm

logger = logging.getLogger("fsm.dispatcher")


def emitir_evento(
    evento: FSMEvent,
    descripcion: str = "",
    source: str = "unknown",
    payload: dict[str, Any] | None = None,
    timestamp: float | None = None,
) -> FSMProcessResult:
    """
    Encola un evento en la FSM y solicita el procesamiento inmediato del
    siguiente evento pendiente.

    Parameters
    ----------
    evento : FSMEvent
        Evento lógico a emitir.
    descripcion : str, optional
        Descripción legible del evento.
    source : str, optional
        Fuente del evento.
    payload : dict[str, Any] | None, optional
        Metadatos asociados al evento.
    timestamp : float | None, optional
        Marca temporal explícita del evento. Si no se proporciona, el
        controlador utilizará el tiempo actual.

    Returns
    -------
    FSMProcessResult
        Resultado detallado del procesamiento del siguiente evento atendido
        por la FSM.

    Notes
    -----
    El evento procesado tras la llamada puede no coincidir con el evento recién
    encolado si existen otros eventos pendientes con mayor prioridad.
    """
    logger.info(
        "Emitir evento | event=%s source=%s description=%s",
        evento.name,
        source,
        descripcion,
    )

    fsm.recibir_evento(
        evento=evento,
        timestamp=timestamp,
        source=source,
        description=descripcion,
        payload=payload,
    )

    result = fsm.procesar_siguiente_evento()

    logger.info(
        (
            "Resultado evento | accepted=%s processed_event=%s "
            "source_state=%s target_state=%s reason=%s message=%s"
        ),
        result.accepted,
        result.event.name if result.event else None,
        result.source_state.name if result.source_state else None,
        result.target_state.name if result.target_state else None,
        result.reason.name if result.reason else None,
        result.message,
    )

    return result