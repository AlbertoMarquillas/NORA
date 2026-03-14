"""
Cooldown control module for the vision perception subsystem.

This component prevents repeated activation events when the same
gesture is detected across multiple consecutive frames.

The mechanism combines two protections:
1. Frame persistence requirement
2. Temporal cooldown between activations
"""

from __future__ import annotations

import time

from .config import CooldownConfig, GestureConfig
from .models import GestureDetectionResult, VisionServiceState


class CooldownController:
    """
    Controller that stabilizes gesture activation.

    This class ensures that gestures must persist across several frames
    before triggering an activation and prevents repeated triggers
    within a configurable cooldown interval.

    Parameters
    ----------
    gesture_config : GestureConfig
        Configuration controlling gesture persistence.

    cooldown_config : CooldownConfig
        Configuration controlling cooldown timing.
    """

    def __init__(
        self,
        gesture_config: GestureConfig,
        cooldown_config: CooldownConfig,
    ) -> None:
        """
        Initialize the cooldown controller.

        Parameters
        ----------
        gesture_config : GestureConfig
            Gesture detection configuration.

        cooldown_config : CooldownConfig
            Cooldown timing configuration.
        """
        self._gesture_config = gesture_config
        self._cooldown_config = cooldown_config

    def should_trigger(
        self,
        gesture_result: GestureDetectionResult,
        state: VisionServiceState,
    ) -> bool:
        """
        Evaluate whether a gesture detection should produce an activation event.

        Parameters
        ----------
        gesture_result : GestureDetectionResult
            Result of the gesture detection stage.

        state : VisionServiceState
            Current runtime state of the vision service.

        Returns
        -------
        bool
            True if an activation event should be emitted.
        """
        if not gesture_result.detected:
            state.consecutive_gesture_frames = 0
            return False

        state.consecutive_gesture_frames += 1

        if state.consecutive_gesture_frames < self._gesture_config.frames_required:
            return False

        current_time = time.time()

        if state.last_trigger_timestamp is not None:
            elapsed = current_time - state.last_trigger_timestamp

            if elapsed < self._cooldown_config.cooldown_seconds:
                return False

        state.last_trigger_timestamp = current_time
        state.consecutive_gesture_frames = 0

        return True