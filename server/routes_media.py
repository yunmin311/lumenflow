"""Media route handlers."""

from dataclasses import asdict

from storage.metadata_store import MetadataStore


class MediaRoutes:
    """Provides media listing payloads."""

    def list_media(self, store: MetadataStore) -> dict[str, list[dict[str, object]]]:
        """Return image/video metadata as serializable dict."""
        return {
            "images": [asdict(r) for r in store.images.list_all()],
            "videos": [asdict(r) for r in store.videos.list_all()],
        }
