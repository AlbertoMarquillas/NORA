# Ficha Específica – `utils_voz.py`

## Nombre del archivo:
`utils_voz.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares de soporte al módulo `voz/`, incluyendo normalización de audio, generación de espectrogramas, cálculo de métricas acústicas y otras operaciones comunes de preprocesamiento.

## Entradas esperadas:
- Buffers de audio PCM.
- Texto procesado o transcrito.
- Parámetros de transformación o configuración.

## Salidas generadas:
- Buffers de audio normalizados o modificados.
- Espectrogramas generados.
- Métricas de audio extraídas.

## Funcionalidades principales:
- Normalización de volumen de audio.
- Generación de espectrogramas para análisis o visualización.
- Cálculo de RMS, energía, pitch y otras características básicas del audio.
- Conversión entre formatos o tasas de muestreo.
- Limpieza básica de textos transcritos (opcional).

## Dependencias técnicas:
- `numpy`, `scipy` – Procesamiento de señales de audio.
- `matplotlib` (opcional) – Visualización de espectrogramas.
- `soundfile`, `librosa` (opcional) – Manipulación avanzada de audio.

