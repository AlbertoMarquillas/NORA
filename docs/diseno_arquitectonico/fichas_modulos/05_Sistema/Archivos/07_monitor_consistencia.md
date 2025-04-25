# Ficha Funcional – `monitor_consistencia.py`

## Nombre del archivo:
`monitor_consistencia.py`

## Responsabilidad principal:
Detectar y gestionar la desincronización o fallos lógicos dentro del sistema NORA. Este archivo se encarga de verificar que los módulos estén trabajando de manera coherente entre sí, supervisando el estado del sistema y asegurando que no haya inconsistencias o errores en la ejecución que puedan comprometer el comportamiento global.

## Entradas esperadas:
- **Tipo de entrada:** Estados de los módulos, registros de actividad, eventos de error o desincronización.
- **Fuente:** Módulos como `sistema/`, `agentes/`, `interfaz/`, `voz/`, que generan eventos o estados que podrían indicar desincronización o fallos.
- **Formato o protocolo:** Eventos internos de sincronización (`EVT_STATE_CHANGED`, `EVT_MODULE_FAILURE`), registros de actividad del sistema.

## Salidas generadas:
- **Tipo de salida:** Alertas de inconsistencia, eventos de autocorrección, instrucciones para reiniciar o ajustar módulos.
- **Destinatario:** `sistema/` (para reiniciar o corregir módulos desincronizados), `interfaz/` (para mostrar notificaciones de error o inconsistencias al usuario).
- **Ejemplo de salida:**
  - `EVT_INCONSISTENCY_DETECTED` (Evento que indica que se ha detectado una inconsistencia en el sistema).
  - `CMD_RESTART_MODULE` (Instrucción para reiniciar un módulo desincronizado).
  - `AGT_SYNC_CORRECTION` (Instrucción para realizar una corrección en la sincronización de los módulos).

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `agentes/`, `interfaz/`, `voz/` (para recibir eventos o estados que puedan indicar inconsistencias o desincronización).
- **Salida hacia:** `sistema/` (para aplicar correcciones o reinicios de módulos), `interfaz/` (para mostrar alertas de fallos o inconsistencias).
- **Comunicación bidireccional con:** `sistema/`, `agentes/`, `interfaz/` para gestionar la corrección de fallos y la sincronización entre módulos.

## Dependencias técnicas:
- **Librerías externas:** `pyee` o `eventbus` (para la gestión de eventos y la distribución de señales de inconsistencias), `logging` (para registrar eventos de errores y desincronización).
- **Hardware gestionado:** Ninguno directamente (gestiona la coherencia entre módulos a nivel lógico).
- **Protocolos:** Comunicación basada en eventos internos, detección de inconsistencias y ejecución de autocorrecciones.

## Notas adicionales:
Este archivo es fundamental para garantizar la estabilidad y fiabilidad del sistema NORA. Al monitorizar continuamente el estado de los módulos y verificar que todos los componentes estén funcionando de manera coherente, `monitor_consistencia.py` asegura que el sistema no se desestabilice debido a fallos lógicos o desincronización entre los módulos. Además, permite ejecutar acciones correctivas de forma automática, lo que mejora la resiliencia del sistema y permite mantener el funcionamiento continuo sin intervención manual.

## Archivos previstos del módulo:
- `monitor_consistencia.py`: Detección de desincronización o fallos lógicos, autocorrección (este archivo).
- Archivos adicionales como `fsm_control.py`, `gestion_eventos.py`.
