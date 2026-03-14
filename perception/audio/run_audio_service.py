"""
Simple runner for the NORA audio perception service.

This script launches the microphone listener and prints detections.
"""

import time

from .config import AudioServiceConfig
from .service import AudioService


def main() -> None:
    """
    Start the audio perception service and keep it running.
    """

    config = AudioServiceConfig(debug=False)

    service = AudioService(config)

    print("Starting NORA audio service...")
    service.start()

    try:
        while True:
            status = service.get_status()
            print(
                f"Running: {status.running} | "
                f"Chunks processed: {status.processed_chunks}",
                end="\r",
            )
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping audio service...")
        service.stop()


if __name__ == "__main__":
    main()