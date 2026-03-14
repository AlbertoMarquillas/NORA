# Audio Module

This module handles audio perception for NORA.

## Responsibilities

- Microphone input abstraction
- Wake word detection
- Voice activity detection
- Audio event publishing
- Audio service orchestration

## Files

- config.py
- models.py
- service.py
- capture.py
- wake_word_detector.py
- vad.py
- event_publisher.py


# Audio Module v1

This module implements the first version of NORA audio perception.

## Scope

Version 1 only covers:

- live microphone capture
- wake word detection
- normalized event publication to NORA

## Internal flow

Microphone -> AudioCapture -> OpenWakeWordDetector -> AudioEventPublisher -> NORA backend

## Main files

- `config.py`: configuration dataclasses
- `models.py`: internal domain models
- `capture.py`: microphone input abstraction
- `wake_word_detector.py`: openWakeWord adapter
- `event_publisher.py`: normalized event generation and publication
- `service.py`: orchestration service

## Future extensions

Later versions may include:

- voice activity detection
- speech segmentation
- speech-to-text integration
- ambient audio analysis
- microphone health monitoring