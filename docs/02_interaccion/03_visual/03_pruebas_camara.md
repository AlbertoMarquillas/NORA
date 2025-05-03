# Pruebas de Cámara – Interacción Visual Directa

Este documento recoge los procedimientos recomendados para validar el correcto funcionamiento del subsistema visual de NORA. Las pruebas cubren detección de rostro, postura, zona de interacción y comportamiento frente a condiciones de iluminación y distancia.

---

## 1. Configuración de entorno para pruebas

* **Fondo:** neutro y sin movimiento excesivo.
* **Iluminación:** indirecta, difusa y constante (evitar contraluces).
* **Distancia de usuario:** entre 0.5 m y 2.5 m.
* **Altura de cámara:** entre 1.2 m y 1.5 m, frontal al rostro.

---

## 2. Pruebas de detección de rostro

| Escenario                         | Resultado esperado                                 |
| --------------------------------- | -------------------------------------------------- |
| Usuario frente a cámara (frontal) | Detección estable de rostro                        |
| Usuario gira ligeramente la cara  | Persiste detección; baja confianza si ángulo > 45° |
| Usuario abandona escena           | Rostro deja de detectarse en < 2 s                 |

**Indicador:** evento `EVT_VISUAL_ATTENTION_CONFIRMED`

---

## 3. Pruebas de zona de interacción

| Escenario                  | Zona detectada  | Acciones esperadas            |
| -------------------------- | --------------- | ----------------------------- |
| Usuario se acerca (< 1 m)  | `ZONA_PROXIMA`  | Giro físico, LEDs activos     |
| Usuario entre 1–2 m        | `ZONA_ACTIVA`   | Activación de atención visual |
| Usuario se aleja (> 2.5 m) | `ZONA_INACTIVA` | Desactivación de seguimiento  |

---

## 4. Pruebas de gestos básicos

| Gesto                             | Resultado esperado                       |
| --------------------------------- | ---------------------------------------- |
| Saludo (mano alzada y movimiento) | Evento `EVT_VISUAL_GESTURE_DETECTED`     |
| Postura estática prolongada       | Activación visual sin gestos adicionales |
| Movimiento rápido o brusco        | Ignorado o clasificado como ruido        |

---

## 5. Pruebas con iluminación variable

| Condición           | Efecto esperado                             |
| ------------------- | ------------------------------------------- |
| Luz frontal intensa | Buena detección                             |
| Contraluz directo   | Falla o reducción de confianza en detección |
| Oscuridad parcial   | Solo silueta o no detección de rostro       |

**Recomendación:** activar retroiluminación o LED de apoyo si se detecta baja calidad de imagen.

---

Estas pruebas permiten validar que el sistema de visión de NORA responde de forma coherente ante los escenarios esperables en su contexto de uso real. Su ejecución es clave antes de liberar una nueva versión o reconfigurar parámetros del sistema visual.
