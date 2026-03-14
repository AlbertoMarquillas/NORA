"""
Event publishing utilities for the speech action module.

This module is responsible for publishing speech lifecycle events to the rest
of the system. It does not synthesize audio and does not perform playback.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict
import json
import logging
from typing import Any, Dict, Optional

from .config import SpeechModuleConfig
from .models import SpeechEvent, SpeechRequest, SpeechResult, SpeechStatus


LOGGER = logging.getLogger(__name__)


class CommandPublisherError(Exception):
    """
    Raised when a speech event cannot be published.
    """


class BaseCommandPublisher(ABC):
    """
    Abstract base class for speech event publishers.
    """

    def __init__(self, config: SpeechModuleConfig) -> None:
        """
        Initialize the publisher.

        Args:
            config: Speech module configuration.
        """
        self.config = config

    @abstractmethod
    def publish_event(self, event: SpeechEvent) -> None:
        """
        Publish a speech lifecycle event.

        Args:
            event: Event to publish.

        Raises:
            CommandPublisherError: If the event cannot be published.
        """
        raise NotImplementedError

    def publish_status(
        self,
        request: SpeechRequest,
        status: SpeechStatus,
        detail: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Publish a lifecycle event derived from a speech request.

        Args:
            request: Original speech request.
            status: Current speech lifecycle status.
            detail: Optional human-readable detail.
            payload: Optional machine-readable payload.

        Raises:
            CommandPublisherError: If the event cannot be published.
        """
        event = SpeechEvent(
            request_id=request.request_id,
            status=status,
            detail=detail,
            payload={
                "source": request.source,
                "correlation_id": request.correlation_id,
                "request_metadata": request.metadata,
                **(payload or {}),
            },
        )
        self.publish_event(event)

    def publish_result(
        self,
        request: SpeechRequest,
        result: SpeechResult,
    ) -> None:
        """
        Publish a final event derived from a speech result.

        Args:
            request: Original speech request.
            result: Final speech result.

        Raises:
            CommandPublisherError: If the event cannot be published.
        """
        event = SpeechEvent(
            request_id=request.request_id,
            status=result.status,
            detail=result.message or result.error,
            payload={
                "source": request.source,
                "correlation_id": request.correlation_id,
                "audio_path": result.audio_path,
                "ok": result.ok,
                "started_at": result.started_at,
                "finished_at": result.finished_at,
                "result_metadata": result.metadata,
                "request_metadata": request.metadata,
            },
        )
        self.publish_event(event)


class LoggingCommandPublisher(BaseCommandPublisher):
    """
    Publisher implementation that emits events through the Python logging system.

    This is useful as a safe default while the integration transport is not yet
    connected to WebSocket, HTTP, or an internal dispatcher.
    """

    def publish_event(self, event: SpeechEvent) -> None:
        """
        Publish a speech event by logging it as structured JSON.

        Args:
            event: Event to publish.

        Raises:
            CommandPublisherError: If the event serialization fails.
        """
        try:
            event_dict = asdict(event)
            event_dict["status"] = event.status.value

            LOGGER.info(
                "speech_event topic=%s payload=%s",
                self.config.publisher_topic,
                json.dumps(event_dict, ensure_ascii=False),
            )
        except Exception as exc:
            raise CommandPublisherError(
                f"Failed to log speech event: {exc}"
            ) from exc


class NullCommandPublisher(BaseCommandPublisher):
    """
    No-op publisher implementation.

    This publisher silently ignores publish calls. It is useful when event
    propagation is temporarily disabled.
    """

    def publish_event(self, event: SpeechEvent) -> None:
        """
        Ignore the publish request.

        Args:
            event: Event to ignore.
        """
        return


def build_command_publisher(config: SpeechModuleConfig) -> BaseCommandPublisher:
    """
    Factory function that builds the configured command publisher.

    Args:
        config: Speech module configuration.

    Returns:
        Concrete publisher instance.
    """
    if not config.publish_events:
        return NullCommandPublisher(config)

    return LoggingCommandPublisher(config)