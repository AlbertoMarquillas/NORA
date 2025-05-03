# Ficha Funcional – `vad.py`

## Nombre del archivo:
`vad.py`

## Responsabilidad principal:
Gestionar la detección de actividad vocal (VAD, por sus siglas en inglés) y la gestión del turno conversacional dentro del sistema NORA. Este archivo se encarga de detectar cuando el usuario está hablando (o no) y gestionar las interrupciones o cambios en la conversación. Es fundamental para optimizar el uso del ASR y garantizar que NORA solo procese audio relevante, evitando la captura de ruido de fondo.

## Entradas esperadas:
- **Tipo de entrada:** Señal de audio PCM, eventos de control y configuración del sistema.
- **Fuente:** Micrófono USB, `sistema/`, `voz_main.py` (para recibir eventos de activación y desactivación de la escucha activa).
- **Formato o protocolo:** Stream de audio PCM, eventos internos (`CMD_START_LISTENING`, `CMD_STOP_LISTENING`), configuraciones en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Señales de actividad vocal, eventos de turno conversacional, activación/desactivación de procesamiento de voz.
- **Destinatario:** `voz_main.py` (para activar o desactivar el procesamiento del ASR), `sistema/`, `dialogo/` (para gestionar la transición entre los turnos de conversación).
- **Ejemplo de salida:**
  - `EVT_VAD_DETECTED` (Evento que indica que se ha detectado actividad vocal).
  - `EVT_SILENCE_DETECTED` (Evento que indica que no se detecta actividad vocal, puede iniciar un temporizador para finalizar el turno de conversación).
  - `CMD_PROCESS_VOICE` (Instrucción para iniciar el procesamiento de voz tras detectar que el usuario está hablando).
  - `EVT_TURN_CHANGED` (Evento que indica que el turno conversacional ha cambiado, por ejemplo, de escucha a respuesta).

## Módulos relacionados:
- **Entrada desde:** `voz_main.py` (para recibir la señal de audio y controlar la activación del reconocimiento de voz), `sistema/` (para gestionar eventos de turno conversacional y control de la escucha).
- **Salida hacia:** `voz_main.py` (para activar o desactivar el procesamiento de voz y el ASR), `sistema/` (para coordinar la gestión de turnos y evitar la sobrecarga de procesamiento).
- **Comunicación bidireccional con:** `sistema/`, `dialogo/` para coordinar el flujo de la conversación y asegurar que el sistema solo procese los momentos relevantes de la interacción.

## Dependencias técnicas:
- **Librerías externas:** `webrtcvad` (para la detección de actividad vocal), `pyaudio` (para la captura de audio).
- **Hardware gestionado:** Micrófono USB (para capturar la señal de audio).
- **Protocolos:** PCM para captura de audio, eventos internos para coordinar el turno de conversación y la activación de la escucha activa.

## Notas adicionales:
El archivo **`vad.py`** es esencial para optimizar el uso del ASR y evitar procesar audio no relevante, como el ruido de fondo. La gestión del turno conversacional es clave para permitir que NORA responda solo cuando el usuario está hablando y para manejar las interrupciones de manera adecuada. Esto mejora la eficiencia del sistema y ofrece una experiencia más natural durante las interacciones.

## Archivos previstos del módulo:
- `vad.py`: Detección de actividad vocal y gestión del turno conversacional (este archivo).
- Archivos adicionales como `voz_main.py`, `asr.py`, `emocion_audio.py`.
