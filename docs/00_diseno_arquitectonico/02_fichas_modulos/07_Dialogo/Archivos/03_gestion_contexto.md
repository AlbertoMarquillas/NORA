# Ficha Funcional – `gestion_contexto.py`

## Nombre del archivo:
`gestion_contexto.py`

## Responsabilidad principal:
Gestionar el estado conversacional y el seguimiento de los turnos de conversación en NORA. Este archivo se encarga de mantener el contexto de la interacción, guardando información relevante sobre el diálogo, las intenciones previas, las entidades extraídas y el estado emocional del usuario, para garantizar respuestas coherentes y relevantes a lo largo de la conversación.

## Entradas esperadas:
- **Tipo de entrada:** Texto reconocido, eventos emocionales, contexto de interacción, intenciones y entidades extraídas.
- **Fuente:** `nlu.py` (para recibir intenciones y entidades), `dialogo_main.py` (para gestionar el contexto de la conversación).
- **Formato o protocolo:** Texto plano, eventos internos (`EVT_...`), datos del estado conversacional.

## Salidas generadas:
- **Tipo de salida:** Estado conversacional actualizado, información sobre el turno de conversación, eventos de cambio de contexto.
- **Destinatario:** `dialogo_main.py` (para gestionar el flujo del diálogo con el contexto actualizado).
- **Ejemplo de salida:**
  - `EVT_CONTEXT_UPDATED` (Evento que indica que el contexto de la conversación ha sido actualizado).
  - `CMD_UPDATE_CONVERSATION_STATE` (Instrucción para actualizar el estado conversacional con nueva información).
  - `AGT_CONTEXT_SAVED` (Confirmación de que el contexto ha sido guardado correctamente).

## Módulos relacionados:
- **Entrada desde:** `nlu.py` (para recibir intenciones y entidades), `dialogo_main.py` (para actualizar el estado conversacional y gestionar los turnos de diálogo).
- **Salida hacia:** `dialogo_main.py` (para proporcionar el contexto actualizado y asegurar que la conversación continúe de manera coherente).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que el contexto de la conversación esté alineado con las acciones y estados del sistema.

## Dependencias técnicas:
- **Librerías externas:** `json` (para almacenar y cargar el estado conversacional), `spacy`, `nltk` (para el procesamiento de texto y la extracción de entidades).
- **Hardware gestionado:** Ninguno directamente (gestiona el contexto de la conversación a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, almacenamiento y recuperación de contexto conversacional.

## Notas adicionales:
Este archivo es esencial para garantizar que NORA pueda llevar una conversación coherente a lo largo de múltiples turnos. El seguimiento del contexto asegura que el sistema recuerde información relevante entre interacciones, lo que mejora la fluidez y la naturalidad del diálogo. Además, el manejo adecuado del turno conversacional permite a NORA interactuar de manera efectiva, sabiendo cuándo debe escuchar y cuándo debe responder.

## Archivos previstos del módulo:
- `gestion_contexto.py`: Mantenimiento del estado conversacional y seguimiento de turnos (este archivo).
- Archivos adicionales como `dialogo_main.py`, `nlu.py`, `nlg.py`.
