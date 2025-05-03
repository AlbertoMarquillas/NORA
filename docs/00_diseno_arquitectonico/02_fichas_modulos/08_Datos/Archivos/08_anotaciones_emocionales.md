# Ficha Funcional – `anotaciones_emocionales.py`

## Nombre del archivo:
`anotaciones_emocionales.py`

## Responsabilidad principal:
Registrar y almacenar las emociones detectadas durante las interacciones con el usuario. Este archivo se encarga de anotar eventos emocionales relacionados con los momentos específicos de la conversación, asociando las emociones con las interacciones del usuario, para permitir una mejor comprensión emocional de la conversación y su posterior análisis.

## Entradas esperadas:
- **Tipo de entrada:** Datos de emociones detectadas, texto asociado a momentos emocionales, eventos emocionales durante la interacción.
- **Fuente:** `emocion_audio.py` (para obtener las emociones detectadas en la voz del usuario), `dialogo_main.py` (para registrar eventos emocionales durante la conversación).
- **Formato o protocolo:** Eventos emocionales (`EVT_EMOTION_DETECTED`), datos en formato JSON o texto estructurado, parámetros emocionales.

## Salidas generadas:
- **Tipo de salida:** Confirmaciones de almacenamiento de emociones, eventos relacionados con emociones registradas.
- **Destinatario:** `sistema/`, `agentes/`, `dialogo/` (para utilizar los datos emocionales en el contexto de la conversación o para análisis).
- **Ejemplo de salida:**
  - `EVT_EMOTION_SAVED` (Evento que indica que una emoción ha sido registrada exitosamente).
  - `AGT_EMOTION_LOGGED` (Confirmación de que la emoción ha sido registrada y almacenada).
  - `EVT_EMOTION_RETRIEVED` (Evento que indica que las emociones registradas han sido recuperadas para su uso).

## Módulos relacionados:
- **Entrada desde:** `emocion_audio.py` (para recibir las emociones detectadas en el habla del usuario), `dialogo_main.py` (para asociar las emociones a momentos específicos de la conversación).
- **Salida hacia:** `sistema/`, `agentes/`, `dialogo/` (para proporcionar los datos emocionales y su análisis en el contexto de la interacción).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar el uso de las emociones registradas y asegurar que el sistema responde apropiadamente a las emociones del usuario.

## Dependencias técnicas:
- **Librerías externas:** `json` (para almacenar y recuperar los datos emocionales), `sqlite3` o `SQLAlchemy` (para persistencia en bases de datos locales).
- **Hardware gestionado:** Almacenamiento local (SSD/HDD) para persistencia de anotaciones emocionales.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos estructurados sobre las emociones.

## Notas adicionales:
Este archivo es fundamental para permitir que NORA reconozca y responda adecuadamente a las emociones del usuario. Al registrar las emociones asociadas con interacciones pasadas, **`anotaciones_emocionales.py`** ayuda a personalizar las respuestas y a hacer que NORA sea más empática, creando una experiencia más rica y dinámica. Además, la capacidad de recuperar las emociones registradas durante las interacciones permite mejorar la coherencia de las respuestas en futuras conversaciones.

## Archivos previstos del módulo:
- `anotaciones_emocionales.py`: Registro de emociones detectadas asociadas a momentos de interacción (este archivo).
- Archivos adicionales como `emocion_audio.py`, `dialogo_main.py`, `gestión_emocional.py`.
