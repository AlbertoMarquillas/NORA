"""
Text-to-speech engine implementations for the speech action module.

This module is responsible for converting text into an audio artifact
stored on disk. It does not perform playback and does not publish events.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional
import time
import uuid

from .config import SpeechModuleConfig
from .models import SpeechRequest, SynthesizedAudio


class TTSEngineError(Exception):
    """
    Raised when the TTS engine cannot synthesize the requested text.
    """


class BaseTTSEngine(ABC):
    """
    Abstract base class for TTS engine implementations.
    """

    def __init__(self, config: SpeechModuleConfig) -> None:
        """
        Initialize the TTS engine.

        Args:
            config: Speech module configuration.
        """
        self.config = config

    @abstractmethod
    def synthesize(self, request: SpeechRequest) -> SynthesizedAudio:
        """
        Synthesize a speech request into an audio file.

        Args:
            request: Speech request to synthesize.

        Returns:
            Metadata about the generated audio artifact.

        Raises:
            TTSEngineError: If synthesis fails.
        """
        raise NotImplementedError


class Pyttsx3TTSEngine(BaseTTSEngine):
    """
    Offline TTS engine implementation based on pyttsx3.
    """

    def __init__(self, config: SpeechModuleConfig) -> None:
        """
        Initialize the pyttsx3 engine wrapper.

        Args:
            config: Speech module configuration.

        Raises:
            TTSEngineError: If pyttsx3 is not installed or initialization fails.
        """
        super().__init__(config)

        try:
            import pyttsx3  # type: ignore
        except ImportError as exc:
            raise TTSEngineError(
                "pyttsx3 is not installed. Install it before using the speech module."
            ) from exc

        self._pyttsx3 = pyttsx3

    def _build_output_path(self, request: SpeechRequest) -> Path:
        """
        Build the output path for the synthesized audio file.

        Args:
            request: Speech request being synthesized.

        Returns:
            Path where the generated audio will be stored.
        """
        timestamp_ms = int(time.time() * 1000)
        short_uid = uuid.uuid4().hex[:8]
        filename = f"speech_{timestamp_ms}_{short_uid}_{request.request_id}.{self.config.audio_format}"
        return self.config.storage_dir / filename

    def _apply_voice_settings(self, engine: object, request: SpeechRequest) -> None:
        """
        Apply voice-related settings to the pyttsx3 engine.

        Args:
            engine: pyttsx3 engine instance.
            request: Speech request with optional voice overrides.
        """
        voice_name = request.voice.voice_name or self.config.default_voice_name
        speaking_rate = request.voice.speaking_rate or self.config.default_speaking_rate
        volume = request.voice.volume

        try:
            engine.setProperty("rate", int(200 * speaking_rate))
        except Exception:
            pass

        try:
            engine.setProperty("volume", float(volume))
        except Exception:
            pass

        if voice_name:
            try:
                voices = engine.getProperty("voices")
                selected_voice_id: Optional[str] = None

                for voice in voices:
                    voice_id = getattr(voice, "id", "")
                    voice_label = getattr(voice, "name", "")
                    combined = f"{voice_id} {voice_label}".lower()
                    if voice_name.lower() in combined:
                        selected_voice_id = voice_id
                        break

                if selected_voice_id:
                    engine.setProperty("voice", selected_voice_id)
            except Exception:
                pass

    def synthesize(self, request: SpeechRequest) -> SynthesizedAudio:
        """
        Synthesize text into an audio file using pyttsx3.

        Args:
            request: Speech request to synthesize.

        Returns:
            Metadata describing the generated audio file.

        Raises:
            TTSEngineError: If synthesis fails.
        """
        request.validate()
        self.config.ensure_directories()

        output_path = self._build_output_path(request)

        try:
            engine = self._pyttsx3.init()
            self._apply_voice_settings(engine, request)

            engine.save_to_file(request.text, str(output_path))
            engine.runAndWait()
            engine.stop()
        except Exception as exc:
            raise TTSEngineError(
                f"pyttsx3 synthesis failed for request '{request.request_id}': {exc}"
            ) from exc

        if not output_path.exists():
            raise TTSEngineError(
                "Synthesis finished without generating the expected audio file."
            )

        return SynthesizedAudio(
            request_id=request.request_id,
            audio_path=str(output_path),
            duration_s=None,
            sample_rate_hz=None,
            channels=None,
            metadata={
                "tts_provider": "pyttsx3",
                "language": request.voice.language or self.config.default_language,
                "voice_name": request.voice.voice_name or self.config.default_voice_name,
            },
        )


def build_tts_engine(config: SpeechModuleConfig) -> BaseTTSEngine:
    """
    Factory function that builds the configured TTS engine.

    Args:
        config: Speech module configuration.

    Returns:
        Concrete TTS engine instance.

    Raises:
        TTSEngineError: If the configured provider is unsupported.
    """
    provider = config.tts_provider.strip().lower()

    if provider == "pyttsx3":
        return Pyttsx3TTSEngine(config)

    raise TTSEngineError(
        f"Unsupported TTS provider '{config.tts_provider}'."
    )