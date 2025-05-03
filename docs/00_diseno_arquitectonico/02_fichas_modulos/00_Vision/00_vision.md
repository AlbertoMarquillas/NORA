# Ficha Funcional – Módulo de Visión

## Nombre del módulo:
`vision/`

## Responsabilidad principal:
Gestiona la percepción visual del entorno mediante la cámara, incluyendo detección facial, reconocimiento de atención, estimación postural y análisis emocional. Actúa como uno de los canales principales de entrada sensorial del sistema NORA.

## Entradas esperadas:
- Tipo de entrada: flujo de vídeo en tiempo real
- Fuente: cámara CSI o USB conectada a la Raspberry Pi
- Formato o protocolo: frames procesados mediante OpenCV (BGR/Gray), configuraciones en JSON

## Salidas generadas:
- Tipo de salida: eventos perceptivos internos
- Destinatario: `sistema/`, `agentes/`, `interfaz/`
- Ejemplo de salida:
  - `EVT_FACE_DETECTED`
  - `EVT_ATTENTION_GAINED`
  - `EVT_POSTURE_ALERT`
  - `EVT_EMOTION_CHANGED`
  - `EVT_GESTURE_WAVE`

## Módulos relacionados:
- Entrada desde: `sensores/` (configuración ambiental opcional)
- Salida hacia: `agentes/`, `sistema/`, `interfaz/`
- Comunicación bidireccional con: `agentes/` (modulación de comportamiento)

## Dependencias técnicas:
- Librerías externas: `OpenCV`, `MediaPipe`, `NumPy`, `TensorFlow` o `PyTorch` (para modelos)
- Hardware gestionado: cámara CSI o USB
- Protocolos: USB o CSI para captura de vídeo, eventos internos para comunicación

## Notas adicionales:
Algunas subfunciones como reconocimiento de gestos o lenguaje de signos están planificadas para versiones avanzadas. Se contempla delegar tareas específicas a agentes visuales para optimizar recursos o adaptarse al contexto.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `vision/` para estructurar sus funcionalidades.

- `vision_main.py`: Punto de entrada del módulo, orquestación del flujo principal.
- `deteccion_rostro.py`: Funciones de localización y seguimiento facial.
- `postura.py`: Estimación postural y generación de eventos asociados.
- `atencion_visual.py`: Seguimiento de mirada y atención del usuario.
- `emociones.py`: Análisis emocional a partir de expresiones faciales.
- `gestos.py`: Reconocimiento de gestos y señales simbólicas.
- `signos.py`: (Futuro) Detección de lenguaje de signos predefinido.
- `modelo_loader.py`: Carga y gestión de modelos de IA asociados al módulo.
- `eventos_vision.py`: Definición y emisión de eventos específicos del módulo.
- `utils_vision.py`: Funciones auxiliares internas (transformaciones, métricas, normalización, etc.).
- `config_vision.py`: Parámetros configurables centralizados (FPS, ROI, rutas de modelo, etc.).
- `pipeline.py`: Definición del flujo de procesamiento por frame, gestionando ejecución secuencial de funciones especializadas.
- `tracking.py`: Mantenimiento de identificadores faciales persistentes en la escena.
- `reconocimiento_usuario.py`: Asociación de rostro detectado con perfiles conocidos.
- `verificacion_calidad.py`: Comprobación de condiciones mínimas de imagen (iluminación, obstrucción, etc.).

