"""
Audio playback implementations for the speech action module.

Windows-first implementation using the standard-library winsound module.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
import winsound

from .config import SpeechModuleConfig
from .models import SpeechRequest, SynthesizedAudio


class PlaybackError(Exception):
    """
    Raised when audio playback cannot be performed.
    """


class BaseAudioPlayer(ABC):
    """
    Abstract base class for audio playback implementations.
    """

    def __init__(self, config: SpeechModuleConfig) -> None:
        """
        Initialize the audio player.

        Args:
            config: Speech module configuration.
        """
        self.config = config

    @abstractmethod
    def play(self, audio: SynthesizedAudio, request: SpeechRequest) -> None:
        """
        Reproduce the provided audio artifact.

        Args:
            audio: Synthesized audio artifact.
            request: Original speech request associated with the audio.
        """
        raise NotImplementedError


class WinSoundAudioPlayer(BaseAudioPlayer):
    """
    Windows audio playback implementation using winsound.
    """

    def play(self, audio: SynthesizedAudio, request: SpeechRequest) -> None:
        """
        Reproduce the synthesized audio file.

        Args:
            audio: Synthesized audio artifact.
            request: Original speech request associated with the audio.

        Raises:
            PlaybackError: If the file does not exist or playback fails.
        """
        audio_path = Path(audio.audio_path)

        if not audio_path.exists():
            raise PlaybackError(f"Audio file does not exist: '{audio.audio_path}'.")

        flags = winsound.SND_FILENAME

        if not request.playback.blocking:
            flags |= winsound.SND_ASYNC

        try:
            winsound.PlaySound(str(audio_path), flags)
        except Exception as exc:
            raise PlaybackError(f"winsound playback failed: {exc}") from exc


def build_audio_player(config: SpeechModuleConfig) -> BaseAudioPlayer:
    """
    Factory function that builds the configured audio player.

    Args:
        config: Speech module configuration.

    Returns:
        Concrete audio player instance.
    """
    return WinSoundAudioPlayer(config)