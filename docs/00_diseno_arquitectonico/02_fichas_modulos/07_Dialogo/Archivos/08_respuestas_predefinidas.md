# Ficha Funcional – `respuestas_predefinidas.py`

## Nombre del archivo:
`respuestas_predefinidas.py`

## Responsabilidad principal:
Gestionar las plantillas de respuestas estructuradas y las respuestas de fallback dentro del sistema NORA. Este archivo se encarga de proporcionar respuestas estándar o predefinidas para situaciones comunes, como cuando el sistema no comprende la solicitud del usuario o no puede generar una respuesta dinámica. Además, maneja las respuestas de fallback cuando el sistema detecta confusión o ambigüedad.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de respuestas predefinidas, eventos de confusión o baja comprensión.
- **Fuente:** `dialogo_main.py` (para recibir el contexto de la interacción y detectar la necesidad de una respuesta predefinida), `sistema/` (para gestionar respuestas de emergencia).
- **Formato o protocolo:** Texto plano, eventos internos (`EVT_...`), respuestas predeterminadas en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Respuestas estándar, respuestas de fallback, eventos de respuesta predefinida.
- **Destinatario:** `voz/` (para generar la respuesta de voz a partir de la plantilla), `dialogo_main.py` (para manejar la respuesta generada y continuar con la interacción).
- **Ejemplo de salida:**
  - `"Lo siento, no entendí lo que dijiste. ¿Podrías repetirlo?"` (Respuesta de fallback).
  - `EVT_PREDEFINED_RESPONSE` (Evento que indica que una respuesta predefinida ha sido utilizada).
  - `CMD_USE_PREDEFINED_RESPONSE` (Instrucción para usar una respuesta predefinida en el flujo de la conversación).

## Módulos relacionados:
- **Entrada desde:** `dialogo_main.py` (para recibir solicitudes de respuestas predefinidas o de fallback), `sistema/` (para gestionar la situación de confusión o error).
- **Salida hacia:** `voz/` (para emitir la respuesta generada como voz), `dialogo_main.py` (para coordinar la interacción y el flujo de la conversación).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que las respuestas predefinidas sean coherentes con el contexto general y la interacción del sistema.

## Dependencias técnicas:
- **Librerías externas:** `json` (para almacenar y recuperar respuestas predefinidas en formato estructurado), `nltk`, `spacy` (para el análisis de texto y generación de respuestas estándar).
- **Hardware gestionado:** Ninguno directamente (gestiona respuestas a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, generación de respuestas estructuradas y fallback.

## Notas adicionales:
Este archivo es esencial para mejorar la robustez del sistema de conversación de NORA. Las respuestas predefinidas y de fallback permiten que el sistema mantenga una interacción fluida, incluso cuando no puede generar respuestas dinámicas o cuando se enfrenta a situaciones confusas. Al proporcionar respuestas estándar, **`respuestas_predefinidas.py`** mejora la accesibilidad del sistema y asegura que el usuario reciba siempre una respuesta, incluso si la interacción no es completamente comprendida.

## Archivos previstos del módulo:
- `respuestas_predefinidas.py`: Plantillas para respuestas estructuradas y fallback (este archivo).
- Archivos adicionales como `dialogo_main.py`, `nlg.py`, `manejo_incertidumbre.py`.
