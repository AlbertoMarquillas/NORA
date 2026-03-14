"""
Application service for the speech action module.

This module orchestrates the full speech execution flow:
request validation, synthesis, playback, event publishing,
optional cleanup, and final result creation.
"""

from __future__ import annotations

from pathlib import Path
import logging
import os
import time
from typing import Optional

from .command_publisher import (
    BaseCommandPublisher,
    CommandPublisherError,
    build_command_publisher,
)
from .config import SpeechModuleConfig, load_speech_module_config
from .models import (
    PlaybackConfig,
    SpeechPriority,
    SpeechRequest,
    SpeechResult,
    SpeechStatus,
    VoiceConfig,
)
from .playback import BaseAudioPlayer, PlaybackError, build_audio_player
from .tts_engine import BaseTTSEngine, TTSEngineError, build_tts_engine


LOGGER = logging.getLogger(__name__)


class SpeechServiceError(Exception):
    """
    Raised when the speech service cannot complete its execution flow.
    """


class SpeechService:
    """
    High-level application service for speech execution.

    This service coordinates the TTS engine, the audio player,
    and the command publisher while exposing a simple interface
    to the rest of the system.
    """

    def __init__(
        self,
        config: SpeechModuleConfig,
        tts_engine: BaseTTSEngine,
        audio_player: BaseAudioPlayer,
        command_publisher: BaseCommandPublisher,
    ) -> None:
        """
        Initialize the speech service.

        Args:
            config: Speech module configuration.
            tts_engine: Concrete text-to-speech engine.
            audio_player: Concrete audio playback implementation.
            command_publisher: Concrete lifecycle event publisher.
        """
        self.config = config
        self.tts_engine = tts_engine
        self.audio_player = audio_player
        self.command_publisher = command_publisher

    def _publish_status_safe(
        self,
        request: SpeechRequest,
        status: SpeechStatus,
        detail: Optional[str] = None,
        payload: Optional[dict] = None,
    ) -> None:
        """
        Publish a status event without breaking the main speech flow.

        Args:
            request: Speech request being processed.
            status: Lifecycle status to publish.
            detail: Optional human-readable detail.
            payload: Optional machine-readable payload.
        """
        try:
            self.command_publisher.publish_status(
                request=request,
                status=status,
                detail=detail,
                payload=payload,
            )
        except CommandPublisherError as exc:
            LOGGER.warning("Speech status publish failed: %s", exc)

    def _publish_result_safe(
        self,
        request: SpeechRequest,
        result: SpeechResult,
    ) -> None:
        """
        Publish a final result event without breaking the main speech flow.

        Args:
            request: Original speech request.
            result: Final speech result.
        """
        try:
            self.command_publisher.publish_result(request=request, result=result)
        except CommandPublisherError as exc:
            LOGGER.warning("Speech result publish failed: %s", exc)

    def _cleanup_audio_file(self, audio_path: Optional[str]) -> None:
        """
        Remove a generated audio file if cleanup is enabled.

        Args:
            audio_path: Path to the generated audio file.
        """
        if not self.config.cleanup_after_playback:
            return

        if not audio_path:
            return

        try:
            path = Path(audio_path)
            if path.exists():
                path.unlink()
        except OSError as exc:
            LOGGER.warning("Audio cleanup failed for '%s': %s", audio_path, exc)

    def speak(self, request: SpeechRequest) -> SpeechResult:
        """
        Execute the full speech flow for a prepared speech request.

        Args:
            request: Fully built speech request.

        Returns:
            Final speech execution result.
        """
        started_at = time.time()
        audio_path: Optional[str] = None

        if not self.config.enabled:
            result = SpeechResult(
                request_id=request.request_id,
                status=SpeechStatus.FAILED,
                audio_path=None,
                message="Speech module is disabled.",
                error="Speech module is disabled.",
                started_at=started_at,
                finished_at=time.time(),
                metadata={"enabled": False},
            )
            self._publish_result_safe(request, result)
            return result

        try:
            request.validate()

            self._publish_status_safe(
                request=request,
                status=SpeechStatus.PENDING,
                detail="Speech request accepted.",
            )

            self._publish_status_safe(
                request=request,
                status=SpeechStatus.SYNTHESIZING,
                detail="Speech synthesis started.",
            )

            synthesized_audio = self.tts_engine.synthesize(request)
            audio_path = synthesized_audio.audio_path

            self._publish_status_safe(
                request=request,
                status=SpeechStatus.READY,
                detail="Speech synthesis completed.",
                payload={"audio_path": audio_path},
            )

            self._publish_status_safe(
                request=request,
                status=SpeechStatus.PLAYING,
                detail="Audio playback started.",
                payload={"audio_path": audio_path},
            )

            self.audio_player.play(synthesized_audio, request)

            finished_at = time.time()
            result = SpeechResult(
                request_id=request.request_id,
                status=SpeechStatus.COMPLETED,
                audio_path=audio_path,
                message="Speech action completed successfully.",
                error=None,
                started_at=started_at,
                finished_at=finished_at,
                metadata={
                    "tts_provider": self.config.tts_provider,
                    "audio_format": self.config.audio_format,
                    "cleanup_after_playback": self.config.cleanup_after_playback,
                },
            )

            self._publish_result_safe(request, result)
            self._cleanup_audio_file(audio_path)
            return result

        except ValueError as exc:
            finished_at = time.time()
            result = SpeechResult(
                request_id=request.request_id,
                status=SpeechStatus.FAILED,
                audio_path=audio_path,
                message="Invalid speech request.",
                error=str(exc),
                started_at=started_at,
                finished_at=finished_at,
                metadata={"error_type": "validation_error"},
            )
            self._publish_result_safe(request, result)
            self._cleanup_audio_file(audio_path)
            return result

        except TTSEngineError as exc:
            finished_at = time.time()
            result = SpeechResult(
                request_id=request.request_id,
                status=SpeechStatus.FAILED,
                audio_path=audio_path,
                message="Speech synthesis failed.",
                error=str(exc),
                started_at=started_at,
                finished_at=finished_at,
                metadata={"error_type": "tts_error"},
            )
            self._publish_result_safe(request, result)
            self._cleanup_audio_file(audio_path)
            return result

        except PlaybackError as exc:
            finished_at = time.time()
            result = SpeechResult(
                request_id=request.request_id,
                status=SpeechStatus.FAILED,
                audio_path=audio_path,
                message="Audio playback failed.",
                error=str(exc),
                started_at=started_at,
                finished_at=finished_at,
                metadata={"error_type": "playback_error"},
            )
            self._publish_result_safe(request, result)
            self._cleanup_audio_file(audio_path)
            return result

        except Exception as exc:
            finished_at = time.time()
            result = SpeechResult(
                request_id=request.request_id,
                status=SpeechStatus.FAILED,
                audio_path=audio_path,
                message="Unexpected speech service failure.",
                error=str(exc),
                started_at=started_at,
                finished_at=finished_at,
                metadata={"error_type": "unexpected_error"},
            )
            self._publish_result_safe(request, result)
            self._cleanup_audio_file(audio_path)
            return result

    def speak_text(
        self,
        text: str,
        source: str = "system",
        correlation_id: Optional[str] = None,
        priority: SpeechPriority = SpeechPriority.NORMAL,
        language: Optional[str] = None,
        voice_name: Optional[str] = None,
        speaking_rate: Optional[float] = None,
        volume: Optional[float] = None,
        pitch: Optional[float] = None,
        blocking: Optional[bool] = None,
        interrupt_current: Optional[bool] = None,
        metadata: Optional[dict] = None,
    ) -> SpeechResult:
        """
        Build a speech request from primitive parameters and execute it.

        Args:
            text: Text to be synthesized and reproduced.
            source: Origin module or subsystem.
            correlation_id: Optional correlation identifier.
            priority: Speech request priority.
            language: Optional voice language override.
            voice_name: Optional voice identifier override.
            speaking_rate: Optional speaking rate override.
            volume: Optional volume override.
            pitch: Optional pitch override.
            blocking: Optional playback blocking override.
            interrupt_current: Optional playback interruption override.
            metadata: Optional request metadata.

        Returns:
            Final speech execution result.
        """
        print("[SPEECH SERVICE] Speaking text...")
        request = SpeechRequest(
            text=text,
            source=source,
            correlation_id=correlation_id,
            priority=priority,
            voice=VoiceConfig(
                language=language or self.config.default_language,
                voice_name=voice_name or self.config.default_voice_name,
                speaking_rate=speaking_rate
                if speaking_rate is not None
                else self.config.default_speaking_rate,
                volume=volume if volume is not None else self.config.default_volume,
                pitch=pitch if pitch is not None else self.config.default_pitch,
            ),
            playback=PlaybackConfig(
                blocking=blocking
                if blocking is not None
                else self.config.playback_blocking,
                interrupt_current=interrupt_current
                if interrupt_current is not None
                else self.config.playback_interrupt_current,
                output_device=self.config.playback_output_device,
            ),
            metadata=metadata or {},
        )
        print("[SPEECH SERVICE] Speaking request...")
        return self.speak(request)


def build_speech_service(
    config: Optional[SpeechModuleConfig] = None,
) -> SpeechService:
    """
    Build a fully wired speech service using the configured components.

    Args:
        config: Optional externally provided module configuration.

    Returns:
        Fully initialized speech service.
    """
    print("[SPEECH SERVICE] Building speech service...")
    resolved_config = config or load_speech_module_config()

    print("[SPEECH SERVICE] Building TTS engine...")
    tts_engine = build_tts_engine(resolved_config)

    print("[SPEECH SERVICE] Building audio player...")
    audio_player = build_audio_player(resolved_config)

    print("[SPEECH SERVICE] Building command publisher...")
    command_publisher = build_command_publisher(resolved_config)

    return SpeechService(
        config=resolved_config,
        tts_engine=tts_engine,
        audio_player=audio_player,
        command_publisher=command_publisher,
    )