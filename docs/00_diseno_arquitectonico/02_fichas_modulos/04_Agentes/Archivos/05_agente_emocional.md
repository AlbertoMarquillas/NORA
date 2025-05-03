# Ficha Funcional – `agente_emocional.py`

## Nombre del archivo:
`agente_emocional.py`

## Responsabilidad principal:
Gestionar la modulación emocional del sistema NORA, evaluando eventos relacionados con las emociones del usuario, tanto a través de entradas visuales como auditivas. Este agente ajusta las respuestas del sistema basándose en el estado emocional del usuario, proporcionando respuestas más empáticas y adaptadas al contexto emocional del momento.

## Entradas esperadas:
- **Tipo de entrada:** Eventos emocionales derivados de la voz y las expresiones faciales, análisis de tono vocal y emociones visuales.
- **Fuente:** Módulos `voz/` (análisis emocional vocal), `vision/` (análisis de emociones faciales).
- **Formato o protocolo:** Eventos emocionales (`EVT_EMOTION_VOICE_HAPPY`, `EVT_EMOTION_FACE_SAD`), eventos internos que describen el estado emocional.

## Salidas generadas:
- **Tipo de salida:** Modulación emocional del sistema, ajustes en el tono de voz, expresión visual y respuestas verbales.
- **Destinatario:** `voz/` (para generar una respuesta emocional vocal), `interfaz/` (para generar una respuesta visual adaptada).
- **Ejemplo de salida:**
  - `AGT_EMOTIONAL_MODULATION` (Modulación emocional del sistema en función de la entrada emocional).
  - `CMD_EMOTIONAL_TONE` (Instrucción para ajustar el tono de la respuesta vocal según el estado emocional).
  - `CMD_EXPRESSION_ADJUSTMENT` (Ajuste de la expresión visual del sistema basado en las emociones detectadas).

## Módulos relacionados:
- **Entrada desde:** `voz/` (análisis emocional vocal), `vision/` (análisis de emociones faciales).
- **Salida hacia:** `voz/` (para generar una respuesta emocional vocal), `interfaz/` (para actualizar la expresión visual de NORA).
- **Comunicación bidireccional con:** `agentes/`, `sistema/` (para ajustar la respuesta global y asegurar coherencia emocional).

## Dependencias técnicas:
- **Librerías externas:** `TensorFlow` o `PyTorch` (para modelos de análisis emocional), `dlib` o `face_recognition` (para detección de emociones faciales).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, modulación emocional mediante procesamiento de datos emocionales.

## Notas adicionales:
Este agente se centra en interpretar y reaccionar al estado emocional del usuario, utilizando tanto los datos visuales como auditivos. Su función es hacer que el sistema NORA sea más empático y adaptativo, proporcionando respuestas que estén alineadas con las emociones del usuario. A través de la interacción con otros agentes, como los agentes de visión y de voz, el `agente_emocional` puede generar respuestas multimodales que no solo responden de manera lógica, sino también emocionalmente coherente.

## Archivos previstos del módulo:
- `agente_emocional.py`: Modulación de expresividad basada en estado emocional detectado (este archivo).
- Archivos adicionales de agentes como `agente_visual.py`, `agente_base.py`.
