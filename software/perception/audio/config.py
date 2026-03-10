"""
Configuration models for the NORA audio perception module.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(slots=True)
class AudioCaptureConfig:
    """
    Configuration for audio capture.

    Attributes:
        sample_rate: Sampling rate in Hz.
        channels: Number of audio channels.
        chunk_size: Number of samples per chunk.
        input_device_index: Optional input device index.
        format_name: Logical audio format name.
    """

    sample_rate: int = 16_000
    channels: int = 1
    chunk_size: int = 1280
    input_device_index: Optional[int] = None
    format_name: str = "int16"


from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class WakeWordConfig:
    """
    Configuration for wake word detection.

    Attributes:
        model_paths: Explicit list of wake word model file paths.
        threshold: Detection threshold.
        cooldown_seconds: Minimum time between accepted detections.
    """

    model_paths: List[str] = field(
        default_factory=lambda: [
            "C:/Users/amarq/OneDrive/Documentos/Contenido/Proyectos/Programación/NORA/software/perception/audio/models/hey_nora.onnx"
        ]
    )
    threshold: float = 0.5
    cooldown_seconds: float = 2.0


@dataclass(slots=True)
class AudioPublisherConfig:
    """
    Configuration for publishing events to the NORA backend.

    Attributes:
        backend_event_url: HTTP endpoint used to publish audio events.
        source_name: Logical source identifier for generated events.
        timeout_seconds: HTTP timeout in seconds.
        enabled: Whether publishing is enabled.
    """

    backend_event_url: str = "http://127.0.0.1:8000/events"
    source_name: str = "audio_perception"
    timeout_seconds: float = 5.0
    enabled: bool = False


@dataclass(slots=True)
class AudioServiceConfig:
    """
    Root configuration for the audio perception service.

    Attributes:
        capture: Audio capture configuration.
        wake_word: Wake word configuration.
        publisher: Event publisher configuration.
        debug: Whether debug mode is enabled.
    """

    capture: AudioCaptureConfig = field(default_factory=AudioCaptureConfig)
    wake_word: WakeWordConfig = field(default_factory=WakeWordConfig)
    publisher: AudioPublisherConfig = field(default_factory=AudioPublisherConfig)
    debug: bool = False