# Ficha Específica – `signos.py`

## Nombre del archivo:
`signos.py`

## Responsabilidad principal:
Detectar y reconocer patrones específicos del lenguaje de signos predefinido en usuarios que utilicen esta modalidad de comunicación, ampliando las capacidades de accesibilidad e inclusión de NORA.

## Entradas esperadas:
- Frame de vídeo preprocesado (imagen BGR o RGB).
- Puntos clave de las manos, brazos y postura corporal (keypoints) extraídos previamente.
- Configuraciones dinámicas (diccionario de signos activos, sensibilidad de reconocimiento).

## Salidas generadas:
- Signo reconocido: palabra o expresión correspondiente al gesto manual detectado.
- Nivel de confianza de la interpretación.
- Eventos asociados:
  - `EVT_SIGN_DETECTED`

## Funcionalidades principales:
- Análisis secuencial de posiciones y movimientos de manos y brazos.
- Comparación de la secuencia detectada contra un conjunto de signos predefinidos.
- Tolerancia configurable a errores parciales en la formación de signos.
- Emisión de eventos internos cuando se reconoce un signo válido.

## Dependencias técnicas:
- `OpenCV` – Procesamiento de imágenes.
- `MediaPipe` – Detección precisa de keypoints de manos y brazos.
- `TensorFlow` o `PyTorch` – (opcional) uso de modelos de clasificación de secuencias complejas.
- `NumPy` – Procesamiento y análisis de trayectorias de keypoints.

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

