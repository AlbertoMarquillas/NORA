# Ficha Específica – `pipeline_audio.py`

## Nombre del archivo:
`pipeline_audio.py`

## Responsabilidad principal:
Definir y coordinar el flujo secuencial de procesamiento del audio capturado en tiempo real, orquestando la detección de actividad vocal, hotword, transcripción (ASR) y análisis emocional.

## Entradas esperadas:
- Stream de audio PCM en tiempo real.
- Configuraciones activas del módulo `voz/`.

## Salidas generadas:
- Resultados de cada etapa del procesamiento auditivo.
- Eventos internos según resultados:
  - `EVT_WAKEWORD_DETECTED`
  - `EVT_SPEECH_RECOGNIZED`
  - `EVT_COMMAND_PARSED`
  - `EVT_EMOTION_AUDIO_ANALYZED`

## Funcionalidades principales:
- Captura continua de audio desde micrófono.
- División en ventanas o segmentos temporales adecuados para análisis.
- Ejecución secuencial de:
  - Detección de actividad vocal (`vad.py`).
  - Detección de hotword (`hotword.py`).
  - Reconocimiento de voz (`asr.py`).
  - Análisis emocional (`emocion_audio.py`).
- Enrutamiento de los resultados hacia el sistema de eventos internos.
- Gestión de flujos de control como interrupción (barge-in) o suspensiones temporales.

## Dependencias técnicas:
- `sounddevice`, `pyaudio` – Captura y reproducción de audio.
- Submódulos de procesamiento de `voz/`.
- `asyncio` – Gestión eficiente y no bloqueante del flujo continuo de audio.

