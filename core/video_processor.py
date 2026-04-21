"""Video processing placeholder."""


class VideoProcessor:
    """Performs lightweight pseudo processing for scaffold stage."""

    def process(self, frame: bytes) -> bytes:
        """Return frame unchanged; hook for future transcoding pipeline."""
        return frame
