# Ficha Funcional – `gestion_subcontextos.py`

## Nombre del archivo:
`gestion_subcontextos.py`

## Responsabilidad principal:
Gestionar conversaciones paralelas y subtemas activos dentro de la interacción de NORA. Este archivo se encarga de manejar múltiples subcontextos conversacionales, permitiendo que NORA pueda interactuar sobre varios temas al mismo tiempo sin perder la coherencia del diálogo principal. Facilita la creación de conversaciones más dinámicas y complejas, donde el sistema pueda mantener diversos hilos de diálogo activos simultáneamente.

## Entradas esperadas:
- **Tipo de entrada:** Texto de entrada del usuario, eventos de cambio de tema o subtema, contexto conversacional.
- **Fuente:** `dialogo_main.py` (para recibir el flujo principal de la conversación y los subtemas).
- **Formato o protocolo:** Texto plano, eventos de contexto conversacional, eventos internos (`EVT_...`).

## Salidas generadas:
- **Tipo de salida:** Creación o cambio de subcontextos, activación de nuevos temas o subtemas, eventos de gestión de subcontextos.
- **Destinatario:** `dialogo_main.py` (para gestionar el flujo de la conversación con subtemas).
- **Ejemplo de salida:**
  - `EVT_SUBCONTEXT_STARTED` (Evento que indica que se ha iniciado un nuevo subcontexto conversacional).
  - `CMD_SWITCH_SUBCONTEXT` (Instrucción para cambiar de un subcontexto a otro durante la conversación).
  - `AGT_SUBCONTEXT_UPDATED` (Confirmación de que el subcontexto ha sido actualizado correctamente).

## Módulos relacionados:
- **Entrada desde:** `dialogo_main.py` (para recibir cambios en el tema o subtema y actualizar el contexto de la conversación).
- **Salida hacia:** `dialogo_main.py` (para aplicar cambios en los subcontextos y coordinar el flujo del diálogo).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar el manejo de subcontextos y asegurar que la conversación principal y los subtemas sean coherentes.

## Dependencias técnicas:
- **Librerías externas:** `nltk`, `spacy` (para el procesamiento de texto y la detección de cambios de tema o subtema).
- **Hardware gestionado:** Ninguno directamente (se maneja la lógica de los subcontextos y el flujo conversacional a nivel de software).
- **Protocolos:** Comunicación basada en eventos internos, cambio y gestión de subcontextos durante la conversación.

## Notas adicionales:
Este archivo es clave para mejorar la capacidad de NORA de gestionar conversaciones complejas y dinámicas. Permite que NORA mantenga el contexto de varias conversaciones o temas activos, sin perder la coherencia del diálogo principal. Esto es esencial cuando el usuario cambia de tema durante la conversación o cuando NORA necesita gestionar múltiples hilos de diálogo relacionados entre sí, como en situaciones de preguntas y respuestas o de conversaciones multitarea.

## Archivos previstos del módulo:
- `gestion_subcontextos.py`: Manejo de conversaciones paralelas y subtemas activos (este archivo).
- Archivos adicionales como `dialogo_main.py`, `gestion_contexto.py`, `nlu.py`.
