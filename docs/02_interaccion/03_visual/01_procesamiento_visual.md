# Procesamiento Visual – Interacción Visual Directa

Este documento detalla los procesos internos que permiten a NORA interpretar señales visuales del entorno, centrados en la postura, rostro, atención, gestos y emociones del usuario. La información visual se analiza en tiempo real y genera eventos utilizados por el sistema para modular su comportamiento.

---

## 1. Flujo general de procesamiento visual

```plaintext
[cámara RGB] 
    ↓
vision/captura.py → frame actual
    ↓
→ rostro.py → coordenadas de rostro + atención
→ deteccion_postura.py → keypoints corporales
    ↓
agentes/visual.py → validación de condiciones y eventos
```

---

## 2. Detección de presencia y atención

* Detección de rostro frontal mediante modelo Haar o DNN ligero.

* Condición mínima para generar `EVT_PRESENCIA_VISUAL`:

  * Rostro visible durante N frames
  * Ratio de frontalidad y estabilidad aceptable

* Atención visual validada por:

  * Centroide del rostro dentro de región activa
  * Opción futura: vector de mirada

---

## 3. Postura y gestos

* Se utiliza MediaPipe Pose o alternativa OpenCV+DL para obtener puntos clave.

* Gestos soportados en v1:

  * Saludo (mano elevada con codo extendido)
  * Asentimiento (cabeza baja y subida)
  * Movimiento lateral (detectar giro leve)

* El sistema valida cada gesto durante un rango de tiempo específico para evitar falsos positivos.

---

## 4. Detección de emociones

* Reconocimiento facial de emociones mediante clasificadores entrenados sobre expresiones básicas:

  * Feliz, Triste, Sorprendido, Neutral
* Se evalúa solo si el rostro está bien alineado y centrado
* Se genera `EVT_EMOCION_RELEVANTE` solo si:

  * Detección estable por al menos N frames
  * Estado del sistema permite reacción

---

## 5. Zonas de interacción

* La imagen se divide en zonas (izquierda, centro, derecha, cerca, lejos)
* Permite orientar servos y LEDs de forma contextual
* Ayuda a modular la reactividad en función de la distancia o ángulo del usuario

---

## 6. Resultados del procesamiento visual

* Generación de eventos tipo `EVT_...`
* Actualización de estado visual interno
* Comandos hacia actuadores físicos (`motor_actuadores.py`)
* Registros visuales para depuración (si activado)

El procesamiento visual permite a NORA interpretar señales humanas implícitas y responder de manera coherente sin requerir interacción verbal o táctil directa.
