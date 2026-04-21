"""Network configuration for Lumenflow."""

from dataclasses import dataclass


@dataclass(slots=True)
class NetworkConfig:
    """Network settings for hotspot and uplink."""

    host: str = "0.0.0.0"
    port: int = 8080
    websocket_port: int = 8765
    hotspot_ssid: str = "Lumenflow"
