"""
Audio capture utilities for the NORA audio perception module.
"""

from __future__ import annotations

from typing import Optional

from .config import AudioCaptureConfig
from .models import AudioChunk

try:
    import pyaudio
except Exception:  # pragma: no cover
    pyaudio = None


class AudioCaptureError(RuntimeError):
    """
    Raised when the audio capture layer cannot operate correctly.
    """


class MicrophoneCapture:
    """
    Microphone audio capture wrapper.

    This class encapsulates access to a live microphone stream and exposes
    a minimal chunk-based API for the rest of the audio perception service.
    """

    def __init__(self, config: AudioCaptureConfig) -> None:
        """
        Initialize the microphone capture object.

        Args:
            config: Capture configuration.
        """
        self._config = config
        self._pa: Optional["pyaudio.PyAudio"] = None
        self._stream = None
        self._active = False

    @property
    def is_active(self) -> bool:
        """
        Return whether the capture stream is active.

        Returns:
            True if active, otherwise False.
        """
        return self._active

    def start(self) -> None:
        """
        Start microphone capture.

        Raises:
            AudioCaptureError: If PyAudio is unavailable or stream creation fails.
        """
        if self._active:
            return

        if pyaudio is None:
            raise AudioCaptureError(
                "PyAudio is not installed. Install it before using live microphone capture."
            )

        try:
            self._pa = pyaudio.PyAudio()
            self._stream = self._pa.open(
                format=pyaudio.paInt16,
                channels=self._config.channels,
                rate=self._config.sample_rate,
                input=True,
                input_device_index=self._config.input_device_index,
                frames_per_buffer=self._config.chunk_size,
            )
            self._active = True
        except Exception as exc:
            raise AudioCaptureError(f"Failed to start microphone capture: {exc}") from exc

    def read_chunk(self) -> AudioChunk:
        """
        Read the next chunk from the microphone stream.

        Returns:
            Captured audio chunk.

        Raises:
            AudioCaptureError: If the stream is not active or reading fails.
        """
        if not self._active or self._stream is None:
            raise AudioCaptureError("Microphone stream is not active.")

        try:
            raw = self._stream.read(self._config.chunk_size, exception_on_overflow=False)
        except Exception as exc:
            raise AudioCaptureError(f"Failed to read microphone chunk: {exc}") from exc

        return AudioChunk(
            data=raw,
            sample_rate=self._config.sample_rate,
            channels=self._config.channels,
        )

    def stop(self) -> None:
        """
        Stop microphone capture and release resources.
        """
        if self._stream is not None:
            try:
                self._stream.stop_stream()
                self._stream.close()
            except Exception:
                pass

        if self._pa is not None:
            try:
                self._pa.terminate()
            except Exception:
                pass

        self._stream = None
        self._pa = None
        self._active = False