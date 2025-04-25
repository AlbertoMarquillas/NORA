# Ficha Funcional – `memoria_conversacional.py`

## Nombre del archivo:
`memoria_conversacional.py`

## Responsabilidad principal:
Gestionar la persistencia de información relevante durante la sesión de conversación, permitiendo a NORA recordar y utilizar datos del contexto, interacciones pasadas y preferencias del usuario. Este archivo se encarga de almacenar y recuperar información relevante durante el diálogo, como nombres, lugares, temas discutidos y detalles importantes que mejoran la continuidad y la coherencia de las interacciones.

## Entradas esperadas:
- **Tipo de entrada:** Información relevante de la conversación, detalles del usuario, eventos de contexto.
- **Fuente:** `dialogo_main.py` (para recibir los datos generados durante la conversación), `nlu.py` (para extraer entidades relevantes que deben ser almacenadas).
- **Formato o protocolo:** Texto estructurado, eventos de contexto conversacional.

## Salidas generadas:
- **Tipo de salida:** Recuperación de datos conversacionales previos, actualización del contexto de la conversación.
- **Destinatario:** `dialogo_main.py` (para aplicar la memoria conversacional en el flujo de diálogo), `sistema/` (para actualizar el contexto del sistema con la información almacenada).
- **Ejemplo de salida:**
  - `EVT_MEMORY_RETRIEVED` (Evento que indica que se ha recuperado información relevante de la memoria conversacional).
  - `CMD_UPDATE_CONVERSATION_MEMORY` (Instrucción para almacenar nueva información en la memoria conversacional).
  - `AGT_MEMORY_SAVED` (Confirmación de que la información ha sido correctamente almacenada en la memoria).

## Módulos relacionados:
- **Entrada desde:** `dialogo_main.py` (para recibir datos del diálogo y contexto que deben ser almacenados), `nlu.py` (para extraer entidades clave).
- **Salida hacia:** `dialogo_main.py` (para gestionar el contexto de la conversación utilizando la memoria conversacional), `sistema/` (para integrar los datos almacenados en la interacción general).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que la memoria conversacional esté alineada con las interacciones globales y que los datos se utilicen eficazmente.

## Dependencias técnicas:
- **Librerías externas:** `json` (para almacenar y recuperar datos en un formato estructurado), `sqlite` o `pickle` (para persistencia de datos durante la sesión).
- **Hardware gestionado:** Ninguno directamente (se maneja la memoria a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, almacenamiento y recuperación de datos conversacionales.

## Notas adicionales:
Este archivo es esencial para hacer que NORA mantenga una conversación coherente y fluida a lo largo del tiempo. La memoria conversacional permite que NORA recuerde información clave de interacciones pasadas, lo que le permite continuar conversaciones en varios turnos sin perder contexto, haciendo la interacción más natural. La capacidad de recordar detalles importantes también ayuda a personalizar las respuestas y mejorar la experiencia del usuario.

## Archivos previstos del módulo:
- `memoria_conversacional.py`: Persistencia de información relevante durante la sesión (este archivo).
- Archivos adicionales como `dialogo_main.py`, `gestion_contexto.py`, `nlu.py`.
