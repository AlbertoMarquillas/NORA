# Ficha Específica – `tts.py`

## Nombre del archivo:
`tts.py`

## Responsabilidad principal:
Realizar la síntesis de voz (TTS) a partir de texto generado por el sistema, convirtiendo mensajes de texto en señales de audio reproducibles para la interacción auditiva de NORA.

## Entradas esperadas:
- Texto a sintetizar.
- Configuraciones dinámicas (voz seleccionada, velocidad de habla, tono, emoción si aplica).

## Salidas generadas:
- Stream de audio PCM o archivo de audio en formato `.wav`.
- Señales de control de inicio y fin de síntesis.

## Funcionalidades principales:
- Recepción de textos dinámicos para conversión a voz.
- Configuración de parámetros de voz: tono, velocidad, estilo.
- Ejecución de motor TTS (`pyttsx3`, `gTTS`, motor local adaptado).
- Emisión de audio en tiempo real o almacenamiento temporal en RAM.
- Emisión de señales o eventos al sistema al comenzar y terminar la reproducción.

## Dependencias técnicas:
- `pyttsx3` – Síntesis de voz local.
- `gTTS` (opcional) – Conversión de texto a voz mediante API online.
- `pyaudio`, `sounddevice` – Reproducción local de audio.
- `numpy` – Tratamiento de buffers de audio.

