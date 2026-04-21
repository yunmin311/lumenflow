"""Video metadata repository."""

from dataclasses import dataclass


@dataclass(slots=True)
class VideoRecord:
    """Represents one recorded video item."""

    name: str
    duration_seconds: int
    created_at: str


class VideoRepository:
    """In-memory video index placeholder."""

    def __init__(self) -> None:
        self._records: list[VideoRecord] = []

    def add(self, record: VideoRecord) -> None:
        """Store video metadata record."""
        self._records.append(record)

    def list_all(self) -> list[VideoRecord]:
        """Return all video records."""
        return list(self._records)
