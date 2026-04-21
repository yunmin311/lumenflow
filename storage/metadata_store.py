"""Unified metadata store for media records."""

from storage.image_repository import ImageRepository
from storage.video_repository import VideoRepository


class MetadataStore:
    """Facade over image/video repositories."""

    def __init__(self) -> None:
        self.images = ImageRepository()
        self.videos = VideoRepository()
