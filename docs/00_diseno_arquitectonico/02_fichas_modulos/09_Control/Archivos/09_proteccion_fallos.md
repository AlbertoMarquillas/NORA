# Ficha Funcional – `proteccion_fallos.py`

## Nombre del archivo:
`proteccion_fallos.py`

## Responsabilidad principal:
Implementar mecanismos de protección y recuperación ante fallos críticos del sistema NORA. Supervisa condiciones de error grave, gestiona el watchdog interno, y ejecuta acciones correctivas automáticas como reinicios selectivos, apagado de emergencia o escalada de alarmas.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de fallo, alertas críticas del sistema, monitorización de estado anómalo.
- **Fuente:** `supervision_estado.py`, `control_main.py`, `sistema/`.
- **Formato o protocolo:** Eventos estructurados (`EVT_ERROR_CRITICO`, `EVT_TEMPERATURA_ALTA`, etc.).

## Salidas generadas:
- **Tipo de salida:** Acciones de recuperación, reinicios automáticos, apagados controlados, logs de incidentes.
- **Destinatario:** `control_main.py`, `sistema/`, `gui/`.
- **Ejemplo de salida:**
  - `CMD_REINICIAR_SISTEMA`
  - `CMD_APAGADO_EMERGENCIA`
  - Registro de evento crítico en logs

## Módulos relacionados:
- **Entrada desde:** `supervision_estado.py`, `control_main.py`, `sistema/`.
- **Salida hacia:** `control_main.py`, `sistema/`, `gui/`.
- **Comunicación bidireccional con:** Watchdog de sistema, sistema operativo.

## Dependencias técnicas:
- **Librerías externas:** `RPi.GPIO`, `os`, `subprocess`, `logging`, `watchdog`.
- **Hardware gestionado:** CPU (monitoreo), periféricos críticos.
- **Protocolos:** GPIO, llamadas al sistema operativo.

## Notas adicionales:
`proteccion_fallos.py` es esencial para garantizar la resiliencia operativa de NORA frente a fallos imprevistos. Debe ser capaz de discriminar entre fallos recuperables y no recuperables, aplicar estrategias escalonadas de respuesta, y preservar la integridad de los datos ante cualquier apagado o reinicio forzado. La correcta configuración del watchdog y su integración con los eventos del sistema es fundamental para su efectividad.

