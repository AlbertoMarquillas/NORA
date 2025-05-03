# Condiciones de entrada – Estado: Reposo

El sistema NORA entra en el estado **Reposo** cuando se determina que no existe intención inmediata de interacción, y las condiciones contextuales justifican la desactivación parcial o total de los módulos operativos. Esta decisión puede derivarse de eventos de inactividad, comandos explícitos o estados de error resueltos.

---

## 1. Inactividad prolongada

- **Evento:** `EVT_IDLE_TIMEOUT`  
  Generado por el módulo `sistema/` tras un período de inactividad superior a un umbral definido (`T_IDLE_MAX`).  
  No se han detectado eventos relevantes como voz, presencia o atención sostenida.

---

## 2. Finalización del ciclo de interacción

- **Evento:** `EVT_SESSION_CLOSED`  
  Emitido por el módulo `sistema/` o `agentes/` tras determinar que la sesión ha concluido correctamente.  
  Esto puede incluir confirmación verbal del usuario, o finalización de una rutina.

---

## 3. Transición desde error recuperado

- **Evento:** `EVT_RECOVERY_SUCCESS` o `CMD_FORCE_REPOSO`  
  Tras resolver un estado `Error`, si no se requiere retorno inmediato a `Activado`, se permite transición directa a `Reposo`.

---

## 4. Comando explícito de suspensión

- **Comando:** `CMD_SUSPENDER_SISTEMA`  
  Emitido desde la interfaz `gui/` o desde un perfil programado de descanso.  
  Permite la entrada voluntaria al estado de reposo bajo demanda del usuario.

---

## Consideraciones adicionales

- Los módulos `voz/` y `vision/` pueden quedar en vigilancia mínima (modo latente), si se define en la configuración del perfil.
- La FSM debe confirmar que no hay procesos en curso (`FSM_BUSY = False`) antes de autorizar la entrada a este estado.
- Puede coexistir con estados energéticos de bajo nivel (ej. "sleep mode") si el hardware lo soporta.
