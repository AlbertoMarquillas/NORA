# Flujo de Transición a Reposo por Ausencia Visual del Usuario

Este documento define el comportamiento de NORA cuando no se detecta la presencia del usuario durante un periodo prolongado. El sistema se autogestiona para pasar a un estado de reposo energético y funcional sin intervención del usuario, optimizando recursos y manteniendo coherencia conductual.

---

## Nombre del flujo

Transición a reposo por ausencia visual

---

## Estado inicial

**STATE\_ACTIVE\_WAIT** o **STATE\_ATTENTION**

Sistema activo, con visión y expresión habilitadas.

---

## Evento disparador

* No detección de rostro o cuerpo humano durante un intervalo configurado (ej. 60 segundos)

---

## Condición de validación

* Ausencia confirmada durante un umbral de tiempo sin falsas alarmas
* Validación secuencial por `vision/deteccion.py` + `agentes/gestor_tiempo.py`

---

## Acción del sistema

1. Desactivación progresiva de `voz/asr.py` y `vision/camara.py`
2. Apagado gradual o atenuación de `pantalla_facial`
3. Apagado de LEDs o animación neutra de reposo (`led_rgb.py`)
4. Retorno de servos a posición neutral (si aplicable)
5. Emisión opcional de despedida (“Hasta luego”)
6. Transición al estado interno `STATE_SLEEP`

---

## Estado final

**STATE\_SLEEP**

Sistema en reposo, con consumo energético mínimo, esperando reactivación por eventos definidos (NFC, hotword, toque, etc.).

---

## Respuesta multimodal

| Canal      | Respuesta prevista                                 |
| ---------- | -------------------------------------------------- |
| Pantalla   | Ojos cierran lentamente o se apagan                |
| LEDs       | Transición a color neutro o apagado completo       |
| Movimiento | Giro a posición base o central                     |
| Voz        | Opción: “Hasta luego” sintetizado por `voz/tts.py` |

---

## Acciones complementarias

* Registro de evento de entrada a reposo en `logs/estado_sistema.log`
* Envío de `EVT_AUTONOMOUS_SLEEP` a `estado/fsm.py`

---

## Diagrama

El archivo `flujo_ausencia_usuario.drawio` representará la progresión temporal desde la inactividad visual hasta el modo de reposo.

---

Este flujo permite a NORA comportarse de forma eficiente y autónoma ante inactividad prolongada, reforzando su capacidad de autorregulación sin intervención directa del usuario.
