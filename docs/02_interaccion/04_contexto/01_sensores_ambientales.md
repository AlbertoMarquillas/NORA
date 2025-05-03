# Sensores Ambientales – Interacción Contextual o Ambiental

Este documento detalla los sensores encargados de captar las condiciones del entorno físico de NORA, así como su integración en el sistema y los eventos que pueden desencadenar. Cada sensor debe operar de forma no bloqueante, con lectura periódica y respuesta asíncrona según los umbrales definidos.

---

## 1. Sensor de luminosidad (LDR o fotodiodo)

**Objetivo:** Detectar nivel de luz ambiental para ajustar el comportamiento visual de NORA.

* **Conexión:** ADC o divisor resistivo en GPIO analógico
* **Módulo:** `sensores/contexto_luz.py`
* **Frecuencia de lectura:** 1 Hz
* **Umbral de activación:** lux < 20 (ambiente oscuro)
* **Evento generado:** `EVT_CONTEXT_LOW_LIGHT`

---

## 2. Sensor de temperatura y humedad (DHT22)

**Objetivo:** Monitorizar el confort ambiental y detectar condiciones anómalas.

* **Conexión:** GPIO con protocolo de un solo hilo
* **Módulo:** `sensores/ambiente.py`
* **Frecuencia de lectura:** 1 vez cada 5 s
* **Eventos generados:**

  * `EVT_CONTEXT_TEMP_HIGH` (temp > 30 °C)
  * `EVT_CONTEXT_HUMID_LOW` (hum < 30 %)

---

## 3. Sensor de ruido ambiental (micrófono analógico o digital)

**Objetivo:** Detectar nivel de sonido ambiental no dirigido a NORA.

* **Conexión:** ADC o bus I2S (según modelo)
* **Módulo:** `sensores/ambiente.py`
* **Frecuencia de lectura:** 10 Hz (media móvil)
* **Umbral configurable:** RMS > 70 dB
* **Evento generado:** `EVT_CONTEXT_NOISE_HIGH`

---

## 4. Sensor PIR o radar Doppler (presencia secundaria)

**Objetivo:** Detectar movimiento pasivo fuera del campo visual directo.

* **Conexión:** GPIO digital
* **Módulo:** `sensores/contexto_mov.py`
* **Frecuencia de muestreo:** evento por interrupción
* **Evento generado:** `EVT_CONTEXT_MOTION_DETECTED`

---

## 5. Recomendaciones generales

* Todos los sensores deben registrarse al inicio del sistema.
* Las condiciones deben evaluarse mediante `agentes/contexto.py` para evitar falsas alarmas.
* Los umbrales pueden calibrarse dinámicamente si el sistema lo permite.

---

Estos sensores permiten a NORA adaptarse de forma autónoma al entorno físico, generando respuestas adecuadas y anticipando interacciones sin necesidad de intervención directa del usuario.
