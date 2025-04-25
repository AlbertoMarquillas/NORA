# Ficha Funcional – `correccion_asr.py`

## Nombre del archivo:
`correccion_asr.py`

## Responsabilidad principal:
Gestionar la corrección automática de errores comunes de transcripción de voz, mejorando la precisión del reconocimiento automático del habla (ASR). Este archivo se encarga de identificar y corregir palabras o frases mal transcritas o mal interpretadas por el sistema, utilizando técnicas de procesamiento de lenguaje natural para validar y ajustar el texto generado por el ASR.

## Entradas esperadas:
- **Tipo de entrada:** Texto transcrito del ASR, eventos de error o baja precisión en la transcripción.
- **Fuente:** `asr.py` (para recibir las transcripciones de audio).
- **Formato o protocolo:** Texto transcrito en formato plano, eventos de error o corrección.

## Salidas generadas:
- **Tipo de salida:** Texto corregido, eventos de corrección de ASR.
- **Destinatario:** `dialogo_main.py` (para enviar el texto corregido y continuar el flujo de la conversación).
- **Ejemplo de salida:**
  - `EVT_ASR_CORRECTION` (Evento que indica que la transcripción ha sido corregida).
  - `CMD_USE_CORRECTED_TEXT` (Instrucción para usar el texto corregido en el flujo de la conversación).
  - `AGT_TEXT_CORRECTED` (Confirmación de que el texto ha sido corregido y validado).

## Módulos relacionados:
- **Entrada desde:** `asr.py` (para recibir las transcripciones y realizar las correcciones necesarias).
- **Salida hacia:** `dialogo_main.py` (para aplicar el texto corregido y continuar el diálogo).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que la corrección de ASR sea coherente con las interacciones y las respuestas generadas.

## Dependencias técnicas:
- **Librerías externas:** `nltk`, `spacy` (para el procesamiento del lenguaje natural y la corrección de errores), `editdistance` (para calcular la distancia de edición y sugerir correcciones).
- **Hardware gestionado:** Ninguno directamente (se maneja la corrección de texto a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, análisis de errores de transcripción y corrección del texto.

## Notas adicionales:
Este archivo es esencial para garantizar que NORA pueda manejar los errores comunes en el proceso de reconocimiento de voz (ASR). Aunque los sistemas ASR son avanzados, aún pueden cometer errores en situaciones ruidosas o cuando las palabras se pronuncian de manera ambigua. **`correccion_asr.py`** asegura que NORA pueda corregir estos errores de manera automática, manteniendo la precisión de la transcripción y evitando malentendidos en la conversación.

## Archivos previstos del módulo:
- `correccion_asr.py`: Corrección automática de errores comunes de transcripción de voz (este archivo).
- Archivos adicionales como `asr.py`, `dialogo_main.py`, `nlu.py`.
