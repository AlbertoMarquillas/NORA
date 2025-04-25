# Ficha Funcional – `adaptacion_emocional.py`

## Nombre del archivo:
`adaptacion_emocional.py`

## Responsabilidad principal:
Ajustar las respuestas generadas por NORA según el estado emocional detectado, asegurando que las interacciones sean más empáticas y naturales. Este archivo se encarga de modificar el tono, el contenido y el estilo de las respuestas en función de las emociones del usuario, detectadas a través de su voz o el contexto de la conversación, para generar una experiencia más personalizada y emocionalmente inteligente.

## Entradas esperadas:
- **Tipo de entrada:** Eventos emocionales (determinados por el análisis de voz o el contexto), texto generado.
- **Fuente:** `emocion_audio.py` (para recibir datos sobre el tono emocional de la voz), `dialogo_main.py` (para obtener el contexto de la interacción y los eventos emocionales).
- **Formato o protocolo:** Eventos emocionales (`EVT_EMOTION_CHANGED`), texto transcrito, configuraciones emocionales en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Texto ajustado emocionalmente, instrucciones de modulación del tono de voz.
- **Destinatario:** `dialogo_main.py` (para ajustar la respuesta según la emoción detectada), `voz/` (para modificar la modulación de la voz sintetizada).
- **Ejemplo de salida:**
  - `EVT_EMOTIONAL_ADJUSTMENT` (Evento que indica que la respuesta ha sido ajustada emocionalmente).
  - `CMD_ADJUST_RESPONSE_TONE` (Instrucción para ajustar el tono de la respuesta según el estado emocional del usuario).
  - `AGT_EMOTIONAL_TONE_ADJUSTED` (Confirmación de que la modulación emocional se ha aplicado correctamente).

## Módulos relacionados:
- **Entrada desde:** `emocion_audio.py` (para detectar el estado emocional de la voz del usuario), `dialogo_main.py` (para recibir el texto generado y decidir cómo ajustarlo emocionalmente).
- **Salida hacia:** `dialogo_main.py` (para aplicar los ajustes emocionales en la respuesta generada), `voz/` (para aplicar la modulación emocional en la síntesis de voz).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar la modulación emocional y el tono de la interacción.

## Dependencias técnicas:
- **Librerías externas:** `transformers` (para analizar el texto y generar respuestas adecuadas emocionalmente), `nltk`, `spacy` (para el procesamiento de texto).
- **Hardware gestionado:** Ninguno directamente (se maneja el ajuste emocional a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, análisis y ajuste emocional de las respuestas.

## Notas adicionales:
Este archivo es esencial para hacer que NORA sea más empática y sensible a las emociones del usuario. Gracias a **`adaptacion_emocional.py`**, NORA puede modificar sus respuestas en tiempo real, adaptándose al tono emocional del usuario, haciendo que la interacción sea más humana y natural. Esta modulación emocional asegura que NORA no solo responda a las palabras, sino también a las emociones que subyacen a esas palabras, lo que enriquece la experiencia del usuario.

## Archivos previstos del módulo:
- `adaptacion_emocional.py`: Ajuste de respuestas en función del estado emocional detectado (este archivo).
- Archivos adicionales como `dialogo_main.py`, `nlg.py`, `emocion_audio.py`.
