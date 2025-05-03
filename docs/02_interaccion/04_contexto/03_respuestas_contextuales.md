# Respuestas Contextuales – Interacción Contextual o Ambiental

Este documento describe las respuestas que puede generar NORA al detectar eventos contextuales relacionados con el entorno o su propio estado interno. Estas respuestas buscan ser expresivas, relevantes y no intrusivas, adaptándose a la situación sin requerir intervención directa del usuario.

---

## 1. Principios de diseño de respuestas

* **No intrusivas:** no interrumpen flujos activos salvo que el evento sea crítico.
* **Multimodales:** combinan expresión facial, voz, luz o movimiento.
* **Contextuales:** dependen del estado del sistema y del historial reciente.
* **Reversibles:** pueden revertirse automáticamente si el contexto cambia.

---

## 2. Tabla de eventos y respuestas asociadas

| Evento                        | Respuesta principal                          | Canales implicados              |
| ----------------------------- | -------------------------------------------- | ------------------------------- |
| `EVT_CONTEXT_LOW_LIGHT`       | Activar expresión relajada o LEDs suaves     | `pantalla/`, `leds/`            |
| `EVT_CONTEXT_TEMP_HIGH`       | Advertencia verbal: “Hace calor aquí.”       | `voz/`, `pantalla/`, `datos/`   |
| `EVT_CONTEXT_HUMID_LOW`       | Mensaje opcional de sequedad ambiental       | `voz/` (si usuario presente)    |
| `EVT_CONTEXT_NOISE_HIGH`      | Expresión de incomodidad o silencio temporal | `expresion/`, `voz/`, `estado/` |
| `EVT_CONTEXT_MOTION_DETECTED` | Giro leve o parpadeo de LEDs (modo pasivo)   | `motor/`, `leds/`               |
| `EVT_CONTEXT_SYS_FAILURE`     | Expresión de fallo + log + reinicio parcial  | `pantalla/`, `voz/`, `monitor/` |

---

## 3. Lógica de activación de respuesta

* Evaluación en `agentes/contexto.py`.
* Verificación de que el estado del sistema permite la respuesta.
* Si se requiere confirmación (en interacciones activas), se omite respuesta automática.

---

## 4. Prioridad y conflictos

* Eventos críticos tienen prioridad absoluta (sistema, temperatura extrema).
* Eventos menores pueden ser descartados si hay diálogo en curso.
* Mecanismo de cola para postergar respuestas no urgentes.

---

## 5. Ejemplos de combinación

* **Luz baja + silencio** → expresión pensativa + voz suave de aviso
* **Movimiento detectado + error del sistema** → girar y mostrar fallo expresivo

---

Estas respuestas fortalecen la percepción de NORA como un asistente atento, autónomo y sensible al entorno, sin requerir explicitud constante por parte del usuario.
