# Ficha Funcional – `gestion_energia.py`

## Nombre del archivo:
`gestion_energia.py`

## Responsabilidad principal:
Gestionar las estrategias de consumo energético del sistema NORA, incluyendo la transición a perfiles de bajo consumo, el apagado controlado de periféricos no esenciales y la ejecución de procedimientos de apagado o suspensión del sistema completo de forma segura y programada.

## Entradas esperadas:
- **Tipo de entrada:** Condiciones del sistema (batería baja, inactividad), comandos de ahorro energético.
- **Fuente:** `control_main.py`, `supervision_estado.py`, `sistema/`.
- **Formato o protocolo:** Eventos internos, evaluación de condiciones, comandos de energía (`CMD_...`).

## Salidas generadas:
- **Tipo de salida:** Acciones de control de energía, logs de eventos energéticos, señales de apagado o suspensión.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`, periféricos físicos.
- **Ejemplo de salida:**
  - `EVT_LOW_POWER_MODE_ACTIVATED`
  - `CMD_SHUTDOWN`
  - `CMD_SLEEP_MODE`

## Módulos relacionados:
- **Entrada desde:** `control_main.py`, `supervision_estado.py`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Hardware gestionado (GPIOs de control de periféricos, sistema operativo).

## Dependencias técnicas:
- **Librerías externas:** `os`, `subprocess`, `RPi.GPIO`, `logging`.
- **Hardware gestionado:** GPIOs asociados a periféricos, Raspberry Pi.
- **Protocolos:** GPIO, llamadas al sistema operativo (shutdown, sleep).

## Notas adicionales:
`gestion_energia.py` es clave para optimizar la autonomía y longevidad de la operación de NORA, especialmente en configuraciones alimentadas por batería o en escenarios de contingencia. Debe priorizar la integridad de datos durante apagados y asegurarse de minimizar riesgos de corrupción o daño de hardware. Su diseño debe contemplar perfiles dinámicos ajustables según la carga del sistema y el contexto operativo.

