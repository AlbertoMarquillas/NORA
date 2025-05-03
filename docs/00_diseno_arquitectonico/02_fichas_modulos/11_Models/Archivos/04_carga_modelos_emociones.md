# Ficha Funcional – `carga_modelos_emociones.py`

## Nombre del archivo:
`carga_modelos_emociones.py`

## Responsabilidad principal:
Gestionar la carga, inicialización y validación de los modelos dedicados al análisis de emociones en NORA. Incluye modelos aplicados tanto a entrada visual (emociones faciales) como a entrada auditiva (emociones vocales).

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de carga de modelos emocionales, parámetros de configuración, rutas de modelos.
- **Fuente:** `models_main.py`, `vision/`, `voz/`, `agentes/`.
- **Formato o protocolo:** Rutas a archivos de modelos, configuraciones de inferencia.

## Salidas generadas:
- **Tipo de salida:** Instancias de modelos de clasificación emocional.
- **Destinatario:** `vision/`, `voz/`, `agentes/`, `models_main.py`.
- **Ejemplo de salida:**
  - Modelo CNN para emociones faciales cargado
  - Modelo LSTM para emociones en voz inicializado

## Módulos relacionados:
- **Entrada desde:** `models_main.py`, `vision/`, `voz/`.
- **Salida hacia:** `vision/`, `voz/`, `agentes/`.
- **Comunicación bidireccional con:** `models_main.py` para control de integridad.

## Dependencias técnicas:
- **Librerías externas:** `TensorFlow`, `PyTorch`, `scikit-learn`, `MediaPipe`, `numpy`, `transformers`.
- **Hardware gestionado:** GPU opcional.
- **Protocolos:** Inferencia basada en imagen o audio.

## Notas adicionales:
`carga_modelos_emociones.py` debe garantizar que los modelos cargados sean apropiados para su tipo de entrada (imagen o audio), y que los resultados de inferencia estén normalizados para su posterior uso en modulación expresiva o toma de decisiones por los agentes del sistema. También debe ser capaz de gestionar diferentes niveles de granularidad emocional (por ejemplo, emociones básicas vs emociones compuestas).