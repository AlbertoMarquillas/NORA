# Condiciones de entrada – Estado: Escucha

El sistema NORA entra en el estado **Escucha** cuando se detecta la intención verbal del usuario a través de eventos auditivos válidos. La transición es gestionada por la FSM principal (`sistema/`) y requiere confirmación mínima de viabilidad técnica en el módulo `voz/`.

---

## 1. Detección de inicio de voz

- **Evento:** `EVT_SPEECH_START`  
  Emitido por el módulo `voz/` cuando se detecta actividad de voz (VAD) con umbral de confianza suficiente.  
  Este evento debe coincidir con una ventana de activación válida (ej. tras `Activado` o `Atencion`).

---

## 2. Activación previa exitosa

- **Origen válido:** `Activado` o `Atencion`  
  La transición solo está permitida si el sistema se encontraba en estado de espera consciente (preparado para interacción).

---

## 3. Evaluación de contexto

- Los agentes (`/agentes/`) pueden validar si el contexto ambiental y del usuario permite interpretar la entrada de voz como intento de interacción:  
  - Ruido ambiental aceptable (`ENV_NOISE_LEVEL < threshold`)  
  - Usuario identificado o sin restricciones de privacidad  
  - Micrófono operativo y sin fallos recientes

---

## 4. Detonación por hotword

- **Evento alternativo:** `EVT_WAKEWORD`  
  En sistemas con hotword persistente habilitada, este evento puede llevar directamente al estado `Escucha` si se detecta fuera de interacción previa.

---

## Consideraciones adicionales

- El sistema no debe entrar en `Escucha` si existe un evento activo `CMD_INHIBIR_MIC`.
- La transición puede ser denegada si la última interacción terminó en error de audio o reconocimiento.
