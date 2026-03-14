"""
Entry point for the vision perception service.
"""

from __future__ import annotations

from .config import VISION_CONFIG
from .service import VisionService


def main() -> None:
    """
    Start the vision perception service.
    """
    backend_endpoint = "http://localhost:8000/api/events/ingest/video/"

    service = VisionService(
        config=VISION_CONFIG,
        backend_endpoint=backend_endpoint,
    )

    service.start()


if __name__ == "__main__":
    main()