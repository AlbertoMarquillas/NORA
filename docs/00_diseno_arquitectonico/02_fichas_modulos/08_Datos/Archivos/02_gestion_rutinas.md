# Ficha Funcional – `gestion_rutinas.py`

## Nombre del archivo:
`gestion_rutinas.py`

## Responsabilidad principal:
Gestionar las rutinas y recordatorios personalizados dentro del sistema NORA. Este archivo se encarga de crear, almacenar y recuperar rutinas diarias o eventos programados por el usuario, así como de activar recordatorios en momentos específicos. Permite que NORA mantenga una agenda organizada de actividades y tareas, y que recuerde o ejecute acciones de acuerdo con las rutinas definidas por el usuario.

## Entradas esperadas:
- **Tipo de entrada:** Nuevas rutinas o recordatorios, solicitudes de recuperación de rutinas, cambios en las rutinas.
- **Fuente:** `voz/` (para recibir comandos de voz para agregar o modificar rutinas), `dialogo/` (para gestionar la interacción de la rutina), `sistema/` (para obtener información sobre el contexto de la rutina).
- **Formato o protocolo:** Texto plano, eventos internos (`CMD_...`, `EVT_...`), datos de rutina en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Confirmación de rutinas guardadas, eventos de activación de rutinas o recordatorios, datos de rutinas recuperados.
- **Destinatario:** `sistema/`, `voz/`, `dialogo/`, `agentes/` (para activar las rutinas y recordatorios, o para recuperar la información almacenada).
- **Ejemplo de salida:**
  - `EVT_ROUTINE_SAVED` (Evento que indica que una nueva rutina ha sido guardada).
  - `EVT_ROUTINE_TRIGGERED` (Evento que indica que una rutina ha sido activada, como un recordatorio).
  - `AGT_ROUTINE_RETRIEVED` (Confirmación de que los datos de la rutina han sido recuperados correctamente).

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir comandos de voz para crear o modificar rutinas), `dialogo/` (para interactuar con las rutinas y recordatorios), `sistema/` (para obtener el estado y contexto de la rutina).
- **Salida hacia:** `sistema/`, `voz/`, `dialogo/` (para proporcionar los datos de la rutina y activar los recordatorios).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar las rutinas con el contexto global del sistema y asegurar que los recordatorios se ajusten al flujo conversacional.

## Dependencias técnicas:
- **Librerías externas:** `sqlite3`, `SQLAlchemy` (para persistencia de datos de rutinas y recordatorios en bases de datos locales), `json` (para el almacenamiento de datos en formato estructurado).
- **Hardware gestionado:** Almacenamiento local USB (SSD/HDD) para persistencia de rutinas y recordatorios.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos estructurados de las rutinas.

## Notas adicionales:
Este archivo es clave para que NORA gestione de manera efectiva las rutinas y recordatorios de los usuarios. Las rutinas personalizadas permiten que NORA ayude al usuario a organizar su día, recordándole tareas importantes, citas o actividades programadas. Además, la capacidad de modificar y recuperar rutinas según el contexto de la conversación mejora la experiencia del usuario, haciendo que NORA sea un asistente útil para la gestión de la agenda personal.

## Archivos previstos del módulo:
- `gestion_rutinas.py`: Administración de rutinas y recordatorios personalizados (este archivo).
- Archivos adicionales como `datos_main.py`, `historial_eventos.py`, `memoria_conversacional.py`.
