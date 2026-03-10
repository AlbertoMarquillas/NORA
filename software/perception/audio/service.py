"""
Main orchestration service for the NORA audio perception module.
"""

from __future__ import annotations

import threading
from typing import Optional

from .capture import MicrophoneCapture
from .config import AudioServiceConfig
from .event_publisher import AudioEventPublisher
from .models import AudioServiceStatus, WakeWordDetectionResult
from .wake_word_detector import OpenWakeWordDetector


class AudioService:
    """
    Main runtime service for NORA audio perception v1.

    Responsibilities:
        - start and stop microphone capture
        - run wake word inference on live chunks
        - publish accepted detections as normalized events
        - expose a simple runtime status API
    """

    def __init__(self, config: AudioServiceConfig) -> None:
        """
        Initialize the audio service.

        Args:
            config: Root service configuration.
        """
        self._config = config
        self._capture = MicrophoneCapture(config.capture)
        self._detector = OpenWakeWordDetector(config.wake_word)
        self._publisher = AudioEventPublisher(config.publisher)

        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._processed_chunks = 0
        self._last_detection: Optional[WakeWordDetectionResult] = None

    def start(self) -> None:
        """
        Start the audio perception service.
        """
        if self._running:
            return

        self._detector.start()
        self._capture.start()

        self._running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """
        Stop the audio perception service.
        """
        self._running = False

        if self._thread is not None:
            self._thread.join(timeout=2.0)
            self._thread = None

        self._capture.stop()
        self._detector.stop()

    def get_status(self) -> AudioServiceStatus:
        """
        Return the current runtime status of the service.

        Returns:
            Current service status.
        """
        return AudioServiceStatus(
            running=self._running,
            microphone_active=self._capture.is_active,
            last_detection=self._last_detection,
            processed_chunks=self._processed_chunks,
        )

    def _run_loop(self) -> None:
        """
        Execute the main audio processing loop.
        """
        while self._running:
            chunk = self._capture.read_chunk()
            self._processed_chunks += 1

            detection = self._detector.process_chunk(chunk)

            if self._config.debug:
                keyword = detection.keyword if detection.keyword is not None else "None"
                print(
                    f"[AUDIO DEBUG] chunk={self._processed_chunks} | "
                    f"keyword={keyword} | "
                    f"confidence={detection.confidence:.4f} | "
                    f"detected={detection.detected}"
                )

            if not detection.detected:
                continue

            self._last_detection = detection
            event = self._publisher.build_wake_word_event(detection)

            if self._config.debug:
                print(
                    f"[AUDIO EVENT] wake_word_detected | "
                    f"keyword={detection.keyword} | "
                    f"confidence={detection.confidence:.4f}"
                )

            self._publisher.publish(event)