"""
Event publishing utilities for the NORA audio perception module.
"""

from __future__ import annotations

from typing import Optional

from .config import AudioPublisherConfig
from .models import NoraAudioEvent, WakeWordDetectionResult

try:
    import requests
except Exception:  # pragma: no cover
    requests = None


class AudioEventPublisher:
    """
    Publisher that converts audio detections into NORA events.
    """

    def __init__(self, config: AudioPublisherConfig) -> None:
        """
        Initialize the publisher.

        Args:
            config: Publisher configuration.
        """
        self._config = config

    def build_wake_word_event(
        self,
        detection: WakeWordDetectionResult,
    ) -> NoraAudioEvent:
        """
        Build a normalized wake word event.

        Args:
            detection: Accepted detection result.

        Returns:
            Normalized NORA event.
        """
        return NoraAudioEvent(
            event_type="wake_word_detected",
            source=self._config.source_name,
            payload={
                "keyword": detection.keyword,
                "confidence": detection.confidence,
                "metadata": detection.metadata,
            },
        )

    def publish(self, event: NoraAudioEvent) -> bool:
        """
        Publish an event to the configured backend endpoint.

        Args:
            event: Event to publish.

        Returns:
            True if publishing succeeded or publishing is disabled, otherwise False.
        """
        if not self._config.enabled:
            return True

        if requests is None:
            return False

        try:
            response = requests.post(
                self._config.backend_event_url,
                json=event.to_dict(),
                timeout=self._config.timeout_seconds,
            )
            return 200 <= response.status_code < 300
        except Exception:
            return False