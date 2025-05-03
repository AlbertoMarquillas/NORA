# Transiciones posibles desde el estado – Procesando

Las transiciones desde el estado **Procesando** dependen del resultado del análisis de entrada y del tipo de acción generada por los módulos `dialogo/`, `agentes/` o `models/`. La FSM (`sistema/`) coordina estas salidas para garantizar continuidad, robustez y coherencia en la interacción.

---

| Estado destino | Evento o condición              | Origen del evento | Observaciones                                                               |
|----------------|---------------------------------|-------------------|----------------------------------------------------------------------------|
| Activado       | `EVT_PROCESS_COMPLETED`         | dialogo/, agentes/| Acción generada sin salida física inmediata. Retorno al estado intermedio. |
| Error          | `EVT_PROCESS_FAILURE`           | dialogo/, models/ | Fallo de interpretación, ambigüedad no resoluble o entrada inválida.       |
| Activado       | `CMD_ACTUAR` ejecutado          | sistema/          | Acción física o lógica completada (gesto, cambio de estado, etc.).         |
| Activado       | `CMD_ABORT_PROCESS`             | gui/, agentes/    | Cancelación por contexto, usuario o detección de redundancia.              |

---

## Reglas de transición

- Siempre debe emitirse `EVT_PROCESS_COMPLETED` antes de liberar FSM y cambiar de estado.
- La transición a `Error` tiene prioridad en caso de conflicto.
- Cualquier transición desde `Procesando` implica el desbloqueo explícito de la FSM (`FSM_LOCK = False`).
- Transiciones directas a `Escucha`, `Reposo` o `Atencion` no están permitidas desde este estado.

