# Estado del Sistema – Reacciones Autónomas

Este documento describe los estados internos del sistema NORA relevantes para la activación de comportamientos autónomos. El motor de estados (FSM) permite transicionar entre modos operativos según interacción, contexto o evaluación interna, y es responsable de permitir o inhibir respuestas automáticas.

---

## 1. Objetivo del modelo de estados

Mantener una representación clara y dinámica del estado actual de NORA, que regule qué comportamientos están activos, cuáles están bloqueados y cuándo es apropiado ejecutar acciones sin intervención directa del usuario.

---

## 2. Estados relevantes para reacciones autónomas

| Estado            | Descripción                                                         |
| ----------------- | ------------------------------------------------------------------- |
| `STATE_IDLE`      | Espera pasiva; permite detección de presencia o eventos ambientales |
| `STATE_ATTENTION` | Usuario detectado o inicio de interacción visual                    |
| `STATE_DIALOGUE`  | Interacción activa por voz o GUI                                    |
| `STATE_SLEEP`     | Modo de reposo inducido por inactividad o evento de descanso        |
| `STATE_ERROR`     | Estado crítico tras detección de fallo grave                        |

---

## 3. Transiciones automáticas comunes

* `STATE_IDLE → STATE_SLEEP`: tras `timeout_idle`
* `STATE_DIALOGUE → STATE_ATTENTION`: por inactividad conversacional
* `STATE_ERROR → STATE_IDLE`: tras reinicio parcial exitoso

---

## 4. Eventos que disparan cambios de estado

| Evento                        | Transición objetivo                            |
| ----------------------------- | ---------------------------------------------- |
| `EVT_AUTONOMOUS_SLEEP`        | `STATE_IDLE` → `STATE_SLEEP`                   |
| `EVT_AUTONOMOUS_REPEAT_QUERY` | Reejecución de última pregunta o reformulación |
| `EVT_AUTONOMOUS_RESTART`      | `STATE_ERROR` → reinicio y vuelta a `IDLE`     |

---

## 5. Evaluación desde agentes

El módulo `agentes/estado.py` y `monitor/supervisor.py` evalúan:

* Errores no resueltos en módulos clave
* Condiciones de baja actividad prolongada
* Estado prolongado sin cambio funcional

Si alguna condición se cumple, se generan eventos internos que la FSM interpreta para aplicar la transición correspondiente.

---

La correcta gestión del estado interno del sistema es clave para mantener el equilibrio entre proactividad, expresividad y estabilidad operativa en NORA.
