# Ficha Específica – `emocion_audio.py`

## Nombre del archivo:
`emocion_audio.py`

## Responsabilidad principal:
Analizar las características acústicas del flujo de audio capturado para inferir el estado emocional del usuario, como alegría, tristeza, enfado o neutralidad, enriqueciendo el contexto de interacción de NORA.

## Entradas esperadas:
- Segmentos de audio PCM procesados.
- Configuraciones dinámicas (modelos de emociones activos, umbrales de sensibilidad).

## Salidas generadas:
- Estado emocional detectado: `feliz`, `triste`, `enfadado`, `neutral`, entre otros.
- Nivel de confianza en la clasificación.
- Eventos asociados:
  - `EVT_EMOTION_AUDIO_ANALYZED`

## Funcionalidades principales:
- Extracción de características acústicas: tono fundamental (F0), energía, velocidad de habla.
- Aplicación de modelos de clasificación emocional entrenados (MLP, CNN o equivalentes).
- Categorización de la emoción dominante en segmentos analizados.
- Suavizado temporal para evitar cambios emocionales erráticos.
- Emisión de eventos internos sobre cambios emocionales detectados.

## Dependencias técnicas:
- `numpy`, `scipy` – Extracción de características acústicas.
- `TensorFlow`, `PyTorch` – Inferencia de modelos de clasificación de emociones.
- `sounddevice`, `pyaudio` – Captura y segmentación de audio.