# Condiciones de entrada – Estado: Error

El sistema NORA entra en el estado **Error** cuando se detecta una condición anómala que compromete el funcionamiento normal de uno o más módulos. Esta transición puede ser directa o forzada, y tiene prioridad máxima en la FSM `sistema/`.

---

## 1. Fallo técnico crítico

- **Evento:** `EVT_MODULE_FAILURE`  
  Emitido por cualquier módulo (`voz/`, `vision/`, `sensores/`, `control/`) al detectar errores de hardware o pérdida de funcionalidad esencial.  
  Ejemplos: desconexión de cámara, fallo del bus I²C, error de inicialización de micrófono, etc.

---

## 2. Error interno en la FSM

- **Evento:** `EVT_STATE_CONFLICT`  
  Generado internamente si se detecta un estado inconsistente, transición no válida o bloqueo lógico en la máquina de estados.

---

## 3. Condición ambiental insegura

- **Evento:** `EVT_ENV_UNSAFE`  
  Reportado por el módulo `sensores/` o `control/` si se exceden umbrales críticos de temperatura, humedad o calidad del aire.

---

## 4. Intervención manual del sistema

- **Comando:** `CMD_FORCE_ERROR_STATE`  
  Emitido desde la interfaz de desarrollo `gui/` para pruebas o control técnico. Puede simular un fallo o forzar evaluación de recuperación.

---

## 5. Falla en procesos de entrada

- **Ejemplo:** `EVT_MIC_FAILURE`, `EVT_CAMERA_TIMEOUT`, `EVT_TRACKING_LOST`  
  Si la entrada sensorial se degrada y el sistema no puede continuar con la interacción, se considera falla operativa.

---

## Reglas adicionales

- Las condiciones anteriores tienen prioridad sobre cualquier transición pendiente.
- Los agentes no pueden inhibir la transición a `Error` una vez que el evento ha sido validado por `control/` o `sistema/`.
- El estado `Error` puede activarse desde cualquier otro estado, incluyendo `Reposo`.
