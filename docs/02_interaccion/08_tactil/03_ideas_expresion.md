# Ideas de Expresión – Interacción Táctil Directa

Este documento propone posibles respuestas expresivas de NORA al detectar interacción táctil, reforzando la comunicación mediante efectos físicos, visuales o sonoros. Las respuestas deben ser inmediatas, coherentes con el contexto y fácilmente interpretables por el usuario.

---

## 1. Objetivo

Ofrecer retroalimentación clara y atractiva tras un gesto físico, para confirmar su recepción y reforzar el vínculo entre acción y reacción.

---

## 2. Canales expresivos posibles

| Canal             | Medio asociado              | Tipo de expresión                    |
| ----------------- | --------------------------- | ------------------------------------ |
| Visual            | LEDs, pantalla              | Cambio de color, ícono, animación    |
| Sonoro            | Altavoz, buzzer             | Sonido breve de confirmación o error |
| Motor             | Giro, vibración, movimiento | Orientación leve o vibración         |
| Facial (pantalla) | Ojos digitales              | Parpadeo, sonrisa, sorpresa          |

---

## 3. Ejemplos por tipo de gesto

| Gesto detectado   | Expresión recomendada                               |
| ----------------- | --------------------------------------------------- |
| Toque simple      | LED parpadea una vez + sonido de confirmación       |
| Toque prolongado  | Giro leve + expresión facial pensativa              |
| Doble toque       | Cambiar color del marco o transición animada rápida |
| Deslizamiento     | Movimiento del avatar o scroll en pantalla          |
| Gesto desconocido | Parpadeo de confusión + sonido neutro               |

---

## 4. Reglas generales de diseño

* La respuesta debe ser inmediata (latencia < 300 ms)
* Debe ser coherente con el estado del sistema (no expresar en `STATE_SLEEP` sin reactivación)
* Evitar redundancia si otro canal ya emitió una respuesta clara

---

## 5. Personalización futura

* Permitirá asignar expresiones distintas por usuario o tipo de interacción
* Los efectos podrán definirse en `config/tacto_expresion.json`

---

Estas ideas de expresión contribuyen a dotar de intencionalidad y calidez a la interacción física, mejorando la experiencia perceptiva y la sensación de reciprocidad en el contacto con NORA.
