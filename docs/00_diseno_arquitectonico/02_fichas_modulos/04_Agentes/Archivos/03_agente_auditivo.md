# Ficha Funcional – `agente_auditivo.py`

## Nombre del archivo:
`agente_auditivo.py`

## Responsabilidad principal:
Gestionar la percepción auditiva del sistema NORA, evaluando eventos relacionados con el reconocimiento de la voz, el análisis emocional del tono de voz y las interrupciones en la comunicación. Este agente toma decisiones basadas en las entradas auditivas y modula las respuestas del sistema según el estado emocional o la interacción vocal del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de reconocimiento de voz, análisis de tono vocal, detección de interrupciones y cambios emocionales en la voz.
- **Fuente:** Módulo `voz/`, que proporciona datos sobre la transcripción del habla, el análisis de emociones vocales y la detección de palabras clave.
- **Formato o protocolo:** Eventos de voz (`EVT_SPEECH_RECOGNIZED`, `EVT_EMOTION_VOICE_HAPPY`, `EVT_EMOTION_VOICE_SAD`).

## Salidas generadas:
- **Tipo de salida:** Decisiones contextuales sobre el tono de voz y emociones, acciones relacionadas con la activación o desactivación de respuestas vocales.
- **Destinatario:** `voz/` (para generar respuestas vocales apropiadas según la emoción detectada), `interfaz/` (para ajustar la expresión visual en respuesta a la emoción vocal).
- **Ejemplo de salida:**
  - `AGT_VOICE_EMOTION_RECOGNIZED` (Evento que indica que se ha detectado una emoción específica en la voz del usuario).
  - `CMD_VOICE_RESPONSE` (Instrucción para generar una respuesta vocal basada en la emoción del usuario).
  - `AGT_INTERUPTION_DETECTED` (Evento que indica que una interrupción se ha producido durante la conversación).

## Módulos relacionados:
- **Entrada desde:** `voz/` (procesamiento de audio, análisis de emociones vocales y transcripción del habla).
- **Salida hacia:** `voz/` (para generar una respuesta vocal apropiada), `interfaz/` (para generar una expresión visual asociada con el tono de voz).
- **Comunicación bidireccional con:** `agentes/` (para ajustar la modulación emocional basada en la voz).

## Dependencias técnicas:
- **Librerías externas:** `Vosk` o `Whisper` (para reconocimiento de voz), `pyttsx3` (para síntesis de voz), `webrtcvad` (para detección de actividad vocal).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos y gestión de la modulación emocional a través de la voz.

## Notas adicionales:
Este agente se especializa en procesar la entrada auditiva del usuario, permitiendo que NORA comprenda el tono emocional de la voz y reconozca interrupciones en el habla. A través del análisis de las características vocales, como el ritmo, el volumen y el tono, el agente evalúa el estado emocional del usuario y ajusta las respuestas del sistema en consecuencia. Este agente puede trabajar de forma conjunta con el `agente_visual` para generar respuestas multimodales que combinen las percepciones visuales y auditivas.

## Archivos previstos del módulo:
- `agente_auditivo.py`: Evaluación de voz, emociones acústicas, interrupciones (este archivo).
- Archivos adicionales de agentes como `agente_visual.py`, `agente_base.py`.
