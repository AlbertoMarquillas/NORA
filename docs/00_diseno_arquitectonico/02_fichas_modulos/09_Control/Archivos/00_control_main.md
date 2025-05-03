# Ficha Funcional – `control_main.py`

## Nombre del archivo:
`control_main.py`

## Responsabilidad principal:
Coordinar la supervisión general y la administración del sistema NORA. Este archivo es el punto de entrada del módulo `control/`, desde el cual se inicializan los subsistemas de control de hardware, monitoreo de estado, energía, conexión WiFi externa, protección ante fallos, gestión de logs, sincronización horaria, entre otros. Establece la arquitectura modular de `control/` y mantiene la comunicación con el núcleo `sistema/` y la interfaz de usuario `gui/`.

## Entradas esperadas:
- **Tipo de entrada:** Comandos administrativos, eventos de estado, configuraciones del sistema.
- **Fuente:** `gui/`, `sistema/`, eventos internos de `control/`.
- **Formato o protocolo:** Llamadas internas a funciones, eventos estructurados (`EVT_...`), comandos tipo `CMD_...`.

## Salidas generadas:
- **Tipo de salida:** Instrucciones de control a subsistemas, actualizaciones de estado, alarmas y registros de eventos.
- **Destinatario:** `sistema/`, `gui/`, periféricos gestionados (expansor, WiFi, RTC).
- **Ejemplo de salida:**
  - `CMD_INICIALIZAR_HARDWARE`
  - `EVT_DIAGNOSTICO_OK`
  - `CMD_APAGADO_CONTROLADO`

## Módulos relacionados:
- **Entrada desde:** `gui/` (comandos de administración manual), `sistema/` (eventos globales), `control/` (submódulos).
- **Salida hacia:** `sistema/` (actualización de estados), `gui/` (logs, estado del sistema), periféricos físicos.
- **Comunicación bidireccional con:** Todos los submódulos de `control/`.

## Dependencias técnicas:
- **Librerías externas:** `RPi.GPIO`, `gpiozero`, `smbus2`, `psutil`, `os`, `subprocess`, `logging`.
- **Hardware gestionado:** Expansor PCF8574, módulo WiFi, RTC DS3231.
- **Protocolos:** GPIO, I2C, UART, llamadas al sistema operativo.

## Notas adicionales:
`control_main.py` actúa como orquestador del funcionamiento de bajo nivel del sistema NORA. Asegura que los servicios críticos estén inicializados correctamente al arranque, mantiene operativos los subsistemas de control, gestiona los procedimientos de apagado y reinicio seguros, y proporciona información de estado al núcleo del sistema y a la interfaz de usuario.

Este archivo debe garantizar la resiliencia del sistema ante condiciones adversas, incluyendo detección de fallos, recuperación automática y optimización del consumo de recursos según las necesidades de operación.

