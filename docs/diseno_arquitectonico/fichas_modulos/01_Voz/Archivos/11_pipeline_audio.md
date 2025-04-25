# Ficha Funcional – `pipeline_audio.py`

## Nombre del archivo:
`pipeline_audio.py`

## Responsabilidad principal:
Gestionar el flujo de procesamiento auditivo en tiempo real dentro del sistema NORA. Este archivo se encarga de orquestar la captura de audio, la preprocesamiento de la señal, y el enrutamiento adecuado hacia los módulos correspondientes (como ASR, análisis emocional, y TTS). Asegura que el procesamiento de audio se realice de manera eficiente y fluida, manteniendo la sincronización y reduciendo la latencia.

## Entradas esperadas:
- **Tipo de entrada:** Señales de audio en tiempo real (PCM), configuraciones de procesamiento.
- **Fuente:** Micrófono USB, `vad.py` (para la detección de actividad vocal), `sistema/`, `voz_main.py` (para recibir instrucciones de procesamiento).
- **Formato o protocolo:** Stream de audio PCM, configuraciones en formato JSON para el procesamiento.

## Salidas generadas:
- **Tipo de salida:** Datos procesados de audio, señales de audio preprocesadas para los módulos ASR y TTS.
- **Destinatario:** `asr.py` (para pasar la señal de audio preprocesada para reconocimiento de voz), `tts.py` (para procesar el texto a voz).
- **Ejemplo de salida:**
  - `EVT_AUDIO_PROCESSED` (Evento que indica que la señal de audio ha sido procesada y está lista para su uso).
  - `CMD_FORWARD_AUDIO` (Instrucción para pasar la señal de audio al siguiente módulo para su procesamiento).
  - `AGT_AUDIO_BUFFER` (Buffer de audio procesado para ser utilizado por el ASR o TTS).

## Módulos relacionados:
- **Entrada desde:** `voz_main.py` (para recibir la señal de audio en tiempo real y enviarla al pipeline), `vad.py` (para gestionar el turno conversacional y la detección de actividad vocal).
- **Salida hacia:** `asr.py` (para pasar la señal preprocesada al sistema de reconocimiento de voz), `tts.py` (para la síntesis de voz).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para garantizar que el audio se procese correctamente y se utilicen los módulos correspondientes para los pasos posteriores.

## Dependencias técnicas:
- **Librerías externas:** `pyaudio`, `numpy`, `scipy`, `webrtcvad` (para la captura y procesamiento en tiempo real de la señal de audio).
- **Hardware gestionado:** Micrófono USB (para capturar la señal de audio), salida de audio mediante altavoces o USB (para emitir la voz sintetizada).
- **Protocolos:** PCM para captura de audio en tiempo real, eventos internos para el enrutamiento y procesamiento del audio.

## Notas adicionales:
Este archivo es esencial para asegurar que el procesamiento de la señal de audio se maneje de manera eficiente y efectiva. **`pipeline_audio.py`** organiza el flujo de trabajo entre los diferentes módulos de audio, como ASR y TTS, manteniendo el sistema en tiempo real y optimizando el uso de los recursos. Además, al centralizar el manejo de la señal de audio, se facilita la integración de nuevos componentes o cambios en el procesamiento de audio sin afectar al resto del sistema.

## Archivos previstos del módulo:
- `pipeline_audio.py`: Pipeline de procesamiento auditivo en tiempo real (este archivo).
- Archivos adicionales como `asr.py`, `vad.py`, `tts.py`.
