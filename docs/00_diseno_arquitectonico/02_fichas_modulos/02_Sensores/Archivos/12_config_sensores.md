# Ficha Específica – `config_sensores.py`

## Nombre del archivo:
`config_sensores.py`

## Responsabilidad principal:
Centralizar todos los parámetros configurables relacionados con el módulo `sensores/`, incluyendo frecuencias de lectura, umbrales de alerta y ajustes de sensibilidad para cada tipo de sensor.

## Entradas esperadas:
- Configuraciones por defecto definidas en el archivo.
- Opcionalmente, sobrescritura de parámetros mediante entrada dinámica (JSON/YAML).

## Salidas generadas:
- Acceso estructurado a las configuraciones activas del módulo `sensores/`.
- Parámetros aplicables por cada submódulo de sensor.

## Funcionalidades principales:
- Definición de:
  - Intervalos de lectura por tipo de sensor.
  - Umbrales críticos de temperatura, humedad, luminosidad, calidad de aire, distancia, etc.
  - Configuración de sensores NFC, BLE, RTC.
- Validación de parámetros de configuración cargados.
- Actualización dinámica de configuraciones si se requiere durante la operación.

## Dependencias técnicas:
- `json`, `yaml` – Lectura y carga de configuraciones.
- `os`, `pathlib` – Gestión de rutas a archivos de configuración.
- `copy` – Manejo seguro de configuraciones en memoria.

