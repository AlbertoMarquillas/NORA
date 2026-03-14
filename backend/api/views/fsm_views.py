"""
fsm_views.py

Vistas HTTP para interacción con la máquina de estados finita (FSM) del sistema NORA.

Responsabilidades
-----------------
- Recibir eventos explícitos desde frontend o herramientas de backend.
- Traducir datos HTTP a eventos FSM.
- Consultar el estado actual de la máquina de estados.
- Consultar el historial de transiciones persistido.

Este módulo no debe contener lógica compleja de negocio ni de sensores,
solo la traducción entre HTTP y la capa de aplicación.
"""

import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.application.event_service import EventApplicationService
from backend.application.state_service import StateApplicationService
from backend.persistence.models.events_models import TransicionFSM
from core.state_machine.definitions.fsm_definitions import FSMEvent


logger = logging.getLogger(__name__)

event_service = EventApplicationService()
state_service = StateApplicationService()


def _serialize_intents(intents: list[object]) -> list[dict]:
    """
    Serializa intenciones de aplicación para devolverlas por HTTP.
    """
    serialized: list[dict] = []

    for intent in intents:
        serialized.append(
            {
                "intent_type": intent.intent_type.name,
                "payload": intent.payload,
                "description": intent.description,
            }
        )

    return serialized


@api_view(["POST"])
def recibir_evento_fsm(request):
    """
    Recibe un evento FSM explícito desde frontend o herramientas de administración.

    Request JSON
    ------------
    {
        "evento": "EVT_WAKEWORD"
    }

    Returns
    -------
    dict
        Resultado serializable del procesamiento del evento FSM.
    """
    nombre_evento = request.data.get("evento")
    descripcion = request.data.get("descripcion", "")
    source = request.data.get("source", "api.fsm")
    payload = request.data.get("payload", {})
    timestamp = request.data.get("timestamp")

    if not nombre_evento:
        return Response(
            {"error": "No se ha especificado un evento"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        evento = FSMEvent[nombre_evento]
    except KeyError:
        return Response(
            {"error": f"Evento no reconocido: {nombre_evento}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    logger.info("Evento FSM recibido por API: %s", nombre_evento)

    try:
        app_result = event_service.handle_event(
            evento=evento,
            descripcion=descripcion,
            source=source,
            payload=payload,
            timestamp=timestamp,
            execute_actions=True,
        )
    except Exception as exc:
        logger.exception("Error ejecutando FSM: %s", exc)
        return Response(
            {"error": "Error interno en FSM"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(
        {
            "fsm_result": app_result.fsm_result,
            "estado_actual": app_result.fsm_result.get("estado_actual"),
            "intents": _serialize_intents(app_result.intents),
            "executed_intents": app_result.executed_intents,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def recibir_sensor_backend(request):
    """
    Recibe datos de sensores del backend que pueden generar eventos FSM.

    Ejemplo
    -------
    {
        "sensor": "temperatura",
        "value": 47
    }
    """
    sensor = request.data.get("sensor")
    valor = request.data.get("value")
    source = request.data.get("source", "api.fsm.sensor")
    timestamp = request.data.get("timestamp")

    if sensor is None:
        return Response(
            {"error": "Sensor no especificado"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        valor = float(valor)
    except (TypeError, ValueError):
        return Response(
            {"error": "Valor numérico inválido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    logger.info("Sensor recibido: %s valor=%s", sensor, valor)

    evento = None
    descripcion = ""
    payload = {
        "sensor": sensor,
        "value": valor,
    }

    if sensor == "temperatura":
        if valor > 45:
            evento = FSMEvent.EVT_MODULE_FAILURE
            descripcion = "Temperatura crítica detectada"
        elif valor < 0:
            evento = FSMEvent.CMD_INHIBIR_ACTIVACION
            descripcion = "Temperatura anómala baja; activación inhibida"

    if evento is None:
        return Response(
            {
                "accepted": False,
                "message": "No se generó ningún evento FSM",
                "estado_actual": state_service.get_current_state(),
            },
            status=status.HTTP_200_OK,
        )

    try:
        app_result = event_service.handle_event(
            evento=evento,
            descripcion=descripcion,
            source=source,
            payload=payload,
            timestamp=timestamp,
            execute_actions=True,
        )
    except Exception as exc:
        logger.exception("Error ejecutando FSM: %s", exc)
        return Response(
            {"error": "Error interno en FSM"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(
        {
            "fsm_result": app_result.fsm_result,
            "estado_actual": app_result.fsm_result.get("estado_actual"),
            "intents": _serialize_intents(app_result.intents),
            "executed_intents": app_result.executed_intents,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def obtener_estado_actual(request):
    """
    Devuelve el estado actual de la FSM.
    """
    return Response(
        {
            "estado_actual": state_service.get_current_state(),
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def lista_transiciones(request):
    """
    Devuelve las últimas transiciones persistidas de la FSM.
    """
    transiciones = TransicionFSM.objects.order_by("-timestamp")[:50]

    data = [
        {
            "timestamp": t.timestamp,
            "estado_anterior": t.estado_anterior,
            "evento": t.evento,
            "estado_nuevo": t.estado_nuevo,
        }
        for t in transiciones
    ]

    return Response(data, status=status.HTTP_200_OK)