# Ficha Funcional – `panel_control.py`

## Nombre del archivo:
`panel_control.py`

## Responsabilidad principal:
Proporcionar un panel gráfico central desde el cual el usuario puede controlar manualmente el estado general de NORA. Permite iniciar, detener, reiniciar o configurar el comportamiento de los módulos principales del sistema de forma sencilla y visual.

## Entradas esperadas:
- **Tipo de entrada:** Acciones del usuario (botones, formularios, selecciones).
- **Fuente:** Usuario a través de la GUI.
- **Formato o protocolo:** Eventos GUI, funciones de callback.

## Salidas generadas:
- **Tipo de salida:** Comandos de control de módulos, actualizaciones visuales del estado.
- **Destinatario:** `sistema/`, `control/`, `voz/`, `interfaz/`, `datos/`.
- **Ejemplo de salida:**
  - `CMD_MODULE_START('vision')`
  - `CMD_MODULE_STOP('voz')`
  - `CMD_MODULE_RESTART('sensores')`

## Módulos relacionados:
- **Entrada desde:** Usuario (eventos GUI).
- **Salida hacia:** `sistema/`, `control/`, `voz/`, `interfaz/`, `datos/`.
- **Comunicación bidireccional con:** `gui_main.py` para coordinación de acciones.

## Dependencias técnicas:
- **Librerías externas:** `tkinter`, `PyQt5`, `PySide2`, `streamlit` (opcional).
- **Hardware gestionado:** Ninguno directo; interacción indirecta con hardware mediante módulos controlados.
- **Protocolos:** Eventos internos.

## Notas adicionales:
`panel_control.py` debe ofrecer una visualización clara y accesible del estado de cada módulo, incluyendo indicadores de estado activos, botones de acción directa y confirmaciones visuales de operaciones realizadas. Debe priorizar la usabilidad, la seguridad en el envío de comandos y permitir operaciones de mantenimiento de forma ágil y segura.