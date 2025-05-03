# Descripción – Interacción Visual Directa

La interacción visual directa en NORA se basa en la percepción en tiempo real de la posición, presencia, atención, gestos o emociones del usuario mediante visión por computador. Es una forma no verbal de comunicación bidireccional que permite a NORA adaptar su comportamiento físico y expresivo al contexto visual percibido.

---

## 1. Objetivo

Detectar e interpretar señales visuales del usuario para generar respuestas físicas, expresivas o de activación. Esta interacción permite iniciar o modular el comportamiento del sistema sin necesidad de comandos explícitos.

---

## 2. Tipos de señales visuales procesadas

* **Presencia frente al sistema** (detección de cuerpo o rostro)
* **Atención visual** (dirección de la mirada, rostro frontal)
* **Gestos simples** (saludo, asentir, levantar la mano)
* **Emociones básicas** (felicidad, sorpresa, enfado – opcional)
* **Distancia al sistema** (zona de interacción)

---

## 3. Componentes del sistema implicados

* `vision/captura.py` – adquisición de imagen de la cámara
* `vision/deteccion_postura.py` – estimación corporal
* `vision/rostro.py` – detección y análisis de rostro
* `agentes/` – análisis del contexto y generación de eventos
* `motor_actuadores.py` – ajuste de orientación física y LEDs

---

## 4. Estados del sistema relacionados

* `STATE_IDLE`: inicio de detección pasiva
* `STATE_ATTENTION`: entrada por presencia visual confirmada
* `STATE_VISUAL_TRACKING`: seguimiento activo del rostro u orientación

---

## 5. Resultados esperados

* Activación o transición de estado por contacto visual
* Reorientación física hacia el usuario
* Confirmaciones visuales (LEDs, pantalla, expresión)
* Generación de eventos de interacción sin comandos

---

La interacción visual directa permite una experiencia más natural, intuitiva y proactiva con NORA, acercándola al comportamiento de un asistente físico con percepción social básica.
