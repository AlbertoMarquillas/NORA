# Ficha Funcional – `gestion_salida_tts.py`

## Nombre del archivo:
`gestion_salida_tts.py`

## Responsabilidad principal:
Gestionar la salida de voz sintetizada (TTS) dentro del sistema NORA, con un enfoque en la modulación avanzada de la voz, control de interrupciones y gestión de las colas de salida. Este archivo se encarga de garantizar que la voz sintetizada se emita de manera coherente, permitiendo interrupciones (barge-in), controlando la latencia y asegurando la calidad de la salida en tiempo real.

## Entradas esperadas:
- **Tipo de entrada:** Texto para síntesis, parámetros de modulación de voz, instrucciones de control de interrupciones.
- **Fuente:** `tts.py` (para recibir el texto a sintetizar), `sistema/`, `agentes/` (para recibir instrucciones de modulación de la voz y control de la salida).
- **Formato o protocolo:** Texto plano, comandos internos (`CMD_...`), eventos de control de TTS.

## Salidas generadas:
- **Tipo de salida:** Audio sintetizado, control de interrupciones y colas de salida.
- **Destinatario:** Hardware de salida de audio (altavoces, salida de audio vía jack o USB).
- **Ejemplo de salida:**
  - `EVT_TTS_STARTED` (Evento que indica que la síntesis de voz ha comenzado).
  - `AGT_VOICE_GENERATED` (Evento que confirma que la voz ha sido generada y está lista para ser reproducida).
  - `CMD_EXECUTE_TTS` (Instrucción para ejecutar la síntesis de voz tras la modulación y control de interrupciones).

## Módulos relacionados:
- **Entrada desde:** `tts.py` (para recibir texto que debe ser sintetizado), `voz_main.py` (para manejar las instrucciones de salida y modulación de voz).
- **Salida hacia:** Hardware de salida de audio (altavoces o salida de audio USB).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar la modulación de la voz y las respuestas del sistema, especialmente en situaciones de interrupción o cambio de contexto.

## Dependencias técnicas:
- **Librerías externas:** `pyttsx3` (para la síntesis de voz), `pyaudio` (para la reproducción del audio generado), `numpy`, `scipy`.
- **Hardware gestionado:** Altavoces o salida de audio mediante jack o USB.
- **Protocolos:** PCM para la captura y reproducción del audio sintetizado, control de interrupciones y gestión de colas.

## Notas adicionales:
Este archivo es esencial para gestionar la salida de voz sintetizada en el sistema, permitiendo una experiencia auditiva de alta calidad. **`gestion_salida_tts.py`** ofrece un control avanzado sobre la síntesis de voz, ajustando aspectos como el tono, el ritmo y la velocidad de la voz. Además, se asegura de que la voz sintetizada pueda ser interrumpida si el usuario comienza a hablar, lo que mejora la interacción en tiempo real. Este archivo también maneja las colas de salida, garantizando que las respuestas de NORA se reproduzcan en el momento adecuado sin retrasos innecesarios.

## Archivos previstos del módulo:
- `gestion_salida_tts.py`: Gestión avanzada de la salida de voz sintetizada (modulación, control de interrupciones, colas de salida) (este archivo).
- Archivos adicionales como `tts.py`, `voz_main.py`, `config_voz.py`.
