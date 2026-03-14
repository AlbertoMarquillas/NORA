"""
action_executor.py

Ejecutor de intenciones de alto nivel.
"""

from __future__ import annotations

import logging
from typing import Any, Callable

from action.speech.service import build_speech_service
from backend.application.exceptions import UnsupportedActionIntentError
from backend.application.intents import ActionIntent, ActionIntentType


logger = logging.getLogger(__name__)


class ActionExecutor:
    """
    Ejecuta ActionIntent provenientes de la capa application.

    Este componente traduce intenciones de alto nivel a llamadas
    a la capa action (hardware, servicios, dispositivos).
    """

    def __init__(self) -> None:

        self._handlers: dict[
            ActionIntentType,
            Callable[[ActionIntent], dict[str, Any]],
        ] = {

            # core
            ActionIntentType.NO_OP: self._execute_no_op,

            # audio output
            ActionIntentType.SPEAK_TEXT: self._execute_speak_text,
            ActionIntentType.PLAY_SOUND: self._execute_play_sound,
            ActionIntentType.PLAY_MUSIC: self._execute_play_music,
            ActionIntentType.STOP_AUDIO: self._execute_stop_audio,

            # listening
            ActionIntentType.START_LISTENING: self._execute_start_listening,
            ActionIntentType.STOP_LISTENING: self._execute_stop_listening,

            # vision
            ActionIntentType.CAPTURE_IMAGE: self._execute_capture_image,
            ActionIntentType.CAPTURE_VIDEO: self._execute_capture_video,

            # screen
            ActionIntentType.DISPLAY_TEXT: self._execute_display_text,
            ActionIntentType.DISPLAY_IMAGE: self._execute_display_image,
            ActionIntentType.DISPLAY_VIDEO: self._execute_display_video,
            ActionIntentType.DISPLAY_EMOTION: self._execute_display_emotion,
            ActionIntentType.CLEAR_SCREEN: self._execute_clear_screen,

            # leds
            ActionIntentType.SET_LED_COLOR: self._execute_led_color,
            ActionIntentType.SET_LED_PATTERN: self._execute_led_pattern,
            ActionIntentType.BLINK_LED: self._execute_led_blink,

            # motion
            ActionIntentType.MOVE_HEAD: self._execute_move_head,
            ActionIntentType.MOVE_ARM: self._execute_move_arm,
            ActionIntentType.MOVE_BODY: self._execute_move_body,
            ActionIntentType.LOOK_AT_TARGET: self._execute_look_at_target,

            # emotions
            ActionIntentType.SET_EMOTION: self._execute_set_emotion,

            # cognition
            ActionIntentType.READ_CONTENT: self._execute_read_content,
            ActionIntentType.SEARCH_INFORMATION: self._execute_search_information,

            # notifications
            ActionIntentType.SEND_NOTIFICATION: self._execute_notification,
        }

    # =========================================================
    # EXECUTION ENTRYPOINT
    # =========================================================

    def execute(self, intent: ActionIntent) -> dict[str, Any]:

        logger.info(
            "Executing intent | type=%s description=%s",
            intent.intent_type.name,
            intent.description,
        )

        handler = self._handlers.get(intent.intent_type)

        if handler is None:
            raise UnsupportedActionIntentError(
                f"No executor for intent_type={intent.intent_type}"
            )

        try:
            result = handler(intent)

            if not isinstance(result, dict):
                raise RuntimeError("Intent handler must return dict")

            return result

        except Exception as exc:

            logger.exception(
                "Action execution failed | intent=%s",
                intent.intent_type.name,
            )

            return {
                "ok": False,
                "intent_type": intent.intent_type.name,
                "error": str(exc),
            }

    # =========================================================
    # CORE
    # =========================================================

    def _execute_no_op(self, intent: ActionIntent):

        return {"ok": True, "message": "No operation executed"}

    # =========================================================
    # AUDIO OUTPUT
    # =========================================================

    def _execute_speak_text(self, intent: ActionIntent):

        text = intent.payload.get("text", "")

        speech_service = build_speech_service()

        result = speech_service.speak_text(
            text=text,
            source="action_executor",
            blocking=False,
        )

        return {"ok": bool(result.ok)}

    def _execute_play_sound(self, intent: ActionIntent):

        sound = intent.payload.get("sound")

        logger.info("Playing sound: %s", sound)

        return {"ok": True}

    def _execute_play_music(self, intent: ActionIntent):

        track = intent.payload.get("track")

        logger.info("Playing music: %s", track)

        return {"ok": True}

    def _execute_stop_audio(self, intent: ActionIntent):

        logger.info("Stopping audio playback")

        return {"ok": True}

    # =========================================================
    # LISTENING
    # =========================================================

    def _execute_start_listening(self, intent: ActionIntent):

        logger.info("Starting microphone capture")

        return {"ok": True}

    def _execute_stop_listening(self, intent: ActionIntent):

        logger.info("Stopping microphone capture")

        return {"ok": True}

    # =========================================================
    # VISION
    # =========================================================

    def _execute_capture_image(self, intent: ActionIntent):

        logger.info("Capturing image")

        return {"ok": True}

    def _execute_capture_video(self, intent: ActionIntent):

        logger.info("Capturing video")

        return {"ok": True}

    # =========================================================
    # SCREEN
    # =========================================================

    def _execute_display_text(self, intent: ActionIntent):

        text = intent.payload.get("text")

        logger.info("Displaying text: %s", text)

        return {"ok": True}

    def _execute_display_image(self, intent: ActionIntent):

        image = intent.payload.get("image")

        logger.info("Displaying image: %s", image)

        return {"ok": True}

    def _execute_display_video(self, intent: ActionIntent):

        video = intent.payload.get("video")

        logger.info("Displaying video: %s", video)

        return {"ok": True}

    def _execute_display_emotion(self, intent: ActionIntent):

        emotion = intent.payload.get("emotion")

        logger.info("Displaying emotion: %s", emotion)

        return {"ok": True}

    def _execute_clear_screen(self, intent: ActionIntent):

        logger.info("Clearing screen")

        return {"ok": True}

    # =========================================================
    # LEDS
    # =========================================================

    def _execute_led_color(self, intent: ActionIntent):

        color = intent.payload.get("color")

        logger.info("Setting LED color: %s", color)

        return {"ok": True}

    def _execute_led_pattern(self, intent: ActionIntent):

        pattern = intent.payload.get("pattern")

        logger.info("LED pattern: %s", pattern)

        return {"ok": True}

    def _execute_led_blink(self, intent: ActionIntent):

        logger.info("LED blinking")

        return {"ok": True}

    # =========================================================
    # MOTION
    # =========================================================

    def _execute_move_head(self, intent: ActionIntent):

        yaw = intent.payload.get("yaw")
        pitch = intent.payload.get("pitch")

        logger.info("Moving head yaw=%s pitch=%s", yaw, pitch)

        return {"ok": True}

    def _execute_move_arm(self, intent: ActionIntent):

        position = intent.payload.get("position")

        logger.info("Moving arm: %s", position)

        return {"ok": True}

    def _execute_move_body(self, intent: ActionIntent):

        direction = intent.payload.get("direction")

        logger.info("Moving body: %s", direction)

        return {"ok": True}

    def _execute_look_at_target(self, intent: ActionIntent):

        target = intent.payload.get("target")

        logger.info("Looking at target: %s", target)

        return {"ok": True}

    # =========================================================
    # EMOTION
    # =========================================================

    def _execute_set_emotion(self, intent: ActionIntent):

        emotion = intent.payload.get("emotion")

        logger.info("Setting emotion: %s", emotion)

        return {"ok": True}

    # =========================================================
    # COGNITION
    # =========================================================

    def _execute_read_content(self, intent: ActionIntent):

        logger.info("Reading content")

        return {"ok": True}

    def _execute_search_information(self, intent: ActionIntent):

        query = intent.payload.get("query")

        logger.info("Searching information: %s", query)

        return {"ok": True}

    # =========================================================
    # NOTIFICATIONS
    # =========================================================

    def _execute_notification(self, intent: ActionIntent):

        message = intent.payload.get("message")

        logger.info("Sending notification: %s", message)

        return {"ok": True}