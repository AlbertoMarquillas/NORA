# Ficha Funcional – `nlu.py`

## Nombre del archivo:
`nlu.py`

## Responsabilidad principal:
Gestionar el procesamiento de lenguaje natural (NLU) para interpretar la intención del usuario, extraer entidades y analizar el sentimiento en el texto recibido. Este archivo se encarga de convertir el texto hablado o escrito en datos estructurados que NORA pueda comprender y utilizar para generar respuestas contextuales apropiadas.

## Entradas esperadas:
- **Tipo de entrada:** Texto recibido desde el reconocimiento de voz (ASR), eventos emocionales, contexto de interacción.
- **Fuente:** `voz/` (texto transcrito), `dialogo_main.py` (para recibir la interacción en curso).
- **Formato o protocolo:** Texto plano, eventos internos (`EVT_...`), datos semánticos y emocionales.

## Salidas generadas:
- **Tipo de salida:** Intenciones identificadas, entidades extraídas, análisis de sentimiento.
- **Destinatario:** `dialogo_main.py` (para generar respuestas contextuales basadas en las intenciones y entidades extraídas).
- **Ejemplo de salida:**
  - `EVT_INTENT_DETECTED` (Evento que indica que una intención ha sido detectada).
  - `EVT_ENTITIES_EXTRACTED` (Evento que indica que las entidades han sido extraídas correctamente).
  - `AGT_INTENT_CONFIRMED` (Confirmación de que la intención ha sido correctamente interpretada).

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir texto transcrito desde el reconocimiento de voz), `dialogo_main.py` (para procesar el texto y el contexto de la conversación).
- **Salida hacia:** `dialogo_main.py` (para enviar la interpretación de las intenciones y entidades).
- **Comunicación bidireccional con:** `agentes/` (para ajustar la respuesta de acuerdo con las intenciones y el sentimiento detectado).

## Dependencias técnicas:
- **Librerías externas:** `transformers` (para la clasificación de intenciones y entidades utilizando modelos de NLP), `sentence-transformers` (para la comparación semántica), `nltk`, `spacy` (para el procesamiento de texto y extracción de entidades).
- **Hardware gestionado:** Ninguno directamente (se maneja a nivel lógico el procesamiento del lenguaje natural).
- **Protocolos:** Comunicación basada en eventos internos, procesamiento de texto estructurado.

## Notas adicionales:
Este archivo es fundamental para permitir que NORA entienda las intenciones del usuario, extraiga información relevante (como nombres, fechas, objetos) y analice el sentimiento del texto para modular sus respuestas. Gracias a la integración de modelos avanzados de NLP, **`nlu.py`** asegura que las respuestas de NORA sean contextuales y adecuadas, haciendo que la interacción sea más fluida y humana.

## Archivos previstos del módulo:
- `nlu.py`: Análisis de intención, entidades y sentimiento en el texto recibido (este archivo).
- Archivos adicionales como `dialogo_main.py`, `nlg.py`, `gestion_contexto.py`.
