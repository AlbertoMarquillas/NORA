# Transiciones posibles desde el estado – Activado

Las siguientes transiciones son gestionadas por la FSM principal (`sistema/`), en función de eventos captados por los módulos sensoriales o inferidos por agentes. Cada transición se activa bajo una condición concreta y conduce a un estado siguiente bien definido.

---

| Estado destino | Evento o condición                | Origen del evento       | Observaciones                                                       |
|----------------|-----------------------------------|--------------------------|----------------------------------------------------------------------|
| Escucha        | `EVT_SPEECH_START`                | voz/                     | Activación por voz o hotword. Prioritaria si se produce en solitario. |
| Atencion       | `EVT_ATTENTION_CONFIRMED`         | vision/ + agentes/       | Detecta atención sostenida. Puede competir con `EVT_SPEECH_START`.    |
| Reposo         | `EVT_IDLE_TIMEOUT`                | sistema/                 | Inactividad prolongada. Reinicia el sistema al modo pasivo.          |
| Error          | `EVT_MODULE_FAILURE`              | control/, sensores/, etc | Falla crítica detectada por supervisión del sistema.                 |

---

## Notas

- Estas transiciones pueden ser moduladas dinámicamente por los agentes en función del perfil del usuario, condiciones ambientales o estado emocional.
- Si se reciben múltiples eventos en conflicto, se prioriza el orden: `Error` > `Escucha` / `Atencion` (según timestamp) > `Reposo`.
- El módulo `sistema/` es responsable de emitir `CMD_TRANSICION_ESTADO` tras validar las condiciones de cada transición.
