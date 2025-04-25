# Ficha Específica – `asr.py`

## Nombre del archivo:
`asr.py`

## Responsabilidad principal:
Realizar el reconocimiento automático del habla (ASR) a partir del flujo de audio capturado, transcribiendo la voz del usuario en texto para su posterior procesamiento semántico o contextual dentro de NORA.

## Entradas esperadas:
- Stream de audio PCM capturado en tiempo real.
- Configuraciones dinámicas (idioma, motor ASR seleccionado, sensibilidad a ruido).

## Salidas generadas:
- Texto transcrito de la voz del usuario.
- Nivel de confianza en la transcripción.
- Eventos asociados:
  - `EVT_SPEECH_RECOGNIZED`

## Funcionalidades principales:
- Recepción de audio en buffers temporales o streams continuos.
- Preprocesamiento del audio: normalización de volumen, reducción de ruido si procede.
- Inferencia mediante modelo de ASR (`Vosk`, `Whisper`, modelo propio).
- Postprocesado de texto transcrito (opcionalmente aplicado en `normalizacion_texto.py`).
- Emisión de eventos de texto reconocido junto a métricas de confianza.

## Dependencias técnicas:
- `vosk`, `whisper` – Librerías de reconocimiento de voz.
- `numpy`, `scipy` – Preprocesamiento de señales de audio.
- `sounddevice`, `pyaudio` – Captura de audio en tiempo real.

