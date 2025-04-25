# Ficha Funcional – Módulo de Modelos de IA

## Nombre del módulo:
`models/`

## Responsabilidad principal:
Gestionar y organizar los modelos de inteligencia artificial utilizados por el sistema NORA. Incluye modelos de visión artificial, procesamiento de voz, reconocimiento de gestos, análisis de emociones y modelado de hábitos de usuario.

## Entradas esperadas:
- Tipo de entrada: solicitudes de inferencia, carga de modelos, parámetros de entrada a modelos
- Fuente: `vision/`, `voz/`, `dialogo/`, `datos/`, `agentes/`
- Formato o protocolo: tensores, matrices de características, texto plano, estructuras JSON

## Salidas generadas:
- Tipo de salida: inferencias, predicciones, clasificaciones, embeddings
- Destinatario: `vision/`, `voz/`, `dialogo/`, `datos/`, `agentes/`
- Ejemplo de salida:
  - Detección de emociones faciales
  - Transcripción de voz
  - Clasificación de gestos o signos

## Módulos relacionados:
- Entrada desde: `vision/`, `voz/`, `dialogo/`, `datos/`, `agentes/`
- Salida hacia: `vision/`, `voz/`, `dialogo/`, `datos/`, `agentes/`
- Comunicación bidireccional con: módulos funcionales que requieran inferencia o entrenamiento incremental

## Dependencias técnicas:
- Librerías externas: `TensorFlow`, `PyTorch`, `scikit-learn`, `MediaPipe`, `transformers`, `sentence-transformers`, `OpenCV`, `numpy`
- Hardware gestionado: GPU opcional para aceleración de inferencias
- Protocolos: carga de modelos estáticos, inferencia en tiempo real, actualización dinámica de modelos

## Notas adicionales:
El módulo `models/` organiza los modelos en carpetas específicas por dominio (visión, voz, gestos, emociones, hábitos), facilitando su carga dinámica y mantenimiento. También contempla la posibilidad de incorporar entrenamiento incremental o fine-tuning basado en los datos recopilados por el sistema.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `models/` para estructurar sus funcionalidades.

- `models_main.py`: Coordinador principal de la gestión y carga de modelos.
- `carga_modelos_vision.py`: Gestión de modelos de visión artificial (detección de objetos, rostros, gestos).
- `carga_modelos_voz.py`: Gestión de modelos de voz (ASR, análisis emocional, hotword detection).
- `carga_modelos_gestos.py`: Gestión de modelos de reconocimiento de gestos y signos.
- `carga_modelos_emociones.py`: Gestión de modelos de análisis de emociones faciales y vocales.
- `carga_modelos_habitos.py`: Gestión de modelos de predicción y análisis de hábitos de usuario.
- `gestion_embeddings.py`: Administración de embeddings generados por modelos (visión, voz, texto).
- `gestion_fine_tuning.py`: Módulo para entrenamiento incremental y ajuste fino de modelos.
- `validacion_modelos.py`: Validación periódica de integridad y rendimiento de modelos cargados.
- `optimizacion_inferencia.py`: Mejoras de rendimiento en la ejecución de inferencias.
- `seleccion_dinamica_modelos.py`: Selección automática del modelo más adecuado según contexto o recursos.
- `actualizacion_remota_modelos.py`: Módulo para actualizar modelos desde repositorios externos o servicios seguros.
- `gestor_versiones_modelos.py`: Gestión de versiones de modelos cargados y rollback seguro en caso de fallo.
- `autoafinado_modelos.py`: Ajuste automático de hiperparámetros y reentrenamiento ligero basado en datos recientes.
- `utils_models.py`: Funciones auxiliares de carga, preprocesamiento de datos y ejecución de inferencias.

