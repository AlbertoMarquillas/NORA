# Condiciones de salida – Estado: Activado

El sistema abandona el estado **Activado** cuando se produce uno de los siguientes eventos o condiciones de transición, evaluadas por la FSM principal (`sistema/`) y, si aplica, validadas por los agentes de contexto (`/agentes/`).

---

## 1. Transición a estado `Escucha`

- **Evento:** `EVT_SPEECH_START`  
  Emitido por el módulo `voz/` tras detección de voz inicial o hotword.  
  Esta transición requiere que el micrófono esté operativo y que no haya eventos de inhibición activos (`CMD_INHIBIR_MIC`).

---

## 2. Transición a estado `Atencion`

- **Evento:** `EVT_ATTENTION_CONFIRMED`  
  Confirmación de atención visual sostenida, emitida por el módulo `vision/` y validada por los agentes.  
  Esta transición puede ser preferida si se detecta mirada directa del usuario antes de recibir voz.

---

## 3. Transición a estado `Reposo`

- **Evento:** `EVT_IDLE_TIMEOUT`  
  Generado internamente por `sistema/` si se supera el umbral de tiempo sin recibir eventos relevantes.  
  Se considera inactividad prolongada (e.g., >60 s sin presencia, voz ni atención).

---

## 4. Transición a estado `Error`

- **Evento:** `EVT_MODULE_FAILURE`  
  Generado por cualquier módulo (`voz/`, `vision/`, `control/`, etc.) al detectar una falla crítica (pérdida de dispositivo, fallo de inicialización, desconexión física).  
  La FSM puede decidir una recuperación directa o escalar a `Error`.

---

## Reglas adicionales

- Si el sistema detecta simultáneamente voz y atención, se prioriza el evento más reciente a menos que un agente indique lo contrario.
- El estado `Activado` es transitorio y no debe mantenerse indefinidamente. El `timeout_max_activado` define un umbral superior configurable (recomendado: 90 s).
