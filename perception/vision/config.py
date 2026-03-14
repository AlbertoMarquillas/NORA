"""
Configuration module for the vision perception subsystem.

This file centralizes all configuration parameters required by the
vision service. The goal is to avoid hardcoded constants distributed
across the codebase and to allow easy modification of runtime behavior.

The parameters defined here control camera capture, YOLO pose inference,
gesture detection logic, and activation cooldown timing.
"""

from dataclasses import dataclass, field


@dataclass
class CameraConfig:
    """
    Camera configuration parameters.

    Attributes
    ----------
    device_index : int
        Index of the camera device used by OpenCV.

    width : int
        Frame width requested from the camera.

    height : int
        Frame height requested from the camera.

    fps : int
        Target capture framerate.
    """

    device_index: int = 0
    width: int = 640
    height: int = 480
    fps: int = 30


@dataclass
class PoseModelConfig:
    """
    Configuration parameters for the YOLO pose estimation model.

    Attributes
    ----------
    model_path : str
        Path or model name used by Ultralytics YOLO pose.

    conf_threshold : float
        Minimum confidence threshold used during inference.

    imgsz : int
        Inference image size passed to the model.

    device : str
        Device used by the backend, for example 'cpu', 'cuda', or '0'.

    verbose : bool
        Whether Ultralytics should print verbose inference logs.
    """

    model_path: str = "yolo11n-pose.pt"
    conf_threshold: float = 0.5
    imgsz: int = 640
    device: str = "cpu"
    verbose: bool = False


@dataclass
class GestureConfig:
    """
    Configuration parameters controlling gesture recognition.

    Attributes
    ----------
    activation_gesture : str
        Name of the gesture used to trigger the activation event.

    frames_required : int
        Number of consecutive frames in which the gesture must be detected
        before being considered valid.

    wrist_above_shoulder_threshold : float
        Minimum vertical margin required for the wrist to be considered
        above the shoulder.
    """

    activation_gesture: str = "right_hand_raised"
    frames_required: int = 8
    wrist_above_shoulder_threshold: float = 0.05


@dataclass
class CooldownConfig:
    """
    Cooldown parameters to avoid repeated event triggering.

    Attributes
    ----------
    cooldown_seconds : float
        Minimum time interval between two consecutive activations.
    """

    cooldown_seconds: float = 3.0


@dataclass
class VisionConfig:
    """
    Global configuration container for the vision subsystem.

    This object aggregates all sub-configurations used by the service.
    """

    camera: CameraConfig = field(default_factory=CameraConfig)
    pose: PoseModelConfig = field(default_factory=PoseModelConfig)
    gesture: GestureConfig = field(default_factory=GestureConfig)
    cooldown: CooldownConfig = field(default_factory=CooldownConfig)


VISION_CONFIG = VisionConfig()