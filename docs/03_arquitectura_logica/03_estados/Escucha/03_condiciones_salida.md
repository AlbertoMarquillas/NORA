# Condiciones de salida – Estado: Escucha

El estado **Escucha** finaliza cuando se produce uno de los siguientes eventos que determinan el éxito, fracaso o cancelación de la intención de entrada verbal. La FSM principal (`sistema/`) y los módulos `voz/` y `agentes/` intervienen en esta decisión.

---

## 1. Reconocimiento de voz exitoso

- **Evento:** `EVT_SPEECH_RECOGNIZED`  
  El módulo `voz/` ha captado, preprocesado y segmentado correctamente un fragmento de voz, determinando que constituye un comando válido o interpretable.  
  Transición a estado `Procesando`.

---

## 2. Expiración del tiempo de espera

- **Evento:** `EVT_LISTEN_TIMEOUT`  
  El usuario no emite voz válida dentro del tiempo predefinido (`t_listen_timeout`).  
  Transición a estado `Activado`.

---

## 3. Falla técnica de audio

- **Evento:** `EVT_MIC_FAILURE`  
  Error de hardware o software que impide seguir utilizando el micrófono.  
  Transición directa a `Error`.

---

## 4. Cancelación voluntaria

- **Comando:** `CMD_CANCEL_LISTENING`  
  Emitido desde `gui/`, por el usuario o un agente, si se detecta situación ambigua o intención de abortar la interacción.  
  Transición a estado `Activado`.

---

## Reglas adicionales

- No se permite transición a `Reposo` directamente desde `Escucha`, salvo si no hay eventos de presencia o atención activos tras `EVT_LISTEN_TIMEOUT`.
- Si se detecta simultáneamente voz y error, tiene prioridad la condición de error.
