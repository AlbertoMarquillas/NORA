# Ficha Funcional – `carga_modelos_voz.py`

## Nombre del archivo:
`carga_modelos_voz.py`

## Responsabilidad principal:
Gestionar la carga, inicialización y validación de los modelos de procesamiento de voz utilizados por NORA. Incluye modelos de reconocimiento automático del habla (ASR), detección de palabras clave (hotword detection) y análisis emocional de la voz.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de carga de modelos de voz, parámetros de inicialización, rutas de modelos.
- **Fuente:** `models_main.py`, `voz/`, `agentes/`.
- **Formato o protocolo:** Rutas de archivos de modelo, configuraciones específicas de carga.

## Salidas generadas:
- **Tipo de salida:** Instancias de modelos de voz listos para inferencia.
- **Destinatario:** `voz/`, `agentes/`, `models_main.py`.
- **Ejemplo de salida:**
  - Cargado modelo Whisper para transcripción offline
  - Inicializado clasificador de emociones vocales

## Módulos relacionados:
- **Entrada desde:** `models_main.py`, `voz/`.
- **Salida hacia:** `voz/`, `agentes/`.
- **Comunicación bidireccional con:** `models_main.py` para registro y validación de modelos cargados.

## Dependencias técnicas:
- **Librerías externas:** `TensorFlow`, `PyTorch`, `vosk`, `whisper`, `transformers`, `numpy`, `scipy`.
- **Hardware gestionado:** GPU opcional para inferencia acelerada.
- **Protocolos:** Inferencia de audio, extracción de características (MFCCs, espectrogramas).

## Notas adicionales:
`carga_modelos_voz.py` debe ser capaz de manejar distintos tipos de modelos (de transcripción, de detección emocional, de hotwords) optimizando tiempos de carga y consumo de memoria. Debe contemplar fallback a modelos ligeros en dispositivos de bajo rendimiento y registrar cualquier error de carga para facilitar la depuración del sistema.

