"""GPIO abstraction for hardware trigger and LED operations."""


class GPIOController:
    """Lightweight GPIO controller placeholder."""

    def __init__(self) -> None:
        self._ready = False

    def initialize(self) -> None:
        """Initialize GPIO resources."""
        self._ready = True

    @property
    def ready(self) -> bool:
        """Whether GPIO layer is ready."""
        return self._ready
