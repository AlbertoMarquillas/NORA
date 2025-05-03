# Ficha Específica – `sensor_base.py`

## Nombre del archivo:
`sensor_base.py`

## Responsabilidad principal:
Definir una clase base abstracta para estandarizar la implementación de sensores en el sistema NORA, asegurando que todos los sensores compatibles implementen una interfaz común de inicialización, lectura y emisión de eventos.

## Entradas esperadas:
- Parámetros de configuración específicos de cada sensor (frecuencia, umbrales, modos de operación).

## Salidas generadas:
- Lecturas normalizadas de sensores.
- Eventos de detección específicos emitidos mediante métodos comunes.

## Funcionalidades principales:
- Definición de métodos abstractos o plantillas para:
  - `inicializar_sensor()`
  - `leer_sensor()`
  - `generar_evento()`
- Implementación de validaciones básicas de lectura.
- Gestión de tiempos de lectura y frecuencia de actualización.
- Facilitar la integración de nuevos sensores siguiendo un esquema uniforme.

## Dependencias técnicas:
- `abc` – Definición de clases y métodos abstractos.
- `time` – Gestión de tiempos de actualización.
- `datetime`, `json` – Estructuración de datos para eventos emitidos.

