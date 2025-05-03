# Tabla: `estado_sistema`

## 1. Descripción Funcional
La tabla `estado_sistema` almacena el estado persistente del sistema NORA entre sesiones. Permite guardar la última configuración conocida del sistema y restaurarla tras reinicios o desconexiones, asegurando que el sistema retorne a su estado anterior, con parámetros como el último usuario, el estado de activación o el UID utilizado.

## 2. Estructura de la Tabla
| Campo             | Tipo      | Restricciones     | Descripción                                               |
|-------------------|-----------|-------------------|-----------------------------------------------------------|
| `id`              | INTEGER   | PK                | Identificador único del estado                            |
| `estado_actual`   | TEXT      | NOT NULL          | Estado actual del sistema (ej. 'activo', 'reposo')        |
| `ultimo_uid`      | TEXT      | NULLABLE          | UID del último usuario o dispositivo activado             |
| `timestamp_actualizacion` | DATETIME | NOT NULL | Fecha y hora de la última actualización del estado        |

## 3. Relaciones
- No tiene relaciones explícitas con otras tablas, pero se utiliza para restaurar el estado de los módulos según el valor de `estado_actual` y `ultimo_uid`.
- Utilizada por `sistema/` y consultada por otros módulos como `activacion/` para comprobar el último estado.

## 4. Ejemplos de Consulta SQL
```sql
-- Guardar el estado actual del sistema
INSERT INTO estado_sistema (estado_actual, ultimo_uid, timestamp_actualizacion)
VALUES ('activo', 'A1B2C3D4', datetime('now'));

-- Recuperar el último estado del sistema
SELECT * FROM estado_sistema ORDER BY timestamp_actualizacion DESC LIMIT 1;

-- Actualizar el estado del sistema a 'reposo'
UPDATE estado_sistema SET estado_actual = 'reposo', timestamp_actualizacion = datetime('now') WHERE id = 1;
```

## 5. Observaciones
- Esta tabla es esencial para restaurar el estado entre reinicios o caídas del sistema.

- Puede ser extendida en el futuro para almacenar configuraciones adicionales relacionadas con el estado del sistema.

- El ultimo_uid es particularmente útil para mantener la trazabilidad de los usuarios y dispositivos activados.

## 6. Versión y Mantenimiento
- Versión inicial: v1.0

- Última revisión: 2025-05-04

- Responsable técnico: sistema/, datos/

> Esta tabla garantiza la persistencia y restauración del estado global del sistema NORA.