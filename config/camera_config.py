"""Camera configuration for Lumenflow."""

from dataclasses import dataclass


@dataclass(slots=True)
class CameraConfig:
    """Runtime camera settings used by capture pipeline."""

    device_id: int = 0
    width: int = 1920
    height: int = 1080
    fps: int = 30
    codec: str = "H264"
