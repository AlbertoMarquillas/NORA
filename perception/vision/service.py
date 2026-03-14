"""
Vision perception service.

This module orchestrates the complete vision pipeline:
camera capture, pose detection, gesture recognition,
cooldown control, debug visualization and event publishing.
"""

from __future__ import annotations

import cv2

from .capture import CameraCapture
from .config import VisionConfig
from .cooldown import CooldownController
from .event_publisher import EventPublisher
from .gesture_detector import GestureDetector
from .models import PoseResult, VisionServiceState
from .pose_detector import PoseDetector


class VisionService:
    """
    Main service responsible for running the vision perception pipeline.

    The service continuously captures frames from the camera,
    performs pose estimation, evaluates gestures, renders a debug
    visualization window and publishes activation events when appropriate.
    """

    def __init__(self, config: VisionConfig, backend_endpoint: str) -> None:
        """
        Initialize the vision service.

        Parameters
        ----------
        config : VisionConfig
            Vision subsystem configuration.

        backend_endpoint : str
            Backend endpoint used to publish events.
        """
        self._config = config

        self._capture = CameraCapture(config.camera)
        self._pose_detector = PoseDetector(config.pose)
        self._gesture_detector = GestureDetector(config.gesture)
        self._cooldown = CooldownController(config.gesture, config.cooldown)
        self._publisher = EventPublisher(backend_endpoint)

        self._state = VisionServiceState()
        self._window_name = "NORA Vision Service"

    def start(self) -> None:
        """
        Start the vision service main loop.

        This method opens the camera, processes frames continuously,
        shows a debug preview window and publishes events whenever the
        configured activation gesture is validated.
        """
        self._capture.start()
        self._state.is_running = True

        print("[VISION] Vision service started")
        print("[VISION] Press 'q' to exit")

        try:
            while self._state.is_running:
                frame_data = self._capture.read()

                if frame_data is None:
                    continue

                self._state.last_frame_id = frame_data.frame_id

                pose_result = self._pose_detector.detect(frame_data)
                gesture_result = self._gesture_detector.detect(pose_result)

                should_trigger = self._cooldown.should_trigger(
                    gesture_result=gesture_result,
                    state=self._state,
                )

                if should_trigger:
                    event = self._publisher.build_event(
                        gesture_name=gesture_result.gesture_name or "unknown",
                        confidence=gesture_result.confidence,
                        metadata=gesture_result.metadata,
                    )

                    self._publisher.publish(event)
                    print(
                        "[VISION] Activation gesture detected "
                        f"({gesture_result.gesture_name})"
                    )

                debug_frame = frame_data.image.copy()
                self._draw_pose_landmarks(debug_frame, pose_result)
                self._draw_status_overlay(
                    frame=debug_frame,
                    pose_result=pose_result,
                    gesture_detected=gesture_result.detected,
                    gesture_name=gesture_result.gesture_name,
                    gesture_confidence=gesture_result.confidence,
                    consecutive_frames=self._state.consecutive_gesture_frames,
                )

                cv2.imshow(self._window_name, debug_frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    print("[VISION] Exit requested by user")
                    break

        except KeyboardInterrupt:
            print("[VISION] Service interrupted by user")

        finally:
            self.stop()

    def stop(self) -> None:
        """
        Stop the vision service and release all resources.
        """
        self._state.is_running = False

        self._capture.stop()
        self._pose_detector.close()
        cv2.destroyAllWindows()

        print("[VISION] Vision service stopped")

    def _draw_pose_landmarks(self, frame: object, pose_result: PoseResult) -> None:
        """
        Draw the detected pose landmarks on the frame.

        Parameters
        ----------
        frame : object
            OpenCV image frame where landmarks will be drawn.

        pose_result : PoseResult
            Pose detection result containing normalized landmarks.
        """
        if not pose_result.detected:
            return

        frame_height, frame_width = frame.shape[:2]

        for landmark in pose_result.landmarks:
            x_px = int(landmark.x * frame_width)
            y_px = int(landmark.y * frame_height)

            cv2.circle(frame, (x_px, y_px), 5, (0, 255, 0), -1)

        self._draw_pose_connections(frame, pose_result)

    def _draw_pose_connections(self, frame: object, pose_result: PoseResult) -> None:
        """
        Draw a minimal skeleton using the available landmarks.

        Parameters
        ----------
        frame : object
            OpenCV image frame where connections will be drawn.

        pose_result : PoseResult
            Pose detection result containing normalized landmarks.
        """
        frame_height, frame_width = frame.shape[:2]

        connection_pairs = [
            ("left_shoulder", "right_shoulder"),
            ("left_shoulder", "left_elbow"),
            ("left_elbow", "left_wrist"),
            ("right_shoulder", "right_elbow"),
            ("right_elbow", "right_wrist"),
            ("left_shoulder", "left_hip"),
            ("right_shoulder", "right_hip"),
            ("left_hip", "right_hip"),
            ("left_hip", "left_knee"),
            ("left_knee", "left_ankle"),
            ("right_hip", "right_knee"),
            ("right_knee", "right_ankle"),
        ]

        for start_name, end_name in connection_pairs:
            start_landmark = pose_result.get_landmark(start_name)
            end_landmark = pose_result.get_landmark(end_name)

            if start_landmark is None or end_landmark is None:
                continue

            start_point = (
                int(start_landmark.x * frame_width),
                int(start_landmark.y * frame_height),
            )
            end_point = (
                int(end_landmark.x * frame_width),
                int(end_landmark.y * frame_height),
            )

            cv2.line(frame, start_point, end_point, (255, 0, 0), 2)

    def _draw_status_overlay(
        self,
        frame: object,
        pose_result: PoseResult,
        gesture_detected: bool,
        gesture_name: str | None,
        gesture_confidence: float,
        consecutive_frames: int,
    ) -> None:
        """
        Draw textual status information on the debug frame.

        Parameters
        ----------
        frame : object
            OpenCV image frame where the text overlay will be drawn.

        pose_result : PoseResult
            Pose detection result.

        gesture_detected : bool
            Indicates whether the activation gesture is currently detected.

        gesture_name : str | None
            Name of the detected gesture, if any.

        gesture_confidence : float
            Confidence or score associated with the gesture.

        consecutive_frames : int
            Number of consecutive frames in which the gesture has been detected.
        """
        pose_text = (
            f"Pose detected: YES ({pose_result.confidence:.2f})"
            if pose_result.detected
            else "Pose detected: NO"
        )

        gesture_text = (
            f"Gesture: YES ({gesture_name}, {gesture_confidence:.3f})"
            if gesture_detected
            else "Gesture: NO"
        )

        persistence_text = (
            "Gesture persistence: "
            f"{consecutive_frames}/{self._config.gesture.frames_required}"
        )

        exit_text = "Press 'q' to quit"

        cv2.putText(
            frame,
            pose_text,
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        cv2.putText(
            frame,
            gesture_text,
            (20, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0) if gesture_detected else (0, 0, 255),
            2,
            cv2.LINE_AA,
        )

        cv2.putText(
            frame,
            persistence_text,
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
            cv2.LINE_AA,
        )

        cv2.putText(
            frame,
            exit_text,
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (200, 200, 200),
            2,
            cv2.LINE_AA,
        )