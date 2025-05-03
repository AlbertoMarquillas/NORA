# Transiciones posibles desde el estado – Reposo

Las transiciones desde el estado **Reposo** se producen exclusivamente ante eventos de activación válidos o programados. La FSM (`sistema/`) supervisa estas condiciones y valida su legitimidad antes de activar el sistema.

---

| Estado destino | Evento o condición              | Origen del evento     | Observaciones                                                             |
|----------------|---------------------------------|------------------------|---------------------------------------------------------------------------|
| Activado       | `EVT_NFC_ACTIVATE`              | sensores/              | Activación física mediante tarjeta NFC válida.                           |
| Activado       | `EVT_PRESENCE_CONFIRMED`        | activacion/, sensores/ | Detección de presencia sostenida en rango válido.                        |
| Activado       | `EVT_ATTENTION_GAINED`          | vision/                | Atención visual directa si vigilancia visual está activa.                |
| Escucha        | `EVT_WAKEWORD`                  | voz/                   | Activación por hotword, si `voz/` permanece operativo en latencia.       |
| Activado       | `EVT_SCHEDULE_TRIGGERED`        | datos/, agentes/       | Activación programada por evento interno (agenda, recordatorio, etc.).   |

---

## Reglas y restricciones

- Todas las transiciones requieren que el sistema esté en estado `FSM_READY = True`.
- Si múltiples eventos se detectan simultáneamente, se prioriza:
  1. `EVT_WAKEWORD`
  2. `EVT_NFC_ACTIVATE`
  3. `EVT_ATTENTION_GAINED`
  4. `EVT_PRESENCE_CONFIRMED`
  5. `EVT_SCHEDULE_TRIGGERED`

- El estado `Reposo` no transita directamente a `Procesando`, `Error` o `Atencion`.

- Los agentes pueden suprimir cualquier transición si se detectan condiciones de inhibición de activación.

