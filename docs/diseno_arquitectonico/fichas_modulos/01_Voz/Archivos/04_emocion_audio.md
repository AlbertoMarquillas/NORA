# Ficha Funcional – `emocion_audio.py`

## Nombre del archivo:
`emocion_audio.py`

## Responsabilidad principal:
Gestionar el análisis emocional basado en las características acústicas de la señal de audio. Este archivo se encarga de extraer características emocionales de la voz, como el tono, ritmo, y volumen, y utiliza esa información para modificar la síntesis de voz (TTS) y la modulación de la respuesta auditiva de NORA. 

## Entradas esperadas:
- **Tipo de entrada:** Señales de audio, parámetros de modulación emocional, comandos internos.
- **Fuente:** `voz_main.py`, `asr.py`, `vad.py`, que proporcionan audio grabado o texto convertido a audio.
- **Formato o protocolo:** Stream de audio PCM, eventos de control emocional, texto o audio de entrada.

## Salidas generadas:
- **Tipo de salida:** Análisis emocional de la señal de audio, parámetros de modulación vocal (tono, ritmo, volumen).
- **Destinatario:** `tts.py` (para modificar la salida de voz según la emoción detectada), `voz_main.py` (para la integración de modulación emocional en las respuestas).
- **Ejemplo de salida:**
  - `AGT_EMOTION_DETECTED` (Evento que indica que se ha detectado una emoción en la señal de audio).
  - `CMD_MODULATE_VOICE` (Instrucción para ajustar el tono, volumen o ritmo de la síntesis de voz según la emoción detectada).
  - `EVT_AUDIO_EMOTION` (Evento que transmite las características emocionales detectadas a los otros módulos).

## Módulos relacionados:
- **Entrada desde:** `voz_main.py` (para recibir la señal de audio o texto convertido a audio), `asr.py` (para extraer texto del habla, luego analizar emociones), `vad.py` (para detectar si hay actividad vocal).
- **Salida hacia:** `tts.py` (para ajustar la modulación de la voz), `voz_main.py` (para transmitir las características emocionales y adaptar las respuestas).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar la modulación emocional de las respuestas y hacer el sistema más dinámico y empático.

## Dependencias técnicas:
- **Librerías externas:** `webrtcvad` (para la detección de actividad vocal), `librosa` (para la extracción de características de audio como tono, ritmo, volumen), `numpy`, `scipy`.
- **Hardware gestionado:** Micrófono USB (para capturar la señal de audio).
- **Protocolos:** PCM para la captura de audio, eventos internos para la integración emocional en el sistema de voz.

## Notas adicionales:
Este archivo es fundamental para hacer que las respuestas de NORA no solo sean textuales y sintéticas, sino también emocionalmente coherentes con el contexto del usuario. A través del análisis acústico, el `emocion_audio.py` adapta las respuestas vocales de NORA, ajustando el tono, ritmo y volumen para reflejar emociones como alegría, tristeza, sorpresa, etc. Esta capacidad mejora la interacción auditiva y hace que el sistema sea más empático y adecuado para diferentes situaciones.

## Archivos previstos del módulo:
- `emocion_audio.py`: Análisis emocional basado en tono, ritmo y volumen (este archivo).
- Archivos adicionales como `tts.py`, `vad.py`, `voz_main.py`.
