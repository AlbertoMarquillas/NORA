# Ficha Funcional – `motor_personalidad_voz.py`

## Nombre del archivo:
`motor_personalidad_voz.py`

## Responsabilidad principal:
Seleccionar y modulación de perfiles de voz con rasgos diferenciados para NORA, adaptando la voz del sistema a diferentes contextos o personalidades del usuario. Este archivo permite que NORA tenga diferentes tipos de "personalidades" vocales, ajustando el tono, la velocidad y el timbre de la voz según la interacción, la emoción y el contexto, creando una experiencia más personalizada y variada.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de modulación de voz, parámetros de personalización de voz, instrucciones de cambio de personalidad.
- **Fuente:** `sistema/`, `agentes/`, `voz_main.py` (para recibir los parámetros y comandos relacionados con las características de la voz).
- **Formato o protocolo:** Parámetros de voz en formato JSON, eventos internos (`CMD_...`), configuraciones de personalidad.

## Salidas generadas:
- **Tipo de salida:** Cambios en las características de la voz, ajustes de modulación (tono, velocidad, timbre) para cambiar la personalidad vocal de NORA.
- **Destinatario:** `tts.py` (para aplicar la personalidad seleccionada en la voz sintetizada).
- **Ejemplo de salida:**
  - `CMD_APPLY_VOICE_PERSONALITY` (Instrucción para aplicar un perfil de voz con características específicas, como un tono más cálido o autoritario).
  - `EVT_VOICE_PERSONALITY_CHANGED` (Evento que indica que la personalidad de la voz ha sido modificada correctamente).
  - `AGT_VOICE_PROFILE_UPDATED` (Confirmación de que el perfil de voz ha sido ajustado y actualizado para reflejar una nueva personalidad).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `voz_main.py` (para recibir parámetros de cambio de personalidad vocal y modulación de voz).
- **Salida hacia:** `tts.py` (para aplicar las modificaciones en la voz sintetizada).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar el cambio de personalidad vocal con las interacciones del sistema.

## Dependencias técnicas:
- **Librerías externas:** `pyttsx3` (para gestionar la modulación de la voz sintetizada), `pyaudio` (para la captura y la manipulación del audio generado).
- **Hardware gestionado:** Ninguno directamente (se gestiona a nivel lógico la personalización de la voz).
- **Protocolos:** PCM para la captura y reproducción de audio, eventos internos para coordinar la aplicación de perfiles de voz.

## Notas adicionales:
Este archivo es fundamental para dotar a NORA de una personalidad vocal diferenciada y flexible, adaptando la voz según el contexto de la conversación o las preferencias del usuario. La capacidad de cambiar de personalidad vocal permite que NORA interactúe de una manera más variada, ofreciendo una experiencia más rica y personalizada. Además, la personalización de la voz mejora la conexión emocional con el usuario, haciéndola más apropiada para situaciones diferentes.

## Archivos previstos del módulo:
- `motor_personalidad_voz.py`: Selección y modulación de perfiles de voz con rasgos diferenciados (este archivo).
- Archivos adicionales como `tts.py`, `voz_main.py`, `config_voz.py`.
