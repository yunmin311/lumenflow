"""System information helpers."""

import platform


def basic_system_info() -> dict[str, str]:
    """Return minimal host metadata for status API."""
    return {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "python": platform.python_version(),
    }
