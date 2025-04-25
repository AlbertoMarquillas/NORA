# Ficha Funcional – `asr.py`

## Nombre del archivo:
`asr.py`

## Responsabilidad principal:
Gestionar el reconocimiento automático del habla (ASR) dentro del sistema NORA. Este archivo se encarga de convertir la señal de audio capturada por el micrófono en texto, utilizando modelos de ASR como `Vosk` o `Whisper`. El ASR es una de las partes fundamentales del sistema de voz, ya que permite que NORA entienda los comandos hablados y pueda interactuar con el usuario de manera natural.

## Entradas esperadas:
- **Tipo de entrada:** Señal de audio PCM desde el micrófono, comandos de configuración.
- **Fuente:** Micrófono USB, `sistema/`, `voz_main.py` (para recibir comandos de inicio, pausa o reconfiguración).
- **Formato o protocolo:** Stream de audio PCM, comandos internos (`CMD_...`), configuraciones en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Texto transcrito, eventos de reconocimiento de voz, comandos extraídos del texto.
- **Destinatario:** `voz_main.py`, `dialogo/`, `sistema/`, `agentes/` (para procesar el texto transcrito y generar respuestas o ejecutar comandos).
- **Ejemplo de salida:**
  - `EVT_SPEECH_RECOGNIZED` (Texto transcrito desde la señal de audio).
  - `EVT_COMMAND_PARSED` (Comando extraído del texto reconocido).
  - `CMD_EXECUTE_COMMAND` (Instrucción para ejecutar el comando reconocido).

## Módulos relacionados:
- **Entrada desde:** `voz_main.py` (para recibir la señal de audio y configuraciones).
- **Salida hacia:** `voz_main.py` (para devolver los resultados del reconocimiento de voz), `dialogo/`, `sistema/` (para ejecutar comandos o respuestas).
- **Comunicación bidireccional con:** `voz_main.py` (para gestionar la activación y los resultados del ASR), `agentes/` (para ejecutar acciones basadas en el texto transcrito).

## Dependencias técnicas:
- **Librerías externas:** `vosk`, `whisper`, `pyaudio`, `numpy`, `scipy`.
- **Hardware gestionado:** Micrófono USB para capturar la señal de audio.
- **Protocolos:** PCM para captura y reproducción de audio, eventos internos para comunicar los resultados del ASR.

## Notas adicionales:
El módulo **`asr.py`** es crucial para convertir la voz en texto, lo que permite que NORA interactúe de manera efectiva con el usuario. Este archivo gestiona la configuración y el procesamiento de audio para transcribir el habla en texto que luego puede ser analizado y procesado. Además, se puede configurar para adaptarse a diferentes tipos de micrófonos, condiciones de ruido y modelos de ASR personalizados.

## Archivos previstos del módulo:
- `asr.py`: Reconocimiento automático del habla (ASR) (este archivo).
- Archivos adicionales como `voz_main.py`, `tts.py`, `vad.py`.
