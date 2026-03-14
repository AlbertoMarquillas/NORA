"""
Configuration for the speech action module.

This module centralizes runtime parameters for text-to-speech synthesis,
audio storage, playback defaults, and event publishing integration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import os


@dataclass(slots=True)
class SpeechModuleConfig:
    """
    Configuration container for the speech action module.

    Attributes:
        enabled: Whether the speech module is enabled.
        tts_provider: Name of the TTS provider implementation to use.
        default_language: Default synthesis language.
        default_voice_name: Optional default voice identifier.
        default_speaking_rate: Default speech speed multiplier.
        default_volume: Default speech volume multiplier.
        default_pitch: Default pitch adjustment.
        audio_format: Output audio file format.
        storage_dir: Directory where generated audio files are stored.
        cleanup_after_playback: Whether generated files are deleted after playback.
        playback_blocking: Default playback blocking mode.
        playback_interrupt_current: Whether a new request interrupts current playback.
        playback_output_device: Optional output device name.
        publish_events: Whether the module publishes internal/external speech events.
        publisher_topic: Logical topic/channel used for command or event publication.
    """

    enabled: bool = True

    tts_provider: str = "pyttsx3"
    default_language: str = "es"
    default_voice_name: Optional[str] = None
    default_speaking_rate: float = 1.0
    default_volume: float = 1.0
    default_pitch: float = 0.0

    audio_format: str = "wav"
    storage_dir: Path = field(default_factory=lambda: Path("runtime/audio"))
    cleanup_after_playback: bool = False

    playback_blocking: bool = True
    playback_interrupt_current: bool = False
    playback_output_device: Optional[str] = None

    publish_events: bool = True
    publisher_topic: str = "action.speech"

    def ensure_directories(self) -> None:
        """
        Create required runtime directories if they do not exist.
        """
        self.storage_dir.mkdir(parents=True, exist_ok=True)


def _read_bool(value: str, default: bool) -> bool:
    """
    Parse a boolean environment variable value.

    Args:
        value: Raw environment variable value.
        default: Fallback value if the input is empty.

    Returns:
        Parsed boolean value.
    """
    if value is None:
        return default

    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    return default


def _read_float(value: str, default: float) -> float:
    """
    Parse a float environment variable value.

    Args:
        value: Raw environment variable value.
        default: Fallback value.

    Returns:
        Parsed float value or the default if parsing fails.
    """
    if value is None:
        return default

    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def load_speech_module_config() -> SpeechModuleConfig:
    """
    Load speech module configuration from environment variables.

    Environment variables:
        NORA_SPEECH_ENABLED
        NORA_SPEECH_TTS_PROVIDER
        NORA_SPEECH_DEFAULT_LANGUAGE
        NORA_SPEECH_DEFAULT_VOICE_NAME
        NORA_SPEECH_DEFAULT_SPEAKING_RATE
        NORA_SPEECH_DEFAULT_VOLUME
        NORA_SPEECH_DEFAULT_PITCH
        NORA_SPEECH_AUDIO_FORMAT
        NORA_SPEECH_STORAGE_DIR
        NORA_SPEECH_CLEANUP_AFTER_PLAYBACK
        NORA_SPEECH_PLAYBACK_BLOCKING
        NORA_SPEECH_PLAYBACK_INTERRUPT_CURRENT
        NORA_SPEECH_PLAYBACK_OUTPUT_DEVICE
        NORA_SPEECH_PUBLISH_EVENTS
        NORA_SPEECH_PUBLISHER_TOPIC

    Returns:
        Loaded speech module configuration.
    """
    config = SpeechModuleConfig(
        enabled=_read_bool(os.getenv("NORA_SPEECH_ENABLED"), True),
        tts_provider=os.getenv("NORA_SPEECH_TTS_PROVIDER", "pyttsx3"),
        default_language=os.getenv("NORA_SPEECH_DEFAULT_LANGUAGE", "es"),
        default_voice_name=os.getenv("NORA_SPEECH_DEFAULT_VOICE_NAME"),
        default_speaking_rate=_read_float(
            os.getenv("NORA_SPEECH_DEFAULT_SPEAKING_RATE"),
            1.0,
        ),
        default_volume=_read_float(
            os.getenv("NORA_SPEECH_DEFAULT_VOLUME"),
            1.0,
        ),
        default_pitch=_read_float(
            os.getenv("NORA_SPEECH_DEFAULT_PITCH"),
            0.0,
        ),
        audio_format=os.getenv("NORA_SPEECH_AUDIO_FORMAT", "wav"),
        storage_dir=Path(os.getenv("NORA_SPEECH_STORAGE_DIR", "runtime/audio")),
        cleanup_after_playback=_read_bool(
            os.getenv("NORA_SPEECH_CLEANUP_AFTER_PLAYBACK"),
            False,
        ),
        playback_blocking=_read_bool(
            os.getenv("NORA_SPEECH_PLAYBACK_BLOCKING"),
            True,
        ),
        playback_interrupt_current=_read_bool(
            os.getenv("NORA_SPEECH_PLAYBACK_INTERRUPT_CURRENT"),
            False,
        ),
        playback_output_device=os.getenv("NORA_SPEECH_PLAYBACK_OUTPUT_DEVICE"),
        publish_events=_read_bool(
            os.getenv("NORA_SPEECH_PUBLISH_EVENTS"),
            True,
        ),
        publisher_topic=os.getenv("NORA_SPEECH_PUBLISHER_TOPIC", "action.speech"),
    )

    config.ensure_directories()
    return config