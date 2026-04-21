"""HTTP API server placeholder."""

from config.network_config import NetworkConfig
from core.camera_controller import CameraController
from server.routes_media import MediaRoutes
from server.routes_status import StatusRoutes
from storage.metadata_store import MetadataStore


class APIServer:
    """Simple server facade to aggregate route handlers."""

    def __init__(self, config: NetworkConfig | None = None) -> None:
        self.config = config or NetworkConfig()
        self.status_routes = StatusRoutes()
        self.media_routes = MediaRoutes()
        self._running = False

    def start(self) -> None:
        """Start placeholder API service."""
        self._running = True
        print(f"[APIServer] Listening on {self.config.host}:{self.config.port}")

    def stop(self) -> None:
        """Stop placeholder API service."""
        self._running = False

    def health(self, camera: CameraController) -> dict[str, object]:
        """Delegate health response."""
        return self.status_routes.health(camera)

    def media(self, store: MetadataStore) -> dict[str, list[dict[str, object]]]:
        """Delegate media response."""
        return self.media_routes.list_media(store)
