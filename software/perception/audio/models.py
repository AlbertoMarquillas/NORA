"""
Domain models for the NORA audio perception module.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Optional


def utc_now() -> datetime:
    """
    Return the current UTC datetime.

    Returns:
        Current UTC-aware datetime.
    """
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class AudioChunk:
    """
    Audio chunk captured from an input source.

    Attributes:
        data: Raw PCM bytes.
        sample_rate: Sampling rate in Hz.
        channels: Number of channels.
        timestamp: Capture timestamp.
    """

    data: bytes
    sample_rate: int
    channels: int
    timestamp: datetime = field(default_factory=utc_now)


@dataclass(slots=True)
class WakeWordDetectionResult:
    """
    Result of a wake word detection pass.

    Attributes:
        detected: Whether a wake word has been detected.
        keyword: Detected keyword, if any.
        confidence: Detection confidence or score.
        timestamp: Detection timestamp.
        metadata: Additional backend-specific information.
    """

    detected: bool
    keyword: Optional[str]
    confidence: float
    timestamp: datetime = field(default_factory=utc_now)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class NoraAudioEvent:
    """
    Normalized audio event emitted toward NORA.

    Attributes:
        event_type: Logical event type.
        source: Event source identifier.
        timestamp: Event timestamp.
        payload: Event payload.
    """

    event_type: str
    source: str
    timestamp: datetime = field(default_factory=utc_now)
    payload: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the event into a JSON-serializable dictionary.

        Returns:
            Dictionary representation of the event.
        """
        return {
            "event_type": self.event_type,
            "source": self.source,
            "timestamp": self.timestamp.isoformat(),
            "payload": self.payload,
        }


@dataclass(slots=True)
class AudioServiceStatus:
    """
    Runtime status of the audio service.

    Attributes:
        running: Whether the service is currently running.
        microphone_active: Whether microphone capture is active.
        last_detection: Last accepted detection result, if any.
        processed_chunks: Total processed chunks.
    """

    running: bool
    microphone_active: bool
    last_detection: Optional[WakeWordDetectionResult] = None
    processed_chunks: int = 0