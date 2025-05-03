# Ficha Funcional – `manejo_incertidumbre.py`

## Nombre del archivo:
`manejo_incertidumbre.py`

## Responsabilidad principal:
Gestionar las situaciones de baja comprensión o ambigüedad en el diálogo de NORA. Este archivo se encarga de identificar cuando el sistema no puede interpretar correctamente una solicitud del usuario, y proporciona mecanismos para manejar la incertidumbre, como pedir aclaraciones, ofrecer opciones o proporcionar respuestas estándar para situaciones ambiguas.

## Entradas esperadas:
- **Tipo de entrada:** Texto incompleto o ambiguo, eventos de confusión o falta de comprensión, respuestas no interpretadas correctamente.
- **Fuente:** `nlu.py` (para recibir intenciones y entidades que no han sido completamente entendidas), `dialogo_main.py` (para gestionar situaciones de ambigüedad o falta de respuesta clara).
- **Formato o protocolo:** Texto plano, eventos internos de confusión (`EVT_DIALOGUE_CONFUSION`), datos de interacción incompleta.

## Salidas generadas:
- **Tipo de salida:** Respuestas de aclaración o confirmación, eventos de ambigüedad.
- **Destinatario:** `dialogo_main.py` (para generar respuestas que gestionen la incertidumbre).
- **Ejemplo de salida:**
  - `"Lo siento, no he entendido lo que dijiste. ¿Podrías repetirlo?"` (Respuesta de aclaración).
  - `EVT_UNCERTAINTY_HANDLED` (Evento que indica que la ambigüedad ha sido manejada correctamente).
  - `CMD_REQUEST_CLARIFICATION` (Instrucción para solicitar más información al usuario).

## Módulos relacionados:
- **Entrada desde:** `nlu.py` (para detectar intenciones y entidades ambiguas o mal interpretadas), `dialogo_main.py` (para gestionar el flujo conversacional y determinar cuándo se presenta incertidumbre).
- **Salida hacia:** `dialogo_main.py` (para generar la respuesta adecuada a la ambigüedad), `voz/` (para emitir la respuesta de aclaración).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar la gestión de la incertidumbre y asegurar que NORA mantenga coherencia en la conversación.

## Dependencias técnicas:
- **Librerías externas:** `nltk`, `spacy` (para el análisis de texto y la detección de ambigüedad o error en el procesamiento del lenguaje natural).
- **Hardware gestionado:** Ninguno directamente (se maneja el análisis de texto y la gestión de incertidumbre a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, detección de ambigüedad en el texto y el contexto de la conversación.

## Notas adicionales:
Este archivo es fundamental para garantizar que NORA pueda gestionar situaciones en las que el sistema no comprende completamente lo que el usuario está pidiendo. Gracias a **`manejo_incertidumbre.py`**, el sistema puede manejar la incertidumbre de forma elegante, pidiendo aclaraciones cuando sea necesario, lo que mejora la experiencia del usuario y evita respuestas erróneas o desconcertantes.

## Archivos previstos del módulo:
- `manejo_incertidumbre.py`: Gestión de situaciones de baja comprensión o ambigüedad (este archivo).
- Archivos adicionales como `dialogo_main.py`, `nlu.py`, `gestion_contexto.py`.
