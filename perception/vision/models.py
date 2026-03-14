"""
Data models for the vision perception subsystem.

This module defines the typed structures exchanged between the
different stages of the vision pipeline, including frame capture,
pose estimation, gesture detection, and event publication.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class FrameData:
    """
    Container for a captured video frame.

    Attributes
    ----------
    frame_id : int
        Sequential identifier of the captured frame.

    image : Any
        Raw image object returned by OpenCV. In practice this is usually
        a NumPy ndarray, but it is typed as Any here to avoid forcing
        a hard dependency at the model layer.

    timestamp : float
        Unix timestamp associated with the capture time.

    width : int
        Frame width in pixels.

    height : int
        Frame height in pixels.
    """

    frame_id: int
    image: Any
    timestamp: float
    width: int
    height: int


@dataclass
class PoseLandmark:
    """
    Representation of a single pose landmark.

    Attributes
    ----------
    name : str
        Semantic landmark name, for example 'right_wrist' or 'left_shoulder'.

    x : float
        Horizontal normalized coordinate in the range [0, 1].

    y : float
        Vertical normalized coordinate in the range [0, 1].

    z : float
        Relative depth coordinate provided by the pose model.

    visibility : float
        Visibility or confidence score associated with the landmark.
    """

    name: str
    x: float
    y: float
    z: float
    visibility: float


@dataclass
class PoseResult:
    """
    Output of the pose estimation stage.

    Attributes
    ----------
    detected : bool
        Indicates whether a valid pose was detected in the frame.

    landmarks : List[PoseLandmark]
        List of detected landmarks.

    confidence : float
        Global confidence score for the pose estimation result.

    raw_output : Optional[Any]
        Original backend-specific pose output, stored optionally for
        debugging or advanced downstream use.
    """

    detected: bool
    landmarks: List[PoseLandmark] = field(default_factory=list)
    confidence: float = 0.0
    raw_output: Optional[Any] = None

    def get_landmark(self, name: str) -> Optional[PoseLandmark]:
        """
        Return a landmark by name.

        Parameters
        ----------
        name : str
            Landmark semantic name.

        Returns
        -------
        Optional[PoseLandmark]
            The matching landmark if found, otherwise None.
        """
        for landmark in self.landmarks:
            if landmark.name == name:
                return landmark
        return None


@dataclass
class GestureDetectionResult:
    """
    Output of the gesture interpretation stage.

    Attributes
    ----------
    detected : bool
        Indicates whether the configured gesture has been detected.

    gesture_name : Optional[str]
        Name of the detected gesture, if any.

    confidence : float
        Confidence or rule-based score associated with the detection.

    reason : Optional[str]
        Optional textual explanation useful for debugging.

    metadata : Dict[str, Any]
        Additional gesture-specific values, such as distances,
        thresholds, or intermediate rule evaluations.
    """

    detected: bool
    gesture_name: Optional[str] = None
    confidence: float = 0.0
    reason: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class VisionEvent:
    """
    Event produced by the vision subsystem and sent to the upper layer.

    Attributes
    ----------
    event_type : str
        Event semantic identifier.

    source : str
        Source module that produced the event.

    timestamp : float
        Unix timestamp associated with the event.

    payload : Dict[str, Any]
        Additional event information.
    """

    event_type: str
    source: str
    timestamp: float
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class VisionServiceState:
    """
    Runtime state of the vision service.

    Attributes
    ----------
    is_running : bool
        Indicates whether the service main loop is active.

    last_frame_id : int
        Identifier of the latest processed frame.

    consecutive_gesture_frames : int
        Number of consecutive frames in which the activation gesture
        has been considered valid.

    last_trigger_timestamp : Optional[float]
        Timestamp of the most recent accepted activation event.
    """

    is_running: bool = False
    last_frame_id: int = -1
    consecutive_gesture_frames: int = 0
    last_trigger_timestamp: Optional[float] = None