# Ficha Funcional – `listas_dinamicas.py`

## Nombre del archivo:
`listas_dinamicas.py`

## Responsabilidad principal:
Gestionar las listas de tareas, compras o ideas generadas por el usuario, permitiendo su creación, modificación y consulta dinámica. Este archivo se encarga de proporcionar una forma flexible de gestionar listas personalizadas que pueden ser utilizadas para diversas finalidades, como hacer listas de compras, tareas pendientes, o incluso de elementos de interés para el usuario.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de creación o modificación de listas, datos de elementos para agregar a la lista.
- **Fuente:** `voz/` (para recibir los elementos que el usuario desea agregar o eliminar de las listas), `dialogo/` (para gestionar la interacción con las listas).
- **Formato o protocolo:** Texto plano, estructuras JSON, eventos internos (`CMD_...`, `EVT_...`).

## Salidas generadas:
- **Tipo de salida:** Listas modificadas, confirmaciones de adición o eliminación de elementos, consultas de listas.
- **Destinatario:** `dialogo/`, `sistema/`, `agentes/` (para interactuar con el usuario y gestionar las listas).
- **Ejemplo de salida:**
  - `EVT_LIST_ITEM_ADDED` (Evento que indica que un nuevo elemento ha sido añadido a la lista).
  - `EVT_LIST_ITEM_REMOVED` (Evento que indica que un elemento ha sido eliminado de la lista).
  - `AGT_LIST_RETRIEVED` (Confirmación de que la lista ha sido recuperada correctamente).
  - `CMD_SHOW_LIST` (Instrucción para mostrar la lista actual).

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir la solicitud de lista o modificación de la misma), `dialogo/` (para gestionar la interacción y mostrar la lista).
- **Salida hacia:** `dialogo/`, `sistema/`, `agentes/` (para activar la visualización de la lista y permitir la modificación de elementos).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que las listas se actualicen correctamente y que el sistema pueda ofrecer asistencia personalizada.

## Dependencias técnicas:
- **Librerías externas:** `sqlite3`, `SQLAlchemy` (para almacenamiento persistente de listas en bases de datos locales), `json` (para almacenar y recuperar listas de manera estructurada).
- **Hardware gestionado:** Almacenamiento local (SSD/HDD) para persistencia de listas y elementos.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos de listas.

## Notas adicionales:
Este archivo es fundamental para proporcionar una herramienta flexible de gestión de listas dentro del sistema NORA. Las listas dinámicas permiten al usuario organizar sus tareas, compras o cualquier otro tipo de actividad o interés personal de manera sencilla y accesible. La capacidad de modificar y consultar listas de manera fluida y mediante comandos de voz mejora la experiencia del usuario, facilitando su uso en la vida diaria.

## Archivos previstos del módulo:
- `listas_dinamicas.py`: Gestión de listas de tareas, compras o ideas generadas por el usuario (este archivo).
- Archivos adicionales como `datos_main.py`, `gestion_rutinas.py`, `memoria_conversacional.py`.
