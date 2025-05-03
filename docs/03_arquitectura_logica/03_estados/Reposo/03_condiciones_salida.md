# Condiciones de salida – Estado: Reposo

El sistema NORA abandona el estado **Reposo** cuando se detecta una condición clara de intención de activación por parte del usuario o por una condición programada del sistema. Estas transiciones son evaluadas por la FSM (`sistema/`) y validadas, en caso necesario, por los agentes perceptivos.

---

## 1. Activación por detección NFC

- **Evento:** `EVT_NFC_ACTIVATE`  
  Emitido por el módulo `sensores/` tras la lectura de una etiqueta NFC válida.  
  Transición directa a estado `Activado`.

---

## 2. Activación por presencia

- **Evento:** `EVT_PRESENCE_CONFIRMED`  
  Detectada por sensores de proximidad o ultrasónicos conectados a `activacion/`.  
  Debe cumplir condiciones configuradas como distancia, duración y horario.

---

## 3. Activación por atención visual

- **Evento:** `EVT_ATTENTION_GAINED`  
  Si el módulo `vision/` está configurado en vigilancia latente, puede emitir este evento ante la detección de rostro y mirada directa.  
  Puede ser modulada por agentes para evitar falsos positivos.

---

## 4. Activación por voz

- **Evento:** `EVT_WAKEWORD`  
  Generado por el módulo `voz/` si está habilitado el detector de hotword en segundo plano.  
  Este evento inicia la cadena de transición hacia `Escucha`.

---

## 5. Activación programada

- **Evento:** `EVT_SCHEDULE_TRIGGERED`  
  Emitido por el módulo `datos/` o `agentes/` si hay rutinas programadas (por ejemplo, despertador, recordatorios).

---

## Consideraciones adicionales

- La transición desde `Reposo` puede ser denegada si hay condiciones inhibidoras activas (`CMD_INHIBIR_ACTIVACION`, `modo_privado = True`).
- Si el sistema se despierta por error o ruido de sensores, puede volver a `Reposo` tras validación rápida de ausencia.
