# Ficha Específica – `vad.py`

## Nombre del archivo:
`vad.py`

## Responsabilidad principal:
Detectar actividad vocal en el flujo de audio capturado para gestionar turnos de conversación y activar dinámicamente el reconocimiento de voz (ASR) cuando se detecta que el usuario comienza a hablar.

## Entradas esperadas:
- Stream de audio PCM en tiempo real.
- Configuraciones dinámicas (sensibilidad de detección, umbrales de energía, duración mínima de habla).

## Salidas generadas:
- Indicador de actividad vocal: `habla detectada` o `silencio`.
- Eventos asociados:
  - `EVT_USER_START_SPEAKING`
  - `EVT_USER_STOP_SPEAKING`

## Funcionalidades principales:
- Análisis de ventanas de audio para detectar energía vocal.
- Aplicación de algoritmos VAD (`WebRTC VAD` o técnicas propias).
- Gestión de umbrales dinámicos según el entorno acústico.
- Temporización para confirmar inicio y final de turnos de habla.
- Emisión de eventos internos para activar/desactivar ASR de manera reactiva.

## Dependencias técnicas:
- `webrtcvad` – Detección eficiente de actividad vocal.
- `numpy`, `scipy` – Preprocesamiento y análisis de señales de audio.
- `sounddevice`, `pyaudio` – Captura de audio en tiempo real.

