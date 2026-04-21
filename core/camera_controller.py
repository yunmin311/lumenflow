"""Camera controller for stream capture lifecycle."""

from config.camera_config import CameraConfig
from core.capture_monitor import CaptureMonitor


class CameraController:
    """Unified camera controller facade."""

    def __init__(self, config: CameraConfig | None = None) -> None:
        self.config = config or CameraConfig()
        self.monitor = CaptureMonitor()
        self._initialized = False

    def initialize(self) -> None:
        """Initialize camera device resources."""
        self._initialized = True
        print(f"[CameraController] Camera {self.config.device_id} initialized")

    def start_capture(self) -> None:
        """Start frame capture state."""
        if not self._initialized:
            raise RuntimeError("camera not initialized")
        self.monitor.start()

    def stop_capture(self) -> None:
        """Stop frame capture state."""
        self.monitor.stop()

    def capture_frame(self) -> bytes:
        """Capture one mock frame for framework validation."""
        if not self.monitor.running:
            raise RuntimeError("capture is not running")
        self.monitor.on_frame()
        return f"frame-{self.monitor.frame_count}".encode("utf-8")
