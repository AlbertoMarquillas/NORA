# Tabla de transiciones – FSM del sistema NORA

Este documento resume las transiciones posibles entre los estados operativos del sistema NORA, indicando el evento o condición que provoca cada transición y una observación breve sobre su contexto. La tabla sigue el orden lógico del ciclo de vida del asistente.

| Estado actual | Evento / Condición         | Estado destino | Observaciones                                 |
|---------------|-----------------------------|----------------|-----------------------------------------------|
| Reposo        | NFC válido (`EVT_NFC_ACTIVATE`)       | Activado       | Activación consciente con credencial NFC      |
| Reposo        | Presencia confirmada (`EVT_PRESENCE_CONFIRMED`) | Activado       | Activación automática por cercanía            |
| Reposo        | Atención visual (`EVT_ATTENTION_GAINED`)        | Activado       | Despertar visual por contacto sostenido       |
| Reposo        | Hotword (`EVT_WAKEWORD`)     | Escucha        | Entrada directa por voz                       |
| Reposo        | Evento programado (`EVT_SCHEDULE_TRIGGERED`)   | Activado       | Activación por agenda o rutina                |
| Activado      | Voz detectada (`EVT_SPEECH_START`)   | Escucha        | Usuario inicia interacción verbal             |
| Activado      | Atención visual sostenida (`EVT_ATTENTION_CONFIRMED`) | Atencion       | NORA se enfoca en el usuario                  |
| Activado      | Ausencia prolongada (`EVT_IDLE_TIMEOUT`)        | Reposo         | Se suspende por falta de interacción          |
| Activado      | Falla técnica (`EVT_MODULE_FAILURE`)            | Error          | Se detecta un fallo operativo                 |
| Escucha       | Comando válido (`EVT_SPEECH_RECOGNIZED`)       | Procesando     | Se interpreta la entrada verbal               |
| Escucha       | Timeout (`EVT_LISTEN_TIMEOUT`)         | Activado       | No se detecta voz a tiempo                    |
| Escucha       | Falla de micrófono (`EVT_MIC_FAILURE`)          | Error          | El canal auditivo no responde                 |
| Atención      | Voz detectada (`EVT_SPEECH_START`)     | Escucha        | Confirma intención verbal                     |
| Atención      | Gesto reconocido (`EVT_GESTURE_COMMAND`)        | Procesando     | Se interpreta una entrada visual              |
| Atención      | Ausencia visual (`EVT_ATTENTION_LOST`)         | Activado       | Se interrumpe la atención del usuario         |
| Procesando    | Acción completada (`EVT_PROCESS_COMPLETED`)    | Activado       | Respuesta emitida, listo para nuevo ciclo     |
| Procesando    | Falla de análisis (`EVT_PROCESS_FAILURE`)       | Error          | No se pudo interpretar correctamente          |
| Error         | Recuperación automática (`EVT_RECOVERY_SUCCESS`) | Activado     | Se restablece funcionamiento tras un fallo    |
| Error         | Timeout estable (`t_error_recovery_timeout`)    | Activado     | Finaliza la espera sin nuevos errores         |
| Error         | Reintento válido (`CMD_FORCE_RESUME`)          | Escucha        | Usuario fuerza nueva interacción              |

---

## Notas

- Todos los eventos están definidos en `sistema/eventos.md`
- Esta tabla podrá ampliarse conforme se implementen subestados o nuevas capacidades (emocionales, adaptativas, etc.)
- Las prioridades en conflicto se resuelven según reglas de resolución FSM documentadas en `fsm_prioridades.md` (en preparación)
