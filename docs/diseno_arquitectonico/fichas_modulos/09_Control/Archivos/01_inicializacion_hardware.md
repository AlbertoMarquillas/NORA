# Ficha Funcional – `inicializacion_hardware.py`

## Nombre del archivo:
`inicializacion_hardware.py`

## Responsabilidad principal:
Configurar todos los componentes de hardware necesarios al arranque del sistema NORA. Este archivo se encarga de la inicialización de GPIOs, buses de comunicación (I2C, UART), sensores físicos conectados, expansores de entradas/salidas, y otros periféricos necesarios para el correcto funcionamiento del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Llamada de inicialización desde `control_main.py`.
- **Fuente:** `control_main.py`
- **Formato o protocolo:** Invocación de funciones internas de configuración.

## Salidas generadas:
- **Tipo de salida:** Estado de inicialización, errores detectados, logs de configuración.
- **Destinatario:** `control_main.py`, `sistema/` (en caso de error crítico), `gui/` (para registro de logs).
- **Ejemplo de salida:**
  - `EVT_HARDWARE_INITIALIZED`
  - `EVT_HARDWARE_ERROR`

## Módulos relacionados:
- **Entrada desde:** `control_main.py`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Dispositivos de hardware (GPIOs, sensores, expansores).

## Dependencias técnicas:
- **Librerías externas:** `RPi.GPIO`, `gpiozero`, `smbus2`, `os`, `subprocess`, `logging`.
- **Hardware gestionado:** GPIOs nativos, bus I2C para sensores y expansores, UART para comunicaciones.
- **Protocolos:** GPIO, I2C, UART.

## Notas adicionales:
`inicializacion_hardware.py` debe garantizar que todos los dispositivos físicos necesarios estén correctamente configurados antes de iniciar la operación normal del sistema. Debe manejar fallos de inicialización de manera segura, reportando errores críticos si algún componente esencial no puede ser preparado. Este archivo es esencial para asegurar que el sistema sea robusto y tolerante a condiciones de arranque anómalas.

