# Ficha Específica – `hotword.py`

## Nombre del archivo:
`hotword.py`

## Responsabilidad principal:
Detectar la pronunciación de una palabra clave (hotword) definida previamente, como "oye NORA", para activar dinámicamente el sistema o iniciar la atención auditiva.

## Entradas esperadas:
- Stream de audio PCM capturado en tiempo real.
- Configuraciones dinámicas (hotwords permitidas, umbral de sensibilidad).

## Salidas generadas:
- Evento de detección de hotword:
  - `EVT_WAKEWORD_DETECTED`

## Funcionalidades principales:
- Análisis continuo del audio en busca de patrones de la hotword.
- Aplicación de modelos ligeros de reconocimiento de palabras clave.
- Validación de detección mediante umbrales de confianza configurables.
- Emisión de eventos internos para activar la captura de voz y procesamiento de órdenes.

## Dependencias técnicas:
- `porcupine`, `snowboy` (opcional) – Motores de detección de hotword.
- `numpy` – Preprocesamiento de audio.
- `sounddevice`, `pyaudio` – Captura continua de audio.