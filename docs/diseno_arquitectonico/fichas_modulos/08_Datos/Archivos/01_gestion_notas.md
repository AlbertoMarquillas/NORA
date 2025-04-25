# Ficha Funcional – `gestion_notas.py`

## Nombre del archivo:
`gestion_notas.py`

## Responsabilidad principal:
Gestionar el almacenamiento y la consulta de notas dictadas o creadas por el usuario. Este archivo permite que NORA guarde notas relevantes, recordatorios o cualquier otro tipo de información textual proporcionada por el usuario durante la interacción. También permite acceder a estas notas cuando sea necesario, facilitando la consulta rápida y la actualización de las mismas.

## Entradas esperadas:
- **Tipo de entrada:** Texto de nota, solicitudes de recuperación de notas.
- **Fuente:** `voz/` (para recibir notas dictadas por el usuario), `dialogo/` (para interactuar con las notas guardadas).
- **Formato o protocolo:** Texto plano, eventos internos (`CMD_...`, `EVT_...`), estructuras JSON para guardar y recuperar las notas.

## Salidas generadas:
- **Tipo de salida:** Confirmaciones de guardado de notas, notas solicitadas, eventos de recuperación.
- **Destinatario:** `dialogo/`, `sistema/`, `agentes/` (para enviar las notas recuperadas o nuevas al sistema).
- **Ejemplo de salida:**
  - `EVT_NOTE_SAVED` (Evento que indica que la nota ha sido guardada exitosamente).
  - `EVT_NOTE_RETRIEVED` (Evento que indica que la nota ha sido recuperada correctamente).
  - Notas de rutina recuperadas para la activación de recordatorios.

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir las notas dictadas por el usuario), `dialogo/` (para gestionar las consultas de notas durante la interacción).
- **Salida hacia:** `dialogo/`, `sistema/`, `agentes/` (para proporcionar las notas almacenadas durante la interacción).
- **Comunicación bidireccional con:** `sistema/` y `agentes/` para garantizar que las notas guardadas estén disponibles para otros módulos que las necesiten, como recordatorios o interacciones personalizadas.

## Dependencias técnicas:
- **Librerías externas:** `json` (para almacenar y recuperar las notas en formato estructurado), `sqlite3` o `SQLAlchemy` (para la persistencia en bases de datos locales si se necesita almacenamiento más robusto).
- **Hardware gestionado:** Almacenamiento local USB (SSD/HDD) para persistencia de datos de notas.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos estructurados de las notas.

## Notas adicionales:
Este archivo es fundamental para hacer que NORA pueda recordar y gestionar notas dictadas por el usuario o generadas durante la interacción. La capacidad de almacenar y consultar estas notas permite que NORA sea más eficiente y útil, ya que puede almacenar recordatorios importantes, información personal relevante o cualquier otro dato necesario durante la interacción. También permite realizar acciones como el establecimiento de alarmas, recordatorios o la actualización de notas de manera dinámica.

## Archivos previstos del módulo:
- `gestion_notas.py`: Almacenamiento y consulta de notas dictadas o creadas (este archivo).
- Archivos adicionales como `datos_main.py`, `gestion_rutinas.py`, `memoria_conversacional.py`.
