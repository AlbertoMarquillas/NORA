# Ficha Funcional – `nlg.py`

## Nombre del archivo:
`nlg.py`

## Responsabilidad principal:
Gestionar la generación de lenguaje natural (NLG) para producir respuestas contextuales a partir de la información procesada. Este archivo se encarga de tomar las intenciones, entidades y contexto de la conversación y generar texto coherente y natural que NORA pueda utilizar para interactuar con el usuario, adaptando las respuestas según el estado emocional, el contexto y el tono de la interacción.

## Entradas esperadas:
- **Tipo de entrada:** Intenciones del usuario, entidades extraídas, contexto de interacción, análisis emocional.
- **Fuente:** `nlu.py` (para recibir intenciones y entidades), `dialogo_main.py` (para recibir el contexto y la situación emocional).
- **Formato o protocolo:** Texto estructurado (intenciones, entidades), datos emocionales (sentimiento, tono), eventos internos.

## Salidas generadas:
- **Tipo de salida:** Texto generado para la respuesta, comandos contextuales.
- **Destinatario:** `voz/` (para sintetizar la respuesta en audio), `sistema/`, `interfaz/` (para gestionar la salida del diálogo).
- **Ejemplo de salida:**
  - `"Ahora mismo te lo digo."` (Texto generado como respuesta).
  - `EVT_DIALOGUE_RESPONSE` (Evento que indica que una respuesta ha sido generada y está lista para ser emitida).
  - `AGT_RESPONSE_GENERATED` (Confirmación de que la respuesta ha sido generada correctamente).

## Módulos relacionados:
- **Entrada desde:** `nlu.py` (para recibir las intenciones y entidades del usuario), `dialogo_main.py` (para procesar el contexto de la conversación y el estado emocional).
- **Salida hacia:** `voz/` (para convertir el texto generado en voz), `interfaz/`, `sistema/` (para manejar el diálogo y la respuesta de forma coherente).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` (para ajustar la respuesta según el contexto emocional o la necesidad de personalización de la respuesta).

## Dependencias técnicas:
- **Librerías externas:** `transformers` (para la generación de texto en lenguaje natural), `nltk`, `spacy` (para el procesamiento del lenguaje natural), `openai` (si se usa GPT u otros modelos de lenguaje).
- **Hardware gestionado:** Ninguno directamente (se maneja el flujo de texto a nivel lógico).
- **Protocolos:** Eventos internos para gestionar la generación de respuestas y el control del flujo conversacional.

## Notas adicionales:
Este archivo es esencial para generar respuestas naturales y contextuales, transformando la interpretación de las intenciones y entidades del usuario en un texto coherente y adecuado. **`nlg.py`** permite que NORA produzca respuestas que se ajusten al tono y contexto de la conversación, haciendo la interacción más fluida y adaptativa. La capacidad de personalizar las respuestas en función del estado emocional del usuario y el contexto general de la conversación es clave para mejorar la experiencia del usuario.

## Archivos previstos del módulo:
- `nlg.py`: Generación de lenguaje natural adaptado al contexto (este archivo).
- Archivos adicionales como `dialogo_main.py`, `nlu.py`, `gestion_contexto.py`.
