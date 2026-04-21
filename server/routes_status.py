"""Status route handlers."""

from core.camera_controller import CameraController
from utils.system_info import basic_system_info
from utils.time_utils import utc_now_iso


class StatusRoutes:
    """Provides status endpoint payloads."""

    def health(self, camera: CameraController) -> dict[str, object]:
        """Return basic service and camera health."""
        return {
            "status": "ok",
            "time": utc_now_iso(),
            "camera_initialized": camera is not None,
            "system": basic_system_info(),
        }
