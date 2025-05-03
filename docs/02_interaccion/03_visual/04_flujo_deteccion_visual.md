# Flujo de Detección Visual de Presencia

Este documento describe el flujo en el que NORA detecta visualmente la presencia de un usuario a través de su cámara, ajustando su comportamiento expresivo sin requerir comandos verbales. Esta detección reactiva es clave para mantener la atención contextual y la disponibilidad del sistema.

---

## Nombre del flujo

Detección visual de presencia

---

## Estado inicial

**STATE\_ACTIVE\_WAIT**

El sistema se encuentra activo, con módulos de visión (`vision/camara.py`) y expresión (`expresion/facial.py`) habilitados.

---

## Evento disparador

* Detección de rostro humano o figura corporal por el módulo `vision/deteccion.py`

---

## Condición de validación

* Presencia mantenida durante al menos 1 segundo
* Confirmación de posición frontal o ángulo aceptable

---

## Acción del sistema

1. Cambiar expresión facial a modo “atención”
2. Encender LEDs con pulso tenue para indicar percepción
3. Girar cabeza o servos hacia el usuario (si se dispone de actuadores)
4. Activar `estado.disponible_para_interaccion = True`
5. Emitir evento `EVT_VISUAL_DETECCION_PRESENCIA`

---

## Estado final

**STATE\_ATTENTION**

Sistema preparado para recibir una interacción activa, manteniendo atención pasiva visual.

---

## Respuesta multimodal

| Canal      | Respuesta prevista                           |
| ---------- | -------------------------------------------- |
| Pantalla   | Ojos abiertos, mirada fija, parpadeo leve    |
| LEDs       | Pulso suave azul/blanco                      |
| Movimiento | Orientación facial hacia el rostro detectado |
| Voz        | No se emite voz en esta fase                 |

---

## Acciones complementarias

* Registrar evento en `logs/presencia_visual.log`
* Activar temporizador de disponibilidad (si no hay comando en 20s → volver a `STATE_IDLE`)

---

## Diagrama

El archivo `flujo_deteccion_visual.drawio` ilustrará este flujo desde entrada visual hasta cambio de estado y expresión.

---

Este flujo permite a NORA demostrar una percepción visual reactiva y contextual, anticipando interacciones y reforzando su comportamiento de presencia inteligente.
