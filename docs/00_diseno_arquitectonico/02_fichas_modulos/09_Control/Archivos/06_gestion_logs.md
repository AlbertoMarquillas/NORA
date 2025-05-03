# Ficha Funcional – `gestion_logs.py`

## Nombre del archivo:
`gestion_logs.py`

## Responsabilidad principal:
Gestionar el registro estructurado de eventos, alertas, errores y mensajes operativos generados por el sistema NORA. Este archivo proporciona una infraestructura de logging centralizada para auditar el comportamiento del sistema, depurar incidencias y mantener historiales de actividad relevantes.

## Entradas esperadas:
- **Tipo de entrada:** Mensajes de log, eventos del sistema, notificaciones de error o advertencia.
- **Fuente:** `control_main.py`, `sistema/`, `supervision_estado.py`, demás submódulos de `control/`.
- **Formato o protocolo:** Llamadas a funciones de logging estructuradas (`info`, `warning`, `error`, `critical`).

## Salidas generadas:
- **Tipo de salida:** Archivos de log persistentes, mensajes de alerta a `gui/`, eventos críticos al sistema.
- **Destinatario:** Sistema de archivos, `gui/`, `control_main.py`.
- **Ejemplo de salida:**
  - Archivo `nora_system.log`
  - Alerta visual en `gui/` por evento crítico

## Módulos relacionados:
- **Entrada desde:** `control_main.py`, `sistema/`, `supervision_estado.py`, submódulos de `control/`.
- **Salida hacia:** Sistema de archivos, `gui/`.
- **Comunicación bidireccional con:** Ninguna (función de almacenamiento y emisión pasiva).

## Dependencias técnicas:
- **Librerías externas:** `logging`, `os`, `datetime`.
- **Hardware gestionado:** Almacenamiento local (USB SSD/HDD).
- **Protocolos:** Escritura en sistema de archivos.

## Notas adicionales:
`gestion_logs.py` debe implementar mecanismos de rotación automática de logs (log rotation) para evitar la saturación del almacenamiento, y permitir configuraciones de nivel de severidad dinámicas (por ejemplo, `DEBUG` en fase de desarrollo y `WARNING`/`ERROR` en operación normal). El diseño debe priorizar robustez ante caídas y garantizar la persistencia segura de los registros.