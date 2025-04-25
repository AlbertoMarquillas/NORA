# Ficha Específica – `parser_comandos.py`

## Nombre del archivo:
`parser_comandos.py`

## Responsabilidad principal:
Analizar el texto transcrito obtenido del ASR para extraer comandos estructurados que el sistema NORA pueda interpretar y ejecutar.

## Entradas esperadas:
- Texto plano transcrito por el módulo ASR.
- Configuraciones dinámicas (listas de comandos válidos, sinónimos, sensibilidad semántica).

## Salidas generadas:
- Estructura de comando interpretado (acción, objeto, parámetros).
- Eventos asociados:
  - `EVT_COMMAND_PARSED`

## Funcionalidades principales:
- Preprocesamiento del texto (normalización, limpieza de ruido lingüístico).
- Búsqueda de patrones, palabras clave o frases definidas.
- Extracción de intenciones (intents) y entidades relevantes.
- Generación de estructuras JSON representando los comandos extraídos.
- Emisión de eventos internos con los comandos interpretados.

## Dependencias técnicas:
- `re` – Expresiones regulares para búsqueda de patrones.
- `nltk`, `spacy` (opcional) – Procesamiento de lenguaje natural ligero.
- `json` – Formateo estructurado de resultados.

