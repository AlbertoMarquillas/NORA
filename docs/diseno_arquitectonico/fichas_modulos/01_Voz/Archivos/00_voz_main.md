# Ficha Específica – `voz_main.py`

## Nombre del archivo:
`voz_main.py`

## Responsabilidad principal:
Coordinar el flujo general del módulo `voz/`. Inicializa los submódulos de entrada (ASR), salida (TTS), análisis emocional de voz, detección de hotword y gestión de actividad vocal. Orquesta la captura de audio, la transcripción, el análisis emocional y la síntesis de respuestas en función de los eventos del sistema.

## Entradas esperadas:
- Flujo de audio capturado en tiempo real (stream PCM).
- Eventos de activación o reactivación (`EVT_WAKEWORD`, `EVT_USER_START_SPEAKING`, etc.).
- Comandos de configuración o reconfiguración dinámica.

## Salidas generadas:
- Texto transcrito del ASR.
- Audio sintetizado vía TTS.
- Eventos perceptivos y semánticos:
  - `EVT_SPEECH_RECOGNIZED`
  - `EVT_COMMAND_PARSED`
  - `EVT_EMOTION_AUDIO_ANALYZED`
  - `EVT_WAKEWORD_DETECTED`

## Funcionalidades principales:
- Inicialización de dispositivos de entrada/salida de audio.
- Orquestación de captura, procesamiento, análisis y síntesis.
- Llamadas secuenciales a `asr.py`, `emocion_audio.py`, `hotword.py`, `parser_comandos.py`, `tts.py`.
- Gestión de eventos para activar el reconocimiento o la respuesta de voz.
- Coordinación con `pipeline_audio.py` para un procesamiento eficiente.
- Gestión de interrupciones (barge-in) y turnos de conversación.

## Dependencias técnicas:
- `pyaudio`, `sounddevice` – Captura y reproducción de audio.
- `asyncio` – Gestión no bloqueante de streams de audio.
- Submódulos específicos de `voz/`.

