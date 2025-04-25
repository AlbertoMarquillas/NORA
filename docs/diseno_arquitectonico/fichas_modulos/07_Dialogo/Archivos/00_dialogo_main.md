# Ficha Funcional – `dialogo_main.py`

## Nombre del archivo:
`dialogo_main.py`

## Responsabilidad principal:
Gestionar el flujo general de la conversación dentro de NORA, coordinando el procesamiento de entrada y salida de texto. Este archivo es el orquestador del módulo de diálogo, gestionando la interacción entre el reconocimiento de voz, la generación de respuestas y el mantenimiento del contexto conversacional. Se encarga de que las respuestas sean generadas dinámicamente, manteniendo coherencia en el diálogo y ajustándolas según el contexto emocional y la interacción previa.

## Entradas esperadas:
- **Tipo de entrada:** Texto reconocido, eventos emocionales, contexto de interacción, comandos.
- **Fuente:** `voz/` (para recibir texto transcrito), `agentes/` (para obtener modulaciones emocionales), `sistema/` (para gestionar el estado general del sistema).
- **Formato o protocolo:** Texto plano, eventos internos (`EVT_...`), estado conversacional, datos de contexto.

## Salidas generadas:
- **Tipo de salida:** Texto generado para síntesis de voz (TTS), comandos contextuales para otras partes del sistema, eventos de interacción conversacional.
- **Destinatario:** `voz/` (para generar la salida de voz), `sistema/` (para gestionar el flujo conversacional y el contexto).
- **Ejemplo de salida:**
  - Respuesta textual: `"Claro, ¿qué más necesitas?"`.
  - `EVT_DIALOGUE_RESPONSE` (Evento que indica que una respuesta ha sido generada).
  - `EVT_DIALOGUE_CONFUSION` (Evento que indica que se ha detectado confusión en la interpretación de la intención del usuario).

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir texto reconocido de la voz del usuario), `agentes/` (para ajustar el tono y la emoción de la respuesta), `sistema/` (para recibir el estado y contexto general).
- **Salida hacia:** `voz/` (para enviar la respuesta generada a través de TTS), `sistema/` (para actualizar el estado conversacional y gestionar el flujo del diálogo).
- **Comunicación bidireccional con:** `agentes/` (para ajustar las respuestas de acuerdo con la emoción detectada y el contexto conversacional).

## Dependencias técnicas:
- **Librerías externas:** `transformers` (para generación de respuestas en lenguaje natural), `sentence-transformers` (para análisis de similitud semántica), `nltk`, `spacy` (para procesamiento de lenguaje natural).
- **Hardware gestionado:** Ninguno directamente (se maneja el flujo de texto a nivel lógico).
- **Protocolos:** Eventos internos para gestionar el flujo de la conversación, flujo de texto estructurado.

## Notas adicionales:
Este archivo es el corazón del módulo de diálogo de NORA. Gestiona la interacción entre el usuario y el sistema, asegurando que las respuestas sean generadas de manera coherente y contextual. Además, coordina la adaptación de las respuestas emocionales, ajustando el tono y el contenido en función de las emociones detectadas y del contexto en curso. `dialogo_main.py` también maneja casos de confusión y ambigüedad en las respuestas, garantizando una interacción fluida y eficiente.

## Archivos previstos del módulo:
- `dialogo_main.py`: Coordinador general del flujo de conversación (este archivo).
- Archivos adicionales como `nlu.py`, `nlg.py`, `gestion_contexto.py`, `adaptacion_emocional.py`.
