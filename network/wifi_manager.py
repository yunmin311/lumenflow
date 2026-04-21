"""Wi-Fi manager abstraction."""


class WifiManager:
    """Tracks current Wi-Fi connection state."""

    def __init__(self) -> None:
        self._ssid: str | None = None

    def connect(self, ssid: str) -> None:
        """Mock connect to the given SSID."""
        self._ssid = ssid

    @property
    def current_ssid(self) -> str | None:
        """Return currently connected SSID."""
        return self._ssid
