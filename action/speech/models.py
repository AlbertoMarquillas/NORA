"""
Data models for the speech action module.

This module defines the internal contracts used by the speech subsystem:
requests, results, playback metadata, and status/event structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional
import time
import uuid


class SpeechStatus(str, Enum):
    """
    Lifecycle status of a speech action.
    """

    PENDING = "pending"
    SYNTHESIZING = "synthesizing"
    READY = "ready"
    PLAYING = "playing"
    COMPLETED = "completed"
    FAILED = "failed"


class SpeechPriority(int, Enum):
    """
    Priority level assigned to a speech request.
    """

    LOW = 1
    NORMAL = 5
    HIGH = 10
    CRITICAL = 20


@dataclass(slots=True)
class VoiceConfig:
    """
    Voice configuration used by the TTS engine.
    """

    language: str = "es"
    voice_name: Optional[str] = None
    speaking_rate: float = 1.0
    volume: float = 1.0
    pitch: float = 0.0


@dataclass(slots=True)
class PlaybackConfig:
    """
    Audio playback configuration for the generated speech.
    """

    blocking: bool = True
    interrupt_current: bool = False
    output_device: Optional[str] = None


@dataclass(slots=True)
class SpeechRequest:
    """
    Input request for a speech action.

    Attributes:
        text: Text to synthesize and reproduce.
        request_id: Unique identifier of the request.
        source: Originating module or subsystem.
        correlation_id: Optional identifier to link this action
            with an external event, FSM transition, or request chain.
        priority: Execution priority.
        voice: TTS voice configuration.
        playback: Playback behavior configuration.
        metadata: Free-form contextual information.
        created_at: Unix timestamp in seconds.
    """

    text: str
    request_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    source: str = "system"
    correlation_id: Optional[str] = None
    priority: SpeechPriority = SpeechPriority.NORMAL
    voice: VoiceConfig = field(default_factory=VoiceConfig)
    playback: PlaybackConfig = field(default_factory=PlaybackConfig)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: float = field(default_factory=time.time)

    def validate(self) -> None:
        """
        Validate the request content.

        Raises:
            ValueError: If the text is empty or contains only whitespace.
        """
        if not self.text or not self.text.strip():
            raise ValueError("SpeechRequest.text cannot be empty.")


@dataclass(slots=True)
class SynthesizedAudio:
    """
    Result of the TTS synthesis step.

    Attributes:
        request_id: Identifier of the originating speech request.
        audio_path: Filesystem path to the generated audio file.
        duration_s: Optional audio duration in seconds.
        sample_rate_hz: Optional sample rate in Hz.
        channels: Optional number of channels.
        metadata: Extra synthesis metadata.
    """

    request_id: str
    audio_path: str
    duration_s: Optional[float] = None
    sample_rate_hz: Optional[int] = None
    channels: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SpeechResult:
    """
    Final result of the speech action.

    Attributes:
        request_id: Identifier of the processed request.
        status: Final lifecycle status.
        audio_path: Generated audio file path, if available.
        message: Human-readable result message.
        error: Error details, if any.
        started_at: Unix timestamp in seconds.
        finished_at: Unix timestamp in seconds.
        metadata: Additional execution metadata.
    """

    request_id: str
    status: SpeechStatus
    audio_path: Optional[str] = None
    message: Optional[str] = None
    error: Optional[str] = None
    started_at: Optional[float] = None
    finished_at: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        """
        Return whether the speech action finished successfully.
        """
        return self.status == SpeechStatus.COMPLETED


@dataclass(slots=True)
class SpeechEvent:
    """
    Internal event emitted by the speech module.

    Attributes:
        request_id: Related speech request identifier.
        status: Current lifecycle status.
        source: Event source module.
        timestamp: Unix timestamp in seconds.
        detail: Optional human-readable detail.
        payload: Optional machine-readable payload.
    """

    request_id: str
    status: SpeechStatus
    source: str = "action.speech"
    timestamp: float = field(default_factory=time.time)
    detail: Optional[str] = None
    payload: Dict[str, Any] = field(default_factory=dict)