# Ficha Funcional – `voz_main.py`

## Nombre del archivo:
`voz_main.py`

## Responsabilidad principal:
Orquestar el funcionamiento general del módulo de voz de NORA, gestionando la interacción entre los distintos submódulos de ASR, TTS, análisis emocional, y otros componentes. Este archivo se encarga de coordinar el flujo de trabajo entre los diferentes módulos de voz, activar el reconocimiento de voz, gestionar la síntesis de voz y aplicar las modulaciones emocionales correspondientes.

## Entradas esperadas:
- **Tipo de entrada:** Señal de audio para ASR, texto para TTS, eventos de análisis emocional, comandos de voz.
- **Fuente:** Micrófono USB (para capturar la señal de audio), `sistema/`, `agentes/`, `interfaz/` (para recibir comandos y eventos relacionados con la voz).
- **Formato o protocolo:** Stream de audio PCM, texto plano, eventos internos (`CMD_...`).

## Salidas generadas:
- **Tipo de salida:** Texto reconocido, audio sintetizado, eventos de control para los submódulos de ASR y TTS.
- **Destinatario:** `dialogo/`, `sistema/`, `interfaz/`, `agentes/`, hardware de audio.
- **Ejemplo de salida:**
  - `EVT_SPEECH_RECOGNIZED` (Texto transcrito del habla).
  - `EVT_COMMAND_PARSED` (Comando extraído del texto reconocido).
  - `EVT_WAKEWORD` (Detección de la palabra clave "oye NORA").
  - Stream de audio sintetizado enviado a salida sonora.

## Módulos relacionados:
- **Entrada desde:** `sistema/` (activación del sistema), `agentes/` (modulación de voz y emociones), `interfaz/` (pruebas de voz y control).
- **Salida hacia:** `dialogo/`, `interfaz/`, `sistema/`, `agentes/` (para manejar las respuestas y los eventos derivados de la voz).
- **Comunicación bidireccional con:** `dialogo/` (texto), `agentes/` (modulación de voz y emociones).

## Dependencias técnicas:
- **Librerías externas:** `pyaudio`, `pyttsx3`, `vosk`, `whisper`, `numpy`, `scipy`, `webrtcvad`.
- **Hardware gestionado:** Micrófono USB, salida de audio vía jack o USB.
- **Protocolos:** PCM para captura y reproducción, eventos internos para coordinar las tareas de voz.

## Notas adicionales:
Este archivo es el encargado de coordinar la entrada y salida de la información relacionada con la voz. A través de este archivo, NORA podrá reconocer comandos, generar respuestas auditivas y gestionar interrupciones de voz de manera dinámica. Es el "cerebro" que orquesta los módulos de reconocimiento de voz, síntesis de voz y análisis emocional, permitiendo que el sistema sea altamente interactivo y emocionalmente inteligente.

## Archivos previstos del módulo:
- `voz_main.py`: Orquestador general del módulo (este archivo).
- Archivos adicionales como `asr.py`, `tts.py`, `vad.py`, `emocion_audio.py`, `parser_comandos.py`, etc.
