"""
Gesture detection module for the vision perception subsystem.

This module interprets pose estimation results and determines whether
a predefined gesture has been performed by the user.

The current implementation supports a basic activation gesture:
"right_hand_raised".
"""

from __future__ import annotations

from typing import Optional

from .config import GestureConfig
from .models import GestureDetectionResult, PoseResult


class GestureDetector:
    """
    Gesture interpretation component.

    This class receives pose estimation results and evaluates
    rule-based conditions to detect semantic gestures.

    Parameters
    ----------
    config : GestureConfig
        Configuration parameters controlling gesture recognition.
    """

    def __init__(self, config: GestureConfig) -> None:
        """
        Initialize the gesture detector.

        Parameters
        ----------
        config : GestureConfig
            Gesture detection configuration.
        """
        self._config = config

    def detect(self, pose_result: PoseResult) -> GestureDetectionResult:
        """
        Evaluate whether a configured gesture is present in the pose.

        Parameters
        ----------
        pose_result : PoseResult
            Pose estimation result.

        Returns
        -------
        GestureDetectionResult
            Result of the gesture detection stage.
        """
        if not pose_result.detected:
            return GestureDetectionResult(
                detected=False,
                reason="no_pose_detected",
            )

        if self._config.activation_gesture == "right_hand_raised":
            return self._detect_right_hand_raised(pose_result)

        return GestureDetectionResult(
            detected=False,
            reason="unknown_gesture",
        )

    def _detect_right_hand_raised(self, pose_result: PoseResult) -> GestureDetectionResult:
        """
        Detect the 'right_hand_raised' gesture.

        The gesture is considered valid if the right wrist is above
        the right shoulder by a configurable vertical margin.

        Parameters
        ----------
        pose_result : PoseResult
            Pose estimation result.

        Returns
        -------
        GestureDetectionResult
            Detection result.
        """
        right_wrist = pose_result.get_landmark("right_wrist")
        right_shoulder = pose_result.get_landmark("right_shoulder")

        if right_wrist is None or right_shoulder is None:
            return GestureDetectionResult(
                detected=False,
                reason="missing_landmarks",
            )

        vertical_margin = right_shoulder.y - right_wrist.y

        if vertical_margin > self._config.wrist_above_shoulder_threshold:
            return GestureDetectionResult(
                detected=True,
                gesture_name="right_hand_raised",
                confidence=vertical_margin,
                metadata={
                    "wrist_y": right_wrist.y,
                    "shoulder_y": right_shoulder.y,
                    "margin": vertical_margin,
                },
            )

        return GestureDetectionResult(
            detected=False,
            reason="gesture_condition_not_met",
            metadata={
                "wrist_y": right_wrist.y,
                "shoulder_y": right_shoulder.y,
                "margin": vertical_margin,
            },
        )