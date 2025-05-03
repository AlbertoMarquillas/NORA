# Ficha Funcional – `agenda_calendario.py`

## Nombre del archivo:
`agenda_calendario.py`

## Responsabilidad principal:
Gestionar la administración de citas, recordatorios y eventos de calendario dentro del sistema NORA. Este archivo se encarga de crear, modificar y consultar eventos en la agenda, permitiendo que NORA actúe como un asistente para organizar citas, establecer recordatorios y gestionar eventos importantes según las necesidades del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Nuevos eventos de calendario, solicitudes de modificación de citas, consultas de agenda.
- **Fuente:** `voz/` (para recibir comandos de voz para agregar o modificar eventos), `dialogo/` (para gestionar las interacciones de la agenda), `sistema/` (para obtener datos del calendario).
- **Formato o protocolo:** Texto plano, estructuras JSON para definir los eventos, comandos internos (`CMD_...`, `EVT_...`).

## Salidas generadas:
- **Tipo de salida:** Confirmación de evento añadido, listado de eventos, alertas de recordatorio.
- **Destinatario:** `sistema/`, `voz/`, `dialogo/`, `agentes/` (para activar los recordatorios o gestionar los eventos).
- **Ejemplo de salida:**
  - `EVT_EVENT_ADDED` (Evento que indica que un nuevo evento ha sido añadido al calendario).
  - `EVT_REMINDER_TRIGGERED` (Evento que indica que un recordatorio ha sido activado).
  - `AGT_EVENT_LIST` (Listado de eventos próximos o eventos solicitados).

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir comandos sobre la agenda y las citas), `dialogo/` (para interactuar con la agenda y obtener información sobre eventos programados).
- **Salida hacia:** `voz/`, `sistema/`, `dialogo/`, `agentes/` (para proporcionar la información de los eventos y activar recordatorios).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que los eventos se gestionen adecuadamente en el sistema y se mantenga la coherencia con otras interacciones.

## Dependencias técnicas:
- **Librerías externas:** `sqlite3`, `SQLAlchemy` (para almacenamiento persistente de eventos y citas), `datetime` (para gestión de fechas y horas), `json` (para serialización de eventos).
- **Hardware gestionado:** Almacenamiento local (SSD/HDD) para persistencia de eventos y recordatorios.
- **Protocolos:** SQL, JSON para almacenar y recuperar eventos, comunicación interna para coordinar los recordatorios.

## Notas adicionales:
Este archivo es fundamental para convertir a NORA en un asistente de productividad que pueda gestionar la agenda del usuario de manera eficiente. Con la integración de recordatorios y la gestión de citas, NORA puede asistir en la organización del día a día del usuario, recordándole eventos importantes y asegurándose de que nunca se pierdan tareas o citas críticas. Además, la posibilidad de interactuar con la agenda de manera natural mediante comandos de voz mejora la experiencia del usuario al hacer la interacción más fluida.

## Archivos previstos del módulo:
- `agenda_calendario.py`: Administración de citas, recordatorios temporales y eventos de calendario (este archivo).
- Archivos adicionales como `datos_main.py`, `gestion_rutinas.py`, `memoria_conversacional.py`.
