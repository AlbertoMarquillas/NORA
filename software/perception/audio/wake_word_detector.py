"""
Wake word detection wrapper for the NORA audio perception module.
"""

from __future__ import annotations

import time
from typing import Dict, Optional

import numpy as np

from .config import WakeWordConfig
from .models import AudioChunk, WakeWordDetectionResult

try:
    from openwakeword.model import Model
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "openwakeword is not available in the current environment."
    ) from exc


class WakeWordDetectorError(RuntimeError):
    """
    Raised when the wake word detector cannot be initialized or used.
    """


class OpenWakeWordDetector:
    """
    Wrapper around openWakeWord for NORA.

    This class isolates the third-party dependency so the rest of NORA does
    not depend directly on openWakeWord internals.
    """

    def __init__(self, config: WakeWordConfig) -> None:
        """
        Initialize the detector.

        Args:
            config: Wake word detector configuration.
        """
        self._config = config
        self._model: Optional[Model] = None
        self._last_detection_ts: float = 0.0

    def start(self) -> None:
        """
        Initialize the underlying wake word model.

        Raises:
            WakeWordDetectorError: If openWakeWord fails to initialize.
        """
        if self._model is not None:
            return

        try:
            if not self._config.model_paths:
                raise WakeWordDetectorError(
                    "No custom wake word model configured. "
                    "For NORA, configure the explicit path to the 'hey nora' model."
                )

            self._model = Model(wakeword_models=self._config.model_paths)
        except Exception as exc:
            raise WakeWordDetectorError(
                "Failed to initialize openWakeWord model. "
                f"Configured model_paths={self._config.model_paths}. "
                f"Original error: {exc}"
            ) from exc

    def stop(self) -> None:
        """
        Stop the detector and release local references.
        """
        self._model = None

    def process_chunk(self, chunk: AudioChunk) -> WakeWordDetectionResult:
        """
        Process one audio chunk and return a normalized detection result.

        Args:
            chunk: Audio chunk to process.

        Returns:
            Normalized wake word detection result.

        Raises:
            WakeWordDetectorError: If the detector is not initialized or processing fails.
        """
        if self._model is None:
            raise WakeWordDetectorError("Wake word detector is not initialized.")

        try:
            pcm_frame = np.frombuffer(chunk.data, dtype=np.int16)
            scores: Dict[str, float] = self._model.predict(pcm_frame)
        except Exception as exc:
            raise WakeWordDetectorError(f"Wake word inference failed: {exc}") from exc

        keyword, confidence = self._extract_best_detection(scores=scores)
        accepted = self._is_detection_accepted(keyword=keyword, confidence=confidence)

        if accepted:
            self._last_detection_ts = time.monotonic()
            return WakeWordDetectionResult(
                detected=True,
                keyword=keyword,
                confidence=confidence,
                metadata={"scores": scores},
            )

        return WakeWordDetectionResult(
            detected=False,
            keyword=keyword,
            confidence=confidence,
            metadata={"scores": scores},
        )

    def _extract_best_detection(
        self,
        scores: Dict[str, float],
    ) -> tuple[Optional[str], float]:
        """
        Extract the strongest score from model outputs.

        Args:
            scores: Raw model score dictionary.

        Returns:
            Tuple of best keyword and its confidence.
        """
        if not scores:
            return None, 0.0

        best_keyword = max(scores, key=scores.get)
        best_confidence = float(scores[best_keyword])
        return best_keyword, best_confidence

    def _is_detection_accepted(self, keyword: Optional[str], confidence: float) -> bool:
        """
        Decide whether a detection should be accepted.

        Args:
            keyword: Candidate detected keyword.
            confidence: Candidate confidence.

        Returns:
            True if detection is accepted, otherwise False.
        """
        if keyword is None:
            return False

        if confidence < self._config.threshold:
            return False

        elapsed = time.monotonic() - self._last_detection_ts
        if elapsed < self._config.cooldown_seconds:
            return False

        return True

    @staticmethod
    def supported_backend_name() -> str:
        """
        Return the logical name of the detector backend.

        Returns:
            Backend name.
        """
        return "openwakeword"