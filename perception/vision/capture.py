"""
Camera capture module for the vision perception subsystem.

This module provides an abstraction layer over the camera device
using OpenCV. Its responsibility is limited to acquiring frames
from the camera and packaging them into FrameData objects used
by the rest of the vision pipeline.

No pose estimation or gesture logic should appear in this module.
"""

from __future__ import annotations

import time
from typing import Optional

import cv2

from .config import CameraConfig
from .models import FrameData


class CameraCapture:
    """
    Camera frame acquisition interface.

    This class manages the lifecycle of the camera device and
    provides a method to read frames as FrameData objects.

    Parameters
    ----------
    config : CameraConfig
        Configuration parameters for the camera.
    """

    def __init__(self, config: CameraConfig) -> None:
        """
        Initialize the camera capture system.

        Parameters
        ----------
        config : CameraConfig
            Camera configuration parameters.
        """
        self._config = config
        self._capture: Optional[cv2.VideoCapture] = None
        self._frame_counter: int = 0

    def start(self) -> None:
        """
        Open the camera device and configure capture properties.

        Raises
        ------
        RuntimeError
            If the camera cannot be opened.
        """
        self._capture = cv2.VideoCapture(self._config.device_index)

        if not self._capture.isOpened():
            raise RuntimeError("Failed to open camera device")

        self._capture.set(cv2.CAP_PROP_FRAME_WIDTH, self._config.width)
        self._capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self._config.height)
        self._capture.set(cv2.CAP_PROP_FPS, self._config.fps)


    def read(self) -> Optional[FrameData]:
        """
        Read a single frame from the camera.

        Returns
        -------
        Optional[FrameData]
            Captured frame packaged as FrameData, or None if
            the frame could not be read.
        """
        if self._capture is None:
            raise RuntimeError("Camera has not been started")

        success, frame = self._capture.read()

        if not success:
            return None

        height, width = frame.shape[:2]

        frame_data = FrameData(
            frame_id=self._frame_counter,
            image=frame,
            timestamp=time.time(),
            width=width,
            height=height,
        )

        self._frame_counter += 1

        return frame_data

    def stop(self) -> None:
        """
        Release the camera device.
        """
        if self._capture is not None:
            self._capture.release()
            self._capture = None