"""Lumenflow entry point."""

from core.camera_controller import CameraController
from core.file_manager import FileManager
from server.api_server import APIServer


def main() -> None:
    """Boot minimal camera transmission scaffold."""
    print("=== LUMENFLOW SYSTEM START ===")

    camera = CameraController()
    files = FileManager()
    server = APIServer()

    camera.initialize()
    files.initialize()
    server.start()

    print("=== SYSTEM RUNNING ===")


if __name__ == "__main__":
    main()
