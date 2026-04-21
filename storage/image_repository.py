"""Image metadata repository."""

from dataclasses import dataclass


@dataclass(slots=True)
class ImageRecord:
    """Represents one captured image item."""

    name: str
    created_at: str


class ImageRepository:
    """In-memory image index placeholder."""

    def __init__(self) -> None:
        self._records: list[ImageRecord] = []

    def add(self, record: ImageRecord) -> None:
        """Store image metadata record."""
        self._records.append(record)

    def list_all(self) -> list[ImageRecord]:
        """Return all image records."""
        return list(self._records)
