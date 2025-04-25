# Ficha Específica – `normalizacion_texto.py`

## Nombre del archivo:
`normalizacion_texto.py`

## Responsabilidad principal:
Preprocesar y normalizar los textos obtenidos por el ASR antes de su análisis o síntesis, mejorando la calidad de los comandos interpretados y la naturalidad de las respuestas generadas.

## Entradas esperadas:
- Texto transcrito procedente del reconocimiento automático de voz.
- Opcionalmente, configuraciones de reglas específicas de normalización.

## Salidas generadas:
- Texto limpio, corregido y estructurado.
- Texto adaptado fonéticamente para la síntesis TTS si es necesario.

## Funcionalidades principales:
- Corrección básica de errores de transcripción (palabras repetidas, artefactos).
- Expansión de abreviaturas o formas contraídas.
- Normalización de números, fechas y expresiones temporales.
- Adaptación del texto a una forma más adecuada para su posterior síntesis (prosodia).
- Opcionalmente, detección de intenciones muy básicas mediante patrones lingüísticos.

## Dependencias técnicas:
- `re` – Expresiones regulares para manipulación de texto.
- `nltk`, `spacy` (opcional) – Análisis lingüístico ligero.
- `json` – Aplicación de reglas de normalización configurables.

