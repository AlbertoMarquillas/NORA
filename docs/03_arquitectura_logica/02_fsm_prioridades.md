# Reglas de prioridad en la FSM – NORA

Este documento define el esquema de prioridad entre eventos y transiciones en la máquina de estados finitos (FSM) del sistema NORA. Su objetivo es garantizar una resolución determinista cuando múltiples eventos ocurren simultáneamente o en condiciones de competencia.

---

## 1. Principios generales

* La FSM opera en modo síncrono y transaccional.
* Se evalúan todos los eventos pendientes en orden de prioridad antes de permitir una transición.
* Las transiciones múltiples nunca se ejecutan en paralelo.
* En caso de conflicto, la prioridad es determinada por las reglas siguientes.

---

## 2. Niveles de prioridad de eventos (orden descendente)

| Nivel | Evento / Categoría                               | Descripción                             |
| ----- | ------------------------------------------------ | --------------------------------------- |
| 1     | `EVT_MODULE_FAILURE`, `EVT_PROCESS_FAILURE`      | Errores técnicos o de interpretación    |
| 2     | `EVT_SPEECH_RECOGNIZED`, `EVT_GESTURE_COMMAND`   | Entrada interpretada como válida        |
| 3     | `EVT_SPEECH_START`, `EVT_ATTENTION_CONFIRMED`    | Señales que indican inicio de intención |
| 4     | `EVT_NFC_ACTIVATE`, `EVT_WAKEWORD`               | Activadores externos de alta fiabilidad |
| 5     | `EVT_IDLE_TIMEOUT`, `EVT_ATTENTION_LOST`         | Indicadores de ausencia o suspensión    |
| 6     | `EVT_LISTEN_TIMEOUT`, `t_error_recovery_timeout` | Expiraciones de temporizadores internos |
| 7     | `EVT_SCHEDULE_TRIGGERED`                         | Activaciones programadas                |

---

## 3. Reglas de resolución en conflicto

* Si eventos de distinto nivel se presentan en el mismo ciclo, se ejecuta la transición asociada al evento de mayor prioridad.
* Si eventos del mismo nivel compiten, se utiliza el **orden cronológico de recepción** (`timestamp_evento`) como desempate.
* Si dos transiciones tienen igual prioridad y tiempo, se ejecuta la primera en la tabla FSM (`fsm_transiciones.md`), salvo que un agente imponga lo contrario.

---

## 4. Inhibiciones y anulaciones

* Los agentes del sistema pueden emitir comandos de inhibición:

  * `CMD_INHIBIR_ACTIVACION`
  * `CMD_INHIBIR_ESCUCHA`
  * `CMD_CANCEL_LISTENING`
* Un evento inhibido **no puede generar transición** aunque tenga prioridad alta.
* El sistema documenta toda inhibición en el log estructurado con evento `EVT_INHIBITION_TRIGGERED`.

---

## 5. Prioridad de estados en caso de competencia

Cuando el sistema debe decidir entre varios estados destino posibles desde una misma fuente, el orden de preferencia por defecto es:

```
Error > Procesando > Escucha > Atencion > Activado > Reposo
```

Este orden puede ser modulado dinámicamente por los agentes en función del perfil del usuario, condiciones contextuales o histórico de uso.

---

## 6. Pendiente de ampliación

* Soporte para estados emocionales (Ej: `Frustración`, `Curiosidad`)
* Reglas dinámicas ajustables por aprendizaje adaptativo
* Prioridad compuesta en secuencias interrumpidas (diálogos encadenados)
