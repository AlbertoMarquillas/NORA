# Ficha Funcional – `configuracion_manual.py`

## Nombre del archivo:
`configuracion_manual.py`

## Responsabilidad principal:
Permitir la edición manual de configuraciones del sistema NORA a través de la GUI. Facilita la modificación de parámetros como idioma, perfiles de usuario, tiempos de espera, sensibilidad de sensores, volumen, y preferencias del comportamiento general del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Formulario de configuración, acciones de usuario (guardar/cancelar).
- **Fuente:** Usuario (interacción GUI).
- **Formato o protocolo:** Formularios de entrada, validación de datos.

## Salidas generadas:
- **Tipo de salida:** Actualización de configuraciones, eventos de reconfiguración, logs de cambios.
- **Destinatario:** `datos/`, `sistema/`, `control/`, `voz/`, `interfaz/`.
- **Ejemplo de salida:**
  - `CMD_UPDATE_LANGUAGE('es')`
  - `CMD_SET_VOLUME(70)`
  - Registro de cambio de configuración

## Módulos relacionados:
- **Entrada desde:** Usuario (GUI).
- **Salida hacia:** `datos/`, `sistema/`, `control/`, `voz/`, `interfaz/`.
- **Comunicación bidireccional con:** `gui_main.py` para actualizar y reflejar cambios en la interfaz.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `json`.
- **Hardware gestionado:** Ninguno directamente.
- **Protocolos:** Lectura/escritura de configuraciones en archivos o bases de datos.

## Notas adicionales:
`configuracion_manual.py` debe asegurar la validación estricta de las entradas del usuario para evitar corrupción de configuraciones. Debe ofrecer mecanismos de restauración de valores por defecto y confirmación visual de los cambios aplicados. La estructura de los formularios debe ser modular para facilitar la ampliación futura de parámetros configurables.