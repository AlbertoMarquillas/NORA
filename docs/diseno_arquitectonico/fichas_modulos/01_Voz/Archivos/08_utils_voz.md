# Ficha Funcional – `utils_voz.py`

## Nombre del archivo:
`utils_voz.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares y herramientas comunes para el procesamiento de audio y la gestión de texto dentro del sistema de voz de NORA. Este archivo contiene utilidades que facilitan el tratamiento de señales de audio (normalización, espectrogramas), así como funciones de soporte para el ASR y TTS, mejorando la calidad y la eficiencia del procesamiento.

## Entradas esperadas:
- **Tipo de entrada:** Señales de audio, texto para procesamiento y normalización, eventos de control.
- **Fuente:** Módulos `asr.py`, `tts.py`, `vad.py`, que requieren procesamiento adicional o normalización de audio.
- **Formato o protocolo:** Stream de audio PCM, texto plano, configuraciones de normalización y procesamiento de espectrogramas.

## Salidas generadas:
- **Tipo de salida:** Datos procesados, señales normalizadas, espectrogramas, eventos auxiliares.
- **Destinatario:** `asr.py`, `tts.py`, `voz_main.py` (para ser utilizados en el procesamiento de audio y en la generación de salida de voz).
- **Ejemplo de salida:**
  - `AGT_AUDIO_NORMALIZED` (Evento que indica que la señal de audio ha sido normalizada).
  - `CMD_PROCESS_SPECTROGRAM` (Instrucción para generar un espectrograma a partir de la señal de audio).
  - `EVT_TEXT_NORMALIZED` (Evento que indica que el texto ha sido procesado y normalizado para mejorar el reconocimiento y síntesis).

## Módulos relacionados:
- **Entrada desde:** `asr.py` (para recibir datos de audio para normalización), `tts.py` (para recibir texto para procesamiento o normalización).
- **Salida hacia:** `asr.py`, `tts.py`, `voz_main.py` (para procesar señales de audio y texto que mejoran el ASR y TTS).
- **Comunicación bidireccional con:** `asr.py`, `tts.py` para garantizar que el procesamiento y la normalización de audio y texto sea coherente.

## Dependencias técnicas:
- **Librerías externas:** `numpy`, `scipy` (para la manipulación y procesamiento de señales de audio), `librosa` (para la generación de espectrogramas y análisis de audio).
- **Hardware gestionado:** Micrófono USB (para capturar audio que se procesará), altavoces (para la salida de audio procesado).
- **Protocolos:** PCM para la captura y reproducción de audio, eventos internos para manejar las utilidades del procesamiento.

## Notas adicionales:
Este archivo es esencial para mejorar la calidad del procesamiento de la voz en el sistema NORA. Las funciones de normalización de audio y la creación de espectrogramas permiten que el sistema maneje mejor las señales de audio y optimice la entrada y salida de voz. También, la normalización de texto y el preprocesamiento permiten que tanto el ASR como el TTS funcionen de manera más precisa y eficiente, mejorando la interacción del usuario con NORA.

## Archivos previstos del módulo:
- `utils_voz.py`: Funciones auxiliares para normalización de audio, espectrogramas, etc. (este archivo).
- Archivos adicionales como `asr.py`, `tts.py`, `voz_main.py`.
