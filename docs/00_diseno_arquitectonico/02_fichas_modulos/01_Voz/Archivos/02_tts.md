# Ficha Funcional – `tts.py`

## Nombre del archivo:
`tts.py`

## Responsabilidad principal:
Gestionar la síntesis de voz (TTS) dentro del sistema NORA. Este archivo se encarga de convertir el texto procesado en audio, generando respuestas auditivas que NORA puede emitir. También permite la modulación de la voz sintetizada en función del estado emocional del sistema, el tono, la velocidad y otras características de la prosodia.

## Entradas esperadas:
- **Tipo de entrada:** Texto para síntesis, parámetros de modulación de voz.
- **Fuente:** `voz_main.py`, `dialogo/`, `agentes/` (para recibir el texto que debe ser convertido en audio y las instrucciones de modulación).
- **Formato o protocolo:** Texto plano, parámetros de modulación (tensión, tono, velocidad), configuraciones en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Audio sintetizado, generado a partir del texto de entrada.
- **Destinatario:** Hardware de audio (altavoces, salida de audio mediante jack o USB).
- **Ejemplo de salida:**
  - `EVT_TTS_STARTED` (Evento que indica que la síntesis de voz ha comenzado).
  - `AGT_VOICE_GENERATED` (Evento que indica que la voz ha sido generada y está lista para ser reproducida).
  - Audio sintetizado en formato WAV o stream de audio directo a la salida sonora.

## Módulos relacionados:
- **Entrada desde:** `voz_main.py` (para recibir texto que debe ser sintetizado), `dialogo/` (para recibir texto generado desde las interacciones del usuario).
- **Salida hacia:** Hardware de salida de audio (altavoces o salida de audio USB).
- **Comunicación bidireccional con:** `agentes/`, `sistema/` para coordinar la modulación emocional de la voz.

## Dependencias técnicas:
- **Librerías externas:** `pyttsx3` (para la síntesis de voz), `pyaudio` (para la reproducción del audio generado), `numpy`, `scipy`.
- **Hardware gestionado:** Altavoces o salida de audio USB/jack.
- **Protocolos:** PCM para la captura y reproducción del audio sintetizado.

## Notas adicionales:
El archivo **`tts.py`** es esencial para que NORA pueda generar respuestas auditivas, transformando texto en audio. Además, permite modulación avanzada de la voz sintetizada, ajustando el tono, la velocidad y la variabilidad prosódica para que las respuestas sean más naturales y empáticas. Este archivo también permite adaptarse a diferentes estados emocionales del sistema, lo que genera una experiencia auditiva más rica y coherente.

## Archivos previstos del módulo:
- `tts.py`: Síntesis de texto a voz (TTS) (este archivo).
- Archivos adicionales como `voz_main.py`, `emocion_audio.py`, `normalizacion_texto.py`.
