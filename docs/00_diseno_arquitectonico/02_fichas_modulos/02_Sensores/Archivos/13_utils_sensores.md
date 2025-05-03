# Ficha Específica – `utils_sensores.py`

## Nombre del archivo:
`utils_sensores.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares comunes para el módulo `sensores/`, facilitando operaciones como la conversión de unidades, validación de datos sensoriales, normalización y filtros básicos de señales.

## Entradas esperadas:
- Datos numéricos de sensores (temperatura, humedad, distancia, luminosidad, calidad del aire).
- Parámetros de normalización, rangos válidos o factores de conversión.

## Salidas generadas:
- Datos sensoriales validados, normalizados o convertidos.
- Indicadores booleanos de validez de lectura.

## Funcionalidades principales:
- Conversión de unidades (por ejemplo, lux → intensidad relativa, ppm → calidad de aire).
- Validación de lecturas dentro de rangos aceptables definidos.
- Aplicación de filtros básicos para suavizado de señales (media móvil, detección de outliers).
- Normalización de datos para comparabilidad y uso interno.
- Cálculos auxiliares para interpretación de sensores analógicos o digitales.

## Dependencias técnicas:
- `numpy`, `scipy` – Cálculos y filtrados básicos.
- `math` – Operaciones matemáticas elementales.
- `json` – Formato de intercambio de datos preprocesados.

