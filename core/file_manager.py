"""File and directory management utilities."""

from pathlib import Path

from config.system_config import SystemConfig


class FileManager:
    """Responsible for project media path initialization."""

    def __init__(self, config: SystemConfig | None = None) -> None:
        self.config = config or SystemConfig()

    def initialize(self) -> None:
        """Create media directories if missing."""
        root = self.config.media_root
        for folder in (self.config.image_dir, self.config.video_dir, self.config.thumbnail_dir):
            Path(root / folder).mkdir(parents=True, exist_ok=True)
        print("[FileManager] File system ready")
