"""System-level configuration for Lumenflow."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class SystemConfig:
    """Global paths and behavior switches."""

    media_root: Path = Path("data")
    image_dir: str = "images"
    video_dir: str = "videos"
    thumbnail_dir: str = "thumbnails"
    keep_days: int = 7
