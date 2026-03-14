"""
events_views.py

Vistas HTTP para la ingesta de eventos externos del sistema NORA.

Responsabilidades
-----------------
- Recibir eventos externos vía HTTP.
- Validar su forma básica.
- Aplicar control básico de cooldown.
- Delegar el caso de uso a la capa de aplicación.

Este módulo no debe contener lógica de transición FSM ni ejecución
directa de acciones complejas del sistema.
"""

import logging
import time
from typing import Any

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.application.event_service import EventApplicationService
from core.state_machine.definitions.fsm_definitions import FSMEvent


logger = logging.getLogger(__name__)

event_service = EventApplicationService()

LAST_EVENT_TS: dict[str, float] = {
    "audio": 0.0,
    "video": 0.0,
}

EVENT_COOLDOWNS_SECONDS: dict[str, float] = {
    "audio": 2.0,
    "video": 2.0,
}


def _check_and_update_cooldown(channel: str) -> tuple[bool, float, float]:
    """
    Comprueba si el canal está dentro de cooldown y actualiza su timestamp
    si procede.

    Parameters
    ----------
    channel : str
        Canal lógico de entrada.

    Returns
    -------
    tuple[bool, float, float]
        (ignorar, delta, cooldown_seconds)
    """
    now_ts = time.time()
    last_ts = LAST_EVENT_TS.get(channel, 0.0)
    cooldown_seconds = EVENT_COOLDOWNS_SECONDS.get(channel, 0.0)
    delta = now_ts - last_ts

    if delta < cooldown_seconds:
        return True, delta, cooldown_seconds

    LAST_EVENT_TS[channel] = now_ts
    return False, delta, cooldown_seconds


def _build_cooldown_response(
    message: str,
    delta_seconds: float,
    cooldown_seconds: float,
) -> Response:
    """
    Construye una respuesta estándar para eventos ignorados por cooldown.
    """
    return Response(
        {
            "accepted": False,
            "reason": "cooldown",
            "message": message,
            "delta_seconds": round(delta_seconds, 3),
            "cooldown_seconds": cooldown_seconds,
        },
        status=status.HTTP_200_OK,
    )


def _publish_ws_event(
    *,
    event_name: str,
    fsm_result: dict[str, Any],
    description: str,
    source: str | None,
) -> None:
    """
    Publica una actualización FSM resumida por WebSocket.
    """
    channel_layer = get_channel_layer()

    if channel_layer is None:
        logger.warning("No hay channel layer disponible para publicar WebSocket.")
        return

    ws_payload = {
        "evento": event_name,
        "descripcion": description,
        "source": source,
        "accepted": fsm_result.get("accepted"),
        "source_state": fsm_result.get("source_state"),
        "target_state": fsm_result.get("target_state"),
        "estado_actual": fsm_result.get("estado_actual"),
        "reason": fsm_result.get("reason"),
        "message": fsm_result.get("message"),
    }

    async_to_sync(channel_layer.group_send)(
        "fsm_updates",
        {
            "type": "enviar_evento_fsm",
            "data": ws_payload,
        },
    )

    logger.info("Evento publicado por WebSocket: %s", ws_payload)


def _serialize_intents(intents: list[Any]) -> list[dict[str, Any]]:
    """
    Serializa intenciones de aplicación para la respuesta HTTP.
    """
    serialized: list[dict[str, Any]] = []

    for intent in intents:
        serialized.append(
            {
                "intent_type": intent.intent_type.name,
                "payload": intent.payload,
                "description": intent.description,
            }
        )

    return serialized


def _handle_external_activation_event(
    *,
    request_data: dict[str, Any],
    expected_event_type: str,
    fsm_event: FSMEvent,
    channel_key: str,
    description: str,
) -> Response:
    """
    Flujo común para eventos externos de activación.
    """
    event_type = request_data.get("event_type")
    source = request_data.get("source", f"api.events.{channel_key}")
    timestamp = request_data.get("timestamp")
    payload = request_data.get("payload", {})

    if event_type != expected_event_type:
        logger.warning(
            "Unsupported event_type recibido. expected=%s got=%s",
            expected_event_type,
            event_type,
        )
        return Response(
            {"detail": "Unsupported event_type."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    ignored, delta, cooldown_seconds = _check_and_update_cooldown(channel_key)

    if ignored:
        logger.info(
            "Evento ignorado por cooldown. channel=%s delta=%.3f cooldown=%.3f",
            channel_key,
            delta,
            cooldown_seconds,
        )
        return _build_cooldown_response(
            message=f"{channel_key.capitalize()} event ignored due to cooldown.",
            delta_seconds=delta,
            cooldown_seconds=cooldown_seconds,
        )

    try:
        app_result = event_service.handle_event(
            evento=fsm_event,
            descripcion=description,
            source=source,
            payload=payload,
            timestamp=timestamp,
            execute_actions=True,
        )
    except Exception as exc:
        logger.exception("Error ejecutando EventApplicationService: %s", exc)
        return Response(
            {"detail": f"Application error: {exc}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    try:
        _publish_ws_event(
            event_name=fsm_event.name,
            fsm_result=app_result.fsm_result,
            description=description,
            source=source,
        )
    except Exception as exc:
        logger.exception("Error enviando WebSocket: %s", exc)

    return Response(
        {
            "message": f"{channel_key.capitalize()} event received successfully.",
            "source": source,
            "timestamp": timestamp,
            "event_type": event_type,
            "fsm_event": fsm_event.name,
            "fsm_result": app_result.fsm_result,
            "estado_actual": app_result.fsm_result.get("estado_actual"),
            "intents": _serialize_intents(app_result.intents),
            "executed_intents": app_result.executed_intents,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def recibir_evento_audio(request: Any) -> Response:
    """
    Recibe un evento del subsistema de audio y lo traduce a un evento FSM.
    """
    logger.info("Evento de audio recibido.")

    data = request.data
    payload = data.get("payload", {})

    keyword = payload.get("keyword")
    confidence = payload.get("confidence")

    response = _handle_external_activation_event(
        request_data=data,
        expected_event_type="wake_word_detected",
        fsm_event=FSMEvent.EVT_WAKEWORD,
        channel_key="audio",
        description="Wake word detectada",
    )

    if response.status_code == status.HTTP_200_OK:
        response.data["keyword"] = keyword
        response.data["confidence"] = confidence

    return response


@api_view(["POST"])
def recibir_evento_video(request: Any) -> Response:
    """
    Recibe un evento del subsistema de visión y lo traduce a un evento FSM.
    """
    logger.info("Evento de video recibido.")

    data = request.data
    payload = data.get("payload", {})

    gesture = payload.get("gesture")
    confidence = payload.get("confidence")
    metadata = payload.get("metadata", {})

    response = _handle_external_activation_event(
        request_data=data,
        expected_event_type="vision_activation",
        fsm_event=FSMEvent.EVT_PRESENCE_CONFIRMED,
        channel_key="video",
        description=f"Gesto de activación detectado: {gesture}",
    )

    if response.status_code == status.HTTP_200_OK:
        response.data["gesture"] = gesture
        response.data["confidence"] = confidence
        response.data["metadata"] = metadata

    return response