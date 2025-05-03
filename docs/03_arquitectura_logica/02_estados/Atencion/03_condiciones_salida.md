# Condiciones de salida – Estado: Atencion

El sistema abandona el estado **Atencion** cuando se produce uno de los siguientes eventos, evaluados por la FSM principal (`sistema/`) y, si aplica, validados por agentes perceptivos o contextuales.

---

## 1. Transición a estado `Escucha`

- **Evento:** `EVT_SPEECH_START`  
  Emisión desde el módulo `voz/` al detectar una señal de inicio de vocalización (actividad de voz con umbral superado).
  Se considera la transición principal esperada desde este estado.

---

## 2. Transición a estado `Procesando`

- **Evento:** `EVT_GESTURE_COMMAND`  
  Generado por el módulo `vision/` si se detecta un gesto explícito reconocido (por ejemplo, señal con la mano).
  Permite interacción no verbal directa, sin pasar por `Escucha`.

---

## 3. Retorno a estado `Activado`

- **Evento:** `EVT_ATTENTION_LOST`  
  Se produce cuando se pierde el contacto visual por debajo del umbral de sostenimiento definido (`T_ATTENTION_BREAK`).
  El sistema considera que la atención ha cesado voluntariamente o por distracción.

---

## 4. Transición a estado `Error`

- **Evento:** `EVT_CAMERA_FAILURE` o `EVT_TRACKING_LOST`  
  Emisión por el módulo `vision/` o `control/` ante pérdida del stream de vídeo, error de hardware, o tracking inestable durante más de `t_tracking_max_lost`.

---

## Condiciones adicionales

- Un agente puede forzar la salida inmediata mediante `CMD_ABORT_ATTENTION` si se detecta riesgo de bloqueo o inconsistencia contextual.
- Si se mantiene atención visual sin cambio durante más de `T_ATTENTION_MAX`, se recomienda evaluar la transición a `Escucha` automáticamente, previa confirmación acústica (ej. sonido breve de "¿necesitas algo?").
