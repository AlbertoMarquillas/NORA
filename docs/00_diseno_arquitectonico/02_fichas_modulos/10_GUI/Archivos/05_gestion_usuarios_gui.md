# Ficha Funcional – `gestion_usuarios_gui.py`

## Nombre del archivo:
`gestion_usuarios_gui.py`

## Responsabilidad principal:
Administrar los perfiles de usuario de NORA a través de la interfaz gráfica. Permite crear, modificar, eliminar y consultar perfiles, así como configurar preferencias específicas asociadas a cada usuario (idioma, sensibilidad, rutinas, accesos).

## Entradas esperadas:
- **Tipo de entrada:** Formularios de alta, modificación o eliminación de usuarios.
- **Fuente:** Usuario (interacción GUI).
- **Formato o protocolo:** Formularios, eventos GUI.

## Salidas generadas:
- **Tipo de salida:** Actualizaciones de perfiles, confirmaciones visuales, eventos de modificación de usuarios.
- **Destinatario:** `datos/`, `sistema/`, `gui_main.py`.
- **Ejemplo de salida:**
  - Nuevo perfil de usuario guardado
  - Cambio de preferencias de un usuario
  - Eliminación de perfil con confirmación

## Módulos relacionados:
- **Entrada desde:** Usuario (GUI).
- **Salida hacia:** `datos/`, `sistema/`, `gui_main.py`.
- **Comunicación bidireccional con:** `datos/` para gestión persistente.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `json`.
- **Hardware gestionado:** Ninguno directamente.
- **Protocolos:** Manejo de datos estructurados en archivos o bases de datos.

## Notas adicionales:
`gestion_usuarios_gui.py` debe implementar validaciones estrictas de entradas (nombres, configuraciones válidas) y confirmar operaciones sensibles como eliminaciones. La gestión de usuarios debe ser intuitiva, rápida y segura, asegurando siempre la coherencia entre la GUI y la base de datos de usuarios persistente.

