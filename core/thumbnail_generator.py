"""Thumbnail generation placeholder."""


class ThumbnailGenerator:
    """Produces lightweight thumbnail bytes from frame bytes."""

    def generate(self, frame: bytes) -> bytes:
        """Return simple reduced payload as thumbnail placeholder."""
        return frame[:16]
