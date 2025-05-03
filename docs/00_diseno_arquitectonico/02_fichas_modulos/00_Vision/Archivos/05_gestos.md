# Ficha Específica – `gestos.py`

## Nombre del archivo:
`gestos.py`

## Responsabilidad principal:
Detectar y clasificar gestos manuales o corporales significativos captados por la cámara, permitiendo interpretar señales simbólicas realizadas por el usuario como parte de la interacción no verbal con NORA.

## Entradas esperadas:
- Frame de vídeo preprocesado (imagen BGR o RGB).
- Puntos clave del cuerpo y de las manos (keypoints) detectados previamente.
- Configuraciones dinámicas (tipo de gestos activos, sensibilidad a detección de movimientos).

## Salidas generadas:
- Gesto detectado: `saludo`, `adiós`, `ok`, `señal de alto`, entre otros.
- Nivel de confianza en la detección del gesto.
- Eventos asociados:
  - `EVT_GESTURE_WAVE`
  - `EVT_GESTURE_OK`
  - `EVT_GESTURE_STOP`

## Funcionalidades principales:
- Detección de manos y posturas corporales utilizando modelos de `MediaPipe Hands` o `Pose`.
- Análisis de secuencias de keypoints para reconocimiento de patrones gestuales.
- Clasificación de gestos simbólicos basados en posiciones y dinámicas de movimiento.
- Filtro de gestos inestables o ambiguos para garantizar la precisión.
- Emisión de eventos internos cuando se confirma un gesto significativo.

## Dependencias técnicas:
- `OpenCV` – Procesamiento de imágenes.
- `MediaPipe` – Detección de manos y poses corporales.
- `NumPy` – Procesamiento de coordenadas y secuencias de movimientos.

# Relación entre `gestos.py` y `signos.py`

El módulo `gestos.py` y el módulo `signos.py` trabajan de manera complementaria para interpretar la comunicación no verbal del usuario, utilizando entradas similares (keypoints de manos, brazos y postura corporal) pero con objetivos y complejidades diferentes:

- `gestos.py` se centra en el reconocimiento rápido de gestos simbólicos simples (por ejemplo, saludo, señal de alto, OK) mediante la evaluación momentánea o casi instantánea de posiciones corporales.
- `signos.py` gestiona la detección y reconocimiento de secuencias gestuales complejas pertenecientes a un lenguaje de signos predefinido, requiriendo un análisis temporal de múltiples frames consecutivos.

Ambos módulos comparten utilidades comunes para:
- Normalización de keypoints.
- Filtrado de ruido posicional.
- Preprocesamiento de secuencias de movimiento.

Cada módulo mantiene su responsabilidad separada:
- `gestos.py` opera de forma continua con baja latencia.
- `signos.py` analiza ventanas temporales y realiza decisiones secuenciales más elaboradas.

Este diseño modularizado permite optimizar recursos y facilitar la escalabilidad del sistema NORA en función de las capacidades requeridas en cada despliegue.

## Comparativa resumen

| Aspecto         | `gestos.py`                   | `signos.py`                      |
|-----------------|--------------------------------|-----------------------------------|
| Propósito       | Interacción rápida             | Comunicación estructurada         |
| Tiempo          | Instantáneo o casi instantáneo | Requiere seguimiento temporal     |
| Complejidad     | Baja-Media                     | Alta                              |
| Uso de IA       | Opcional (mínimo)              | Altamente recomendado             |
| Enfoque técnico | Reglas + clasificación simple  | Modelado secuencial avanzado      |

