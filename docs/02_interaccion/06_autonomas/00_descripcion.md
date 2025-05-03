# Descripción – Reacciones Autónomas del Sistema

Este documento define el comportamiento de NORA cuando ejecuta acciones de forma autónoma, sin una señal directa del usuario. Estas reacciones se basan en condiciones internas, temporales o contextuales acumuladas, y están diseñadas para mantener la coherencia operativa, la expresividad del sistema y la robustez ante fallos.

---

## 1. Objetivo

Permitir que NORA actúe por iniciativa propia en determinadas situaciones, ya sea para mantener el estado general del sistema, gestionar la falta de interacción o responder a eventos internos relevantes.

---

## 2. Características principales

* **Desencadenadas por condiciones internas o acumuladas** (no por entrada externa inmediata)
* **No requieren interacción explícita del usuario**
* **Tienen prioridad moderada o alta según el evento**
* **Pueden expresarse visual, verbal o estructuralmente**

---

## 3. Tipos de reacciones autónomas

* **Reposo automático:** al detectar inactividad prolongada
* **Repetición o reformulación:** si no se obtiene respuesta a un mensaje
* **Supervisión del sistema:** reinicio parcial o mensajes ante errores
* **Regulación del comportamiento expresivo:** según hora, energía o estado general

---

## 4. Condiciones de evaluación

* Temporizadores activos o contadores internos
* Flags de supervisión periódica (`monitor/`, `estado/`)
* Ausencia de comandos recientes en un intervalo definido
* Diagnóstico de errores en módulos clave

---

## 5. Módulos implicados

* `monitor/` – control de salud del sistema
* `estado/` – FSM central, estados como `STATE_IDLE`, `STATE_SLEEP`
* `expresion/` – adaptación de la expresividad
* `voz/` – mensajes automáticos o repetitivos
* `agentes/` – generación de eventos como `EVT_AUTONOMOUS_...`

---