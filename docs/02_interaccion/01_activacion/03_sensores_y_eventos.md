# Sensores y Eventos – Interacción: Activación del Sistema

Este documento detalla los sensores físicos y lógicos que participan en la detección de eventos de activación, así como la forma en que cada uno genera un evento interpretable por el sistema NORA. La activación no depende de un único canal, sino de un conjunto de fuentes sensoriales redundantes y complementarias.

---

## 1. Sensor ultrasónico HC-SR04

**Función:** Detectar la presencia física del usuario a una distancia inferior a un umbral definido (ej. 100 cm).
**Conexión:** GPIO (TRIG, ECHO)
**Frecuencia de muestreo:** 10–20 Hz (dependiendo del loop de sensores)
**Umbral de activación:** distancia < 100 cm durante > 3 s
**Evento generado:** `EVT_ACTIVATION_PRESENCE_CONFIRMED`

---

## 2. Cámara (entrada visual)

**Función:** Detección de rostro humano y seguimiento de la atención visual mediante un modelo de visión computacional.
**Conexión:** USB o CSI (según cámara)
**Procesamiento:** `vision/` detecta rostro + atención mantenida > X frames
**Evaluación adicional:** validación por agentes de contexto
**Evento generado:** `EVT_ACTIVATION_VISUAL_CONFIRMED`

---

## 3. Módulo NFC (ej. PN532)

**Función:** Detectar la proximidad de una tarjeta o dispositivo NFC válido.
**Conexión:** UART o I2C (según configuración)
**Validación:** UID reconocido por el sistema
**Tiempo de detección:** instantánea tras contacto
**Evento generado:** `EVT_ACTIVATION_NFC_CONFIRMED`

---

## 4. Entrada de audio – micrófono

**Función:** Detección de la hotword configurada (ej. “oye NORA”).
**Conexión:** USB o tarjeta de sonido integrada
**Procesamiento:** módulo `voz/` realiza ASR ligero
**Activación:** requiere coincidencia fonética clara en estado `STATE_IDLE`
**Evento generado:** `EVT_ACTIVATION_VOICE_CONFIRMED`

---

## 5. Botón físico (pulsador GPIO)

**Función:** Activación manual directa por el usuario.
**Conexión:** GPIO con resistencia pull-up/pull-down
**Condición de activación:** pulsación mantenida > 1 segundo
**Evento generado:** `EVT_ACTIVATION_BUTTON_CONFIRMED`

---

## 6. Consideraciones generales

* Todos los sensores deben ser no bloqueantes y trabajar en paralelo.
* Se recomienda incluir antirrebote lógico para entradas físicas (botón).
* La validación por `agentes/` puede suprimir eventos si hay conflictos o condiciones no favorables (ej. ocupación, contexto).
* El sistema registra la fuente de cada activación para trazabilidad.

---

## 7. Módulos implicados

* `activacion/`
* `sensores/`
* `voz/`
* `vision/`
* `agentes/`
* `sistema/`

Cada uno debe poder publicar un evento del tipo `EVT_ACTIVATION_XXX` con los metadatos mínimos necesarios (timestamp, origen, ID usuario si aplica).
