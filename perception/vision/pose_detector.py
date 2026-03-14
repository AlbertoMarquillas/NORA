"""
Pose detection module for the vision perception subsystem.

This module provides a wrapper around an Ultralytics YOLO pose model
and converts its output into the internal PoseResult structure used
by the rest of the vision pipeline.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from ultralytics import YOLO

from .config import PoseModelConfig
from .models import FrameData, PoseLandmark, PoseResult


YOLO_POSE_KEYPOINT_NAME_MAP: Dict[int, str] = {
    0: "nose",
    1: "left_eye",
    2: "right_eye",
    3: "left_ear",
    4: "right_ear",
    5: "left_shoulder",
    6: "right_shoulder",
    7: "left_elbow",
    8: "right_elbow",
    9: "left_wrist",
    10: "right_wrist",
    11: "left_hip",
    12: "right_hip",
    13: "left_knee",
    14: "right_knee",
    15: "left_ankle",
    16: "right_ankle",
}


class PoseDetector:
    """
    Human pose estimation interface based on Ultralytics YOLO pose.

    This class receives captured frames, runs pose inference,
    and converts the backend-specific result into the internal
    typed data model.

    Parameters
    ----------
    config : PoseModelConfig
        Configuration parameters for the pose estimation model.
    """

    def __init__(self, config: PoseModelConfig) -> None:
        """
        Initialize the pose detector.

        Parameters
        ----------
        config : PoseModelConfig
            Pose model configuration.
        """
        self._config = config
        self._model = YOLO(self._config.model_path)

    def detect(self, frame_data: FrameData) -> PoseResult:
        """
        Run pose estimation on a captured frame.

        Parameters
        ----------
        frame_data : FrameData
            Captured frame information.

        Returns
        -------
        PoseResult
            Structured pose estimation result.
        """
        results = self._model.predict(
            source=frame_data.image,
            conf=self._config.conf_threshold,
            imgsz=self._config.imgsz,
            device=self._config.device,
            verbose=self._config.verbose,
        )

        if not results:
            return PoseResult(
                detected=False,
                landmarks=[],
                confidence=0.0,
                raw_output=None,
            )

        result = results[0]

        if result.keypoints is None:
            return PoseResult(
                detected=False,
                landmarks=[],
                confidence=0.0,
                raw_output=result,
            )

        person_index = self._select_primary_person_index(result)

        if person_index is None:
            return PoseResult(
                detected=False,
                landmarks=[],
                confidence=0.0,
                raw_output=result,
            )

        landmarks = self._convert_landmarks(result, person_index)
        confidence = self._estimate_global_confidence(landmarks)

        return PoseResult(
            detected=bool(landmarks),
            landmarks=landmarks,
            confidence=confidence,
            raw_output=result,
        )

    def close(self) -> None:
        """
        Release backend resources associated with the pose model.

        Ultralytics does not require an explicit close operation in the
        same way as MediaPipe, so this method currently exists only to
        preserve a stable interface for the rest of the service.
        """
        return None

    def _select_primary_person_index(self, result: object) -> Optional[int]:
        """
        Select the primary detected person from the inference result.

        The current policy is to choose the detection with the largest
        bounding-box area.

        Parameters
        ----------
        result : object
            Ultralytics result object.

        Returns
        -------
        Optional[int]
            Index of the selected person, or None if no valid person
            detection is available.
        """
        boxes = getattr(result, "boxes", None)

        if boxes is None or boxes.xyxy is None:
            keypoints = getattr(result, "keypoints", None)
            if keypoints is None or keypoints.xy is None or len(keypoints.xy) == 0:
                return None
            return 0

        xyxy = boxes.xyxy.cpu().numpy()

        if len(xyxy) == 0:
            return None

        best_index: Optional[int] = None
        best_area: float = -1.0

        for index, box in enumerate(xyxy):
            x1, y1, x2, y2 = box[:4]
            area = max(0.0, float(x2 - x1)) * max(0.0, float(y2 - y1))

            if area > best_area:
                best_area = area
                best_index = index

        return best_index

    def _convert_landmarks(self, result: object, person_index: int) -> List[PoseLandmark]:
        """
        Convert Ultralytics keypoints into the internal PoseLandmark format.

        Parameters
        ----------
        result : object
            Ultralytics result object.

        person_index : int
            Index of the selected person.

        Returns
        -------
        List[PoseLandmark]
            Converted landmark list.
        """
        keypoints = result.keypoints

        xyn = keypoints.xyn.cpu().numpy()
        conf = keypoints.conf

        conf_array = None
        if conf is not None:
            conf_array = conf.cpu().numpy()

        person_xyn = xyn[person_index]

        person_conf = None
        if conf_array is not None and len(conf_array) > person_index:
            person_conf = conf_array[person_index]

        converted_landmarks: List[PoseLandmark] = []

        for index, coords in enumerate(person_xyn):
            landmark_name = YOLO_POSE_KEYPOINT_NAME_MAP.get(index, f"landmark_{index}")
            x = float(coords[0])
            y = float(coords[1])

            visibility = 1.0
            if person_conf is not None and len(person_conf) > index:
                visibility = float(person_conf[index])

            converted_landmarks.append(
                PoseLandmark(
                    name=landmark_name,
                    x=x,
                    y=y,
                    z=0.0,
                    visibility=visibility,
                )
            )

        return converted_landmarks

    def _estimate_global_confidence(self, landmarks: List[PoseLandmark]) -> float:
        """
        Estimate a global confidence score for the detected pose.

        The current implementation uses the mean visibility of all landmarks.

        Parameters
        ----------
        landmarks : List[PoseLandmark]
            Converted landmark list.

        Returns
        -------
        float
            Estimated global confidence score.
        """
        if not landmarks:
            return 0.0

        visibility_sum = sum(landmark.visibility for landmark in landmarks)
        return visibility_sum / len(landmarks)