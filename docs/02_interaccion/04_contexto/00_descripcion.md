# Descripción – Interacción Contextual o Ambiental

La interacción contextual permite que NORA adapte su comportamiento en función del entorno físico y del estado interno del sistema. A diferencia de las interacciones activas, este tipo se basa en la monitorización continua de sensores y condiciones ambientales, sin necesidad de que el usuario emita una señal directa.

---

## 1. Objetivo

Detectar eventos o variaciones relevantes en el entorno que requieran una respuesta visual, sonora o lógica por parte del sistema. Estos cambios pueden influir en la expresividad, estado operativo o nivel de alerta de NORA.

---

## 2. Condiciones monitorizadas

* **Luminosidad ambiental** (fotocélula, sensor de luz)
* **Temperatura y humedad** (sensor DHT22 o similar)
* **Nivel de ruido** (micrófono ambiente o sensor dedicado)
* **Estado interno del sistema** (modo, errores, consumo)
* **Presencia física secundaria** (detector PIR o radar)

---

## 3. Módulos implicados

* `sensores/contexto_luz.py` – lectura de fotodiodo o LDR
* `sensores/ambiente.py` – temperatura, humedad, presión
* `monitor/sistema.py` – salud general, logs, errores críticos
* `agentes/contexto.py` – evaluación de reglas y condiciones
* `nucleo/estado.py` – transición de estado del sistema

---

## 4. Ejemplos de comportamiento reactivo

* **Ambiente oscuro** → activar expresión facial relajada o encender LEDs suaves
* **Ruido elevado** → mostrar incomodidad o entrar en modo silencio
* **Temperatura alta** → advertencia verbal o gestual
* **Error interno** → cambiar expresión facial, registrar evento, enviar alerta

---

## 5. Características del sistema

* Evaluación periódica no intrusiva
* Mecanismo de eventos `EVT_CONTEXT_...` para comunicación entre módulos
* Posibilidad de respuesta combinada (voz, expresión, visual)
* No bloquea otras formas de interacción simultáneas

---

Este tipo de interacción permite a NORA mantenerse sensible a su entorno, ofreciendo respuestas adaptadas que mejoran la experiencia de uso y refuerzan la percepción de inteligencia ambiental.
