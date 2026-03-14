"""
Event publisher for the vision perception subsystem.

This module is responsible for converting gesture detections into
system events and sending them to the central backend or FSM.

The communication mechanism implemented here uses HTTP POST requests.
"""

from __future__ import annotations

import time
from typing import Dict, Any

import requests

from .models import VisionEvent


class EventPublisher:
    """
    Publishes vision events to the backend system.

    Parameters
    ----------
    endpoint_url : str
        HTTP endpoint that receives the events.
    """

    def __init__(self, endpoint_url: str) -> None:
        """
        Initialize the event publisher.

        Parameters
        ----------
        endpoint_url : str
            Backend endpoint used to deliver the event.
        """
        self._endpoint_url = endpoint_url

    def build_event(
        self,
        gesture_name: str,
        confidence: float,
        metadata: Dict[str, Any],
    ) -> VisionEvent:
        """
        Build a VisionEvent object from gesture detection information.

        Parameters
        ----------
        gesture_name : str
            Name of the detected gesture.

        confidence : float
            Confidence score associated with the gesture.

        metadata : Dict[str, Any]
            Additional gesture-related information.

        Returns
        -------
        VisionEvent
            Constructed vision event.
        """
        return VisionEvent(
            event_type="vision_activation",
            source="vision",
            timestamp=time.time(),
            payload={
                "gesture": gesture_name,
                "confidence": confidence,
                "metadata": metadata,
            },
        )

    def publish(self, event: VisionEvent) -> None:
        """
        Send the event to the backend system.

        Parameters
        ----------
        event : VisionEvent
            Event to be sent.
        """
        payload = {
            "event_type": event.event_type,
            "source": event.source,
            "timestamp": event.timestamp,
            "payload": event.payload,
        }

        try:
            response = requests.post(self._endpoint_url, json=payload, timeout=2)

            if response.status_code != 200:
                print(f"[VISION] Event rejected by backend: {response.status_code}")

        except requests.RequestException as exc:
            print(f"[VISION] Failed to publish event: {exc}")