# Transiciones posibles desde el estado – Error

Las transiciones desde el estado **Error** están restringidas y controladas. Sólo pueden producirse una vez validada la recuperación del incidente que causó el fallo. Estas transiciones se ejecutan desde la FSM principal (`sistema/`) bajo condiciones estrictas, con posible participación de agentes y supervisión externa.

---

| Estado destino | Evento o condición            | Origen del evento  | Observaciones                                                                 |
|----------------|-------------------------------|---------------------|------------------------------------------------------------------------------|
| Activado       | `EVT_RECOVERY_SUCCESS`         | control/             | Recuperación automática del módulo afectado. Reinicio limpio.                |
| Activado       | `CMD_FORCE_RESUME`             | gui/                 | Intervención manual desde interfaz de desarrollo o mantenimiento.            |
| Activado       | `EVT_ENV_RESTORED`             | sensores/            | Condiciones ambientales restauradas a niveles operativos.                    |
| Activado       | `t_error_recovery_timeout`     | sistema/             | Tiempo de espera superado, sin agravamiento. Evaluación de estado estable.   |

---

## Reglas de transición

- La única transición permitida desde `Error` es hacia el estado `Activado`.
- Transiciones múltiples a `Error` en corto plazo deben generar evento `EVT_CRITICAL_FAILURE`.
- Durante la transición de salida, se debe revalidar el estado de todos los módulos críticos (`voz/`, `vision/`, `sensores/`, `control/`).

---

## Restricciones

- No se permite transitar directamente desde `Error` a estados interactivos (`Escucha`, `Procesando`, `Atencion`).
- Si durante el proceso de salida se detecta un nuevo fallo, se reinicia el estado `Error` con nuevo registro.

