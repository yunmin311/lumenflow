"""Capture pipeline state monitor."""


class CaptureMonitor:
    """Tracks capture on/off status and counters."""

    def __init__(self) -> None:
        self._running = False
        self._frame_count = 0

    def start(self) -> None:
        """Mark capture as running."""
        self._running = True

    def stop(self) -> None:
        """Mark capture as stopped."""
        self._running = False

    def on_frame(self) -> None:
        """Increase frame counter when frame is captured."""
        if self._running:
            self._frame_count += 1

    @property
    def frame_count(self) -> int:
        """Return total frames captured in this session."""
        return self._frame_count

    @property
    def running(self) -> bool:
        """Whether capture is currently active."""
        return self._running
