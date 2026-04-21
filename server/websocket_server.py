"""WebSocket server placeholder for real-time push."""


class WebSocketServer:
    """Tracks ws server lifecycle for future stream push."""

    def __init__(self) -> None:
        self._running = False

    def start(self) -> None:
        """Start ws service placeholder."""
        self._running = True

    def stop(self) -> None:
        """Stop ws service placeholder."""
        self._running = False

    @property
    def running(self) -> bool:
        """Whether ws service is active."""
        return self._running
