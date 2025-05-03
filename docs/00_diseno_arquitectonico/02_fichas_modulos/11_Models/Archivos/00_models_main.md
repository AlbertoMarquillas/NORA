# Ficha Funcional – `models_main.py`

## Nombre del archivo:
`models_main.py`

## Responsabilidad principal:
Coordinar la gestión integral de los modelos de inteligencia artificial utilizados por NORA. Se encarga de la carga, validación, asignación a submódulos y monitorización del estado de los modelos disponibles para inferencias.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de carga de modelo, verificación de integridad, peticiones de inferencia.
- **Fuente:** `vision/`, `voz/`, `dialogo/`, `datos/`, `agentes/`.
- **Formato o protocolo:** Identificadores de modelo, parámetros de carga, solicitudes de validación.

## Salidas generadas:
- **Tipo de salida:** Modelos cargados en memoria, referencias a instancias de modelos, logs de carga y validación.
- **Destinatario:** Submódulos de `models/`, `vision/`, `voz/`, `dialogo/`, `datos/`, `agentes/`.
- **Ejemplo de salida:**
  - Modelo de detección de emociones cargado
  - Modelo de transcripción de voz preparado para inferencia

## Módulos relacionados:
- **Entrada desde:** `vision/`, `voz/`, `dialogo/`, `datos/`, `agentes/`.
- **Salida hacia:** `carga_modelos_vision.py`, `carga_modelos_voz.py`, `carga_modelos_gestos.py`, `carga_modelos_emociones.py`, `carga_modelos_habitos.py`, `gestion_embeddings.py`.
- **Comunicación bidireccional con:** Todos los submódulos de `models/`.

## Dependencias técnicas:
- **Librerías externas:** `TensorFlow`, `PyTorch`, `scikit-learn`, `transformers`, `numpy`, `joblib`.
- **Hardware gestionado:** GPU opcional (para aceleración de inferencias).
- **Protocolos:** Carga de modelos estáticos, control de versiones, validación de integridad.

## Notas adicionales:
`models_main.py` actúa como punto de entrada y coordinador general del ecosistema de modelos de IA de NORA. Debe garantizar la correcta disponibilidad de los modelos antes de su uso, gestionar errores de carga de forma segura, y permitir estrategias de fallback en caso de fallos. Su diseño debe ser modular, extensible y capaz de operar tanto en entornos con aceleración por GPU como sin ella.

