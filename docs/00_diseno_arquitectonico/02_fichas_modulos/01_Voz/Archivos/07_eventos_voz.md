# Ficha Funcional – `eventos_voz.py`

## Nombre del archivo:
`eventos_voz.py`

## Responsabilidad principal:
Definir y emitir los eventos estándar del módulo de voz dentro del sistema NORA. Este archivo se encarga de estandarizar la creación de eventos relacionados con el procesamiento de audio, como el reconocimiento de voz, la detección de la palabra clave, y la emisión de respuestas de voz, permitiendo una gestión coherente de estos eventos en todo el sistema.

## Entradas esperadas:
- **Tipo de entrada:** Comandos generados por el ASR, TTS, eventos de procesamiento de audio.
- **Fuente:** Módulos como `asr.py`, `tts.py`, `vad.py`, `voz_main.py`, que generan eventos relacionados con la voz.
- **Formato o protocolo:** Eventos internos (`EVT_...`), comandos generados tras el reconocimiento o la síntesis de voz.

## Salidas generadas:
- **Tipo de salida:** Eventos estándar que indican el estado de los procesos de voz, como la transcripción de texto, la síntesis de voz y la detección de palabras clave.
- **Destinatario:** `voz_main.py`, `sistema/`, `agentes/`, `interfaz/` (para manejar los eventos generados en el sistema de voz).
- **Ejemplo de salida:**
  - `EVT_SPEECH_RECOGNIZED` (Evento que indica que se ha reconocido el habla y se ha transcrito a texto).
  - `EVT_COMMAND_PARSED` (Evento que indica que el comando extraído del texto ha sido interpretado correctamente).
  - `EVT_WAKEWORD` (Evento que indica que se ha detectado la palabra clave, como "oye NORA").
  - `AGT_VOICE_OUTPUT` (Evento que indica que se ha generado una salida de voz, ya sea de respuesta o de síntesis).

## Módulos relacionados:
- **Entrada desde:** `asr.py` (para recibir eventos de transcripción de audio), `tts.py` (para recibir eventos de salida de voz generada).
- **Salida hacia:** `voz_main.py`, `sistema/`, `agentes/`, `interfaz/` (para distribuir los eventos a los módulos correspondientes y coordinar la ejecución de respuestas de voz).
- **Comunicación bidireccional con:** `voz_main.py` y otros módulos de procesamiento de voz, para garantizar que los eventos sean emitidos y procesados de manera adecuada.

## Dependencias técnicas:
- **Librerías externas:** `pyee` o `eventbus` (para la gestión de eventos internos en el sistema).
- **Hardware gestionado:** Micrófono USB, salida de audio vía jack o USB (según el evento de audio generado).
- **Protocolos:** PCM para la captura y reproducción de audio, eventos internos para manejar los eventos relacionados con la voz.

## Notas adicionales:
Este archivo es esencial para garantizar que todos los eventos relacionados con el procesamiento de voz sean gestionados de manera coherente. Al estandarizar la creación y emisión de eventos, `eventos_voz.py` permite que otros módulos del sistema puedan reaccionar a eventos como la transcripción de audio, la detección de comandos, y la síntesis de voz de forma sincronizada. Esta organización facilita la integración de la interacción por voz dentro del flujo general del sistema.

## Archivos previstos del módulo:
- `eventos_voz.py`: Emisión de eventos estándar del módulo de voz (este archivo).
- Archivos adicionales como `voz_main.py`, `asr.py`, `tts.py`.
