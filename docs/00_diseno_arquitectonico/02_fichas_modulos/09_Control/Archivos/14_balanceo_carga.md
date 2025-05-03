# Ficha Funcional – `balanceo_carga.py`

## Nombre del archivo:
`balanceo_carga.py`

## Responsabilidad principal:
Implementar estrategias de redistribución dinámica de tareas en el sistema NORA para optimizar el uso de CPU, memoria y recursos de I/O. Permite ajustar la carga de procesamiento según la disponibilidad de recursos y el estado operativo del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Datos de supervisión de uso de CPU, RAM y actividad de módulos.
- **Fuente:** `supervision_estado.py`, `control_main.py`, `sistema/`.
- **Formato o protocolo:** Monitoreo de procesos, eventos de estado (`EVT_HIGH_CPU_LOAD`, `EVT_MEMORY_USAGE_HIGH`).

## Salidas generadas:
- **Tipo de salida:** Comandos de ajuste de carga, reprogramación de tareas, logs de optimización.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `CMD_REDUCIR_PRIORIDAD_PROCESO`
  - `CMD_DESACTIVAR_MODULO_NO_CRITICO`
  - Registro de balanceo de carga en log

## Módulos relacionados:
- **Entrada desde:** `supervision_estado.py`, `sistema/`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Sistema operativo para la gestión de procesos.

## Dependencias técnicas:
- **Librerías externas:** `psutil`, `os`, `subprocess`, `logging`.
- **Hardware gestionado:** CPU, RAM.
- **Protocolos:** Control interno de procesos y prioridad del sistema operativo.

## Notas adicionales:
`balanceo_carga.py` mejora la estabilidad y la capacidad de respuesta de NORA durante situaciones de alta demanda. Debe ser capaz de actuar preventivamente antes de que el sistema entre en estados críticos, garantizando la continuidad operativa mediante la desactivación temporal o la priorización inteligente de tareas y servicios.

