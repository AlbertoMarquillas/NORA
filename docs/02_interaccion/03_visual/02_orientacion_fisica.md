# Orientación Física – Interacción Visual Directa

Este documento describe cómo NORA adapta físicamente su orientación y expresión en función de la información visual percibida. La reactividad del sistema en términos de giro, iluminación o posición busca simular una atención dirigida hacia el usuario, mejorando la percepción de presencia e intención comunicativa.

---

## 1. Objetivo

Reaccionar físicamente al posicionamiento del usuario, girando la cabeza (o cuerpo), activando LEDs direccionales, y adaptando la pantalla o expresión para reflejar atención.

---

## 2. Componentes implicados

* `motor_actuadores.py` – control de servos/motores para orientación
* `leds_rgb.py` – control de color y dirección de iluminación
* `pantalla_estado.py` – expresión facial o indicadores visuales
* `vision/rostro.py` – detección de posición relativa del rostro

---

## 3. Mecanismos de orientación

### a. Detección de ángulo relativo

* Basado en la posición X del centro del rostro (frame horizontal)
* Compensado con zona neutra central (evita sobreoscilación)
* Umbral configurable para iniciar el giro

### b. Acciones posibles

* Giro suave de cabeza (servo)
* Cambio de expresión facial (mirada dirigida)
* LEDs orientados al lado correspondiente

---

## 4. Estados implicados

* `STATE_VISUAL_TRACKING`: seguimiento activo
* `STATE_ATTENTION`: foco breve tras detección
* `STATE_IDLE`: sin respuesta, pero con retorno a posición neutra tras X segundos

---

## 5. Ejemplo de flujo de orientación

```plaintext
[Detección de rostro a la izquierda] 
→ cálculo de desplazamiento 
→ envío a motor_actuadores(giro = -15°) 
→ activación LEDs laterales izquierdos 
→ pantalla muestra expresión enfocada
```

---

## 6. Consideraciones de implementación

* Limitar la frecuencia de correcciones para evitar parpadeo o sobreajuste
* Evitar giro completo si se pierde el rostro (volver a centro)
* Posibilidad de ignorar el seguimiento si el sistema está ocupado

---

La orientación física coordinada con el análisis visual convierte a NORA en un agente con comportamiento reactivo coherente, reforzando la sensación de presencia atenta y personal.
