# Ficha Funcional – `gui_main.py`

## Nombre del archivo:
`gui_main.py`

## Responsabilidad principal:
Coordinar la ejecución principal de la interfaz gráfica de NORA. Se encarga de inicializar los subpaneles, manejar la navegación entre secciones de la GUI, distribuir los eventos de usuario y orquestar la comunicación visual entre los distintos componentes gráficos.

## Entradas esperadas:
- **Tipo de entrada:** Acciones del usuario (clics, entradas de texto, selecciones), comandos internos para actualizar vistas.
- **Fuente:** Usuario (interacción directa), módulos internos (`panel_control.py`, `monitor_eventos.py`, etc.).
- **Formato o protocolo:** Eventos GUI, funciones de callback.

## Salidas generadas:
- **Tipo de salida:** Cambios de vista, actualizaciones de paneles, comandos a otros módulos de NORA.
- **Destinatario:** Subpaneles de `gui/`, `sistema/`, `control/`, `voz/`, `interfaz/`, `datos/`.
- **Ejemplo de salida:**
  - Activación de panel de diagnóstico
  - Envió de comando `CMD_MODULE_RESTART` al `sistema/`

## Módulos relacionados:
- **Entrada desde:** Usuario (acciones GUI), subpaneles.
- **Salida hacia:** Subpaneles (`panel_control.py`, `monitor_eventos.py`, etc.), `sistema/`, `control/`.
- **Comunicación bidireccional con:** Todos los subpaneles de `gui/` y el núcleo `sistema/`.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `flask`, `dash` (dependiendo de implementación).
- **Hardware gestionado:** Ninguno directamente.
- **Protocolos:** Interno por eventos GUI.

## Notas adicionales:
`gui_main.py` constituye el "centro de control" de la interfaz de usuario de NORA. Su diseño debe garantizar fluidez, modularidad y reactividad, permitiendo cambiar entre secciones de la GUI sin interrupciones ni bloqueos de la aplicación. Asimismo, debe asegurar una comunicación robusta y desacoplada con los módulos de control del sistema para ejecutar las acciones solicitadas por el usuario de forma segura.