# Ficha Funcional – `hotword.py`

## Nombre del archivo:
`hotword.py`

## Responsabilidad principal:
Gestionar la detección de la palabra clave (hotword) que activa el sistema NORA, como “oye NORA”. Este archivo se encarga de escuchar continuamente el audio entrante y de activar el procesamiento del sistema cuando se detecta la palabra clave, permitiendo así una interacción sin necesidad de una acción manual para activar el sistema.

## Entradas esperadas:
- **Tipo de entrada:** Señal de audio PCM en tiempo real.
- **Fuente:** Micrófono USB.
- **Formato o protocolo:** Stream de audio PCM capturado mediante `pyaudio`, `sounddevice`, o librerías similares.

## Salidas generadas:
- **Tipo de salida:** Activación del sistema, evento de detección de palabra clave.
- **Destinatario:** `voz_main.py` (para iniciar el procesamiento de voz tras la activación por la hotword).
- **Ejemplo de salida:**
  - `EVT_WAKEWORD_DETECTED` (Evento que indica que se ha detectado la palabra clave "oye NORA").
  - `CMD_ACTIVATE_VOICE_RECOGNITION` (Instrucción para activar el reconocimiento de voz tras detectar la palabra clave).
  - `AGT_HOTWORD_DETECTED` (Confirmación de que la palabra clave ha sido detectada).

## Módulos relacionados:
- **Entrada desde:** `voz_main.py` (para recibir la señal de audio y escuchar la activación de la hotword).
- **Salida hacia:** `voz_main.py` (para iniciar el procesamiento de voz).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` (para coordinar la activación y la modulación de voz según la detección de la hotword).

## Dependencias técnicas:
- **Librerías externas:** `webrtcvad` (para detección de actividad vocal y filtrado de ruido), `pyaudio` (para captura de audio en tiempo real), `snowboy` o `porcupine` (librerías de detección de hotword, si se utilizan).
- **Hardware gestionado:** Micrófono USB (para capturar la señal de audio).
- **Protocolos:** PCM para captura de audio en tiempo real, eventos internos para la activación del sistema.

## Notas adicionales:
Este archivo es clave para hacer que NORA sea completamente interactivo mediante voz sin necesidad de intervención manual. La detección de la palabra clave, como “oye NORA”, permite que el sistema esté siempre listo para escuchar y responder a las solicitudes del usuario. El sistema es capaz de escuchar constantemente el entorno sin procesar constantemente el audio, lo que mejora la eficiencia del sistema.

## Archivos previstos del módulo:
- `hotword.py`: Detección de palabra clave (“oye NORA”) (este archivo).
- Archivos adicionales como `voz_main.py`, `vad.py`, `asr.py`.
