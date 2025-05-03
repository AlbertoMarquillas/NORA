# Tabla: `sensores_log`

## 1. Descripción Funcional
La tabla `sensores_log` almacena las lecturas de los sensores ambientales registrados en NORA. Los datos de sensores como temperatura, humedad, luminosidad, CO2, entre otros, son registrados periódicamente o cuando ocurre un evento relevante. Esta tabla permite la trazabilidad y el análisis de las condiciones ambientales a lo largo del tiempo, siendo útil para entrenar modelos predictivos o para detectar patrones de comportamiento.

## 2. Estructura de la Tabla
| Campo           | Tipo      | Restricciones     | Descripción                                                |
|-----------------|-----------|-------------------|------------------------------------------------------------|
| `id`            | INTEGER   | PK, AUTOINCREMENT | Identificador único de la lectura del sensor               |
| `sensor`        | TEXT      | NOT NULL          | Tipo de sensor (ej. 'temperatura', 'humedad', 'co2', etc.) |
| `valor`         | REAL      | NOT NULL          | Valor medido por el sensor                                 |
| `unidad`        | TEXT      | NOT NULL          | Unidad de medida (ej. '°C', '%', 'ppm')                    |
| `timestamp`     | DATETIME  | NOT NULL          | Fecha y hora de la medición                                 |

## 3. Relaciones
- No tiene relaciones explícitas con otras tablas, pero puede asociarse indirectamente con la tabla `eventos` para registrar condiciones específicas.
- Utilizada por `sensores/` y consultada para análisis históricos o decisiones en tiempo real.

## 4. Ejemplos de Consulta SQL
```sql
-- Insertar nueva lectura del sensor
INSERT INTO sensores_log (sensor, valor, unidad, timestamp) VALUES ('temperatura', 22.5, '°C', datetime('now'));

-- Consultar lecturas de temperatura de los últimos 7 días
SELECT * FROM sensores_log WHERE sensor = 'temperatura' AND timestamp >= datetime('now', '-7 days');

-- Obtener promedio de CO2
SELECT AVG(valor) FROM sensores_log WHERE sensor = 'co2';
```

## 5. Observaciones
- Esta tabla debe ser gestionada cuidadosamente debido a la alta frecuencia de lecturas y volumen de datos que puede generar.

- Se recomienda agregar índices a las columnas sensor y timestamp para optimizar las consultas.

- Es importante asegurar que los sensores estén correctamente calibrados para asegurar la precisión de los datos registrados.

## 6. Versión y Mantenimiento
- Versión inicial: v1.0

- Última revisión: 2025-05-04

- Responsable técnico: sensores/, datos/

> Esta tabla es clave para la recolección de datos ambientales y el análisis a largo plazo dentro de NORA.