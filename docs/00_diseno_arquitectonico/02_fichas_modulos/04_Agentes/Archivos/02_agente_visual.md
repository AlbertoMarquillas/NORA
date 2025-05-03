# Ficha Funcional – `agente_visual.py`

## Nombre del archivo:
`agente_visual.py`

## Responsabilidad principal:
Gestionar la percepción visual del sistema NORA, evaluando eventos relacionados con la atención visual del usuario, el análisis de emociones faciales y los gestos. Este agente toma decisiones basadas en las entradas visuales y modula las respuestas del sistema según el estado emocional o la atención del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de detección visual, análisis de imágenes, eventos de gestos y emociones faciales.
- **Fuente:** Módulo `vision/`, que proporciona información sobre la detección de rostros, posturas, gestos y emociones visuales.
- **Formato o protocolo:** Eventos de percepción (`EVT_FACE_DETECTED`, `EVT_EMOTION_CHANGED`, `EVT_GESTURE_RECOGNIZED`).

## Salidas generadas:
- **Tipo de salida:** Decisiones contextuales sobre la atención del usuario, respuestas emocionales basadas en la detección facial, activación de cambios en el comportamiento del sistema.
- **Destinatario:** `interfaz/`, `voz/`, `sistema/` (para realizar cambios en la expresión visual y respuestas emocionales).
- **Ejemplo de salida:**
  - `AGT_ATTENTION_GAINED` (Evento que indica que el usuario está prestando atención).
  - `AGT_EMOTION_RECOGNIZED` (Evento relacionado con la emoción detectada del usuario).
  - `CMD_UPDATE_VISUALS` (Instrucción para modificar la expresión visual del sistema).

## Módulos relacionados:
- **Entrada desde:** `vision/` (detección de rostros, emociones faciales y gestos).
- **Salida hacia:** `interfaz/` (actualización de expresiones visuales y animaciones en la pantalla).
- **Comunicación bidireccional con:** `agentes/` (para tomar decisiones basadas en las entradas visuales).

## Dependencias técnicas:
- **Librerías externas:** `MediaPipe` (para estimación de poses y detección facial), `OpenCV` (para procesamiento de imágenes).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos y gestión de estados emocionales a través de eventos internos.

## Notas adicionales:
Este agente está diseñado para procesar la entrada visual en tiempo real y reaccionar de manera dinámica a las interacciones del usuario. A través de eventos de percepción visual, el agente puede determinar si el usuario está prestando atención, detectar emociones faciales y reconocer gestos, lo que le permite generar respuestas emocionales o de interacción visual en función de esa información. Este agente también puede trabajar de forma conjunta con otros agentes para generar respuestas multimodales que combinan la percepción visual y auditiva.

## Archivos previstos del módulo:
- `agente_visual.py`: Evaluación de atención, emociones y gestos visuales (este archivo).
- Archivos adicionales de agentes como `agente_auditivo.py`, `agente_base.py`.
