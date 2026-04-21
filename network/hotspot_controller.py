"""Hotspot mode controller."""


class HotspotController:
    """Minimal AP mode state holder."""

    def __init__(self) -> None:
        self._enabled = False

    def enable(self) -> None:
        """Enable hotspot mode."""
        self._enabled = True

    def disable(self) -> None:
        """Disable hotspot mode."""
        self._enabled = False

    @property
    def enabled(self) -> bool:
        """Whether hotspot mode is enabled."""
        return self._enabled
