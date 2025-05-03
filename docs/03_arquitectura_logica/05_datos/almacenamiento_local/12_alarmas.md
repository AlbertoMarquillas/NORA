# Tabla: `alarmas`

## 1. Descripción Funcional
La tabla `alarmas` almacena las alarmas definidas por el usuario o el sistema, que se activan según condiciones predefinidas. Estas alarmas pueden ser ambientales (por ejemplo, si la temperatura supera cierto umbral), programadas (por hora, día, etc.) o desencadenadas por eventos específicos del sistema. Su propósito es alertar al usuario de situaciones que requieren atención inmediata o acción.

## 2. Estructura de la Tabla
| Campo        | Tipo      | Restricciones     | Descripción                                               |
|--------------|-----------|-------------------|-----------------------------------------------------------|
| `id`         | INTEGER   | PK, AUTOINCREMENT | Identificador único de la alarma                          |
| `tipo`       | TEXT      | NOT NULL          | Tipo de alarma (por ejemplo, 'temporal', 'sensorial')     |
| `condicion`  | TEXT      | NOT NULL          | Condición para activar la alarma (umbral de sensor, hora, etc.) |
| `accion`     | TEXT      | NOT NULL          | Acción a realizar al activarse la alarma (sonido, mensaje, etc.) |
| `estado`     | INTEGER   | DEFAULT 1         | Estado de la alarma (1 = activa, 0 = inactiva)            |
| `usuario`    | TEXT      | NULLABLE          | Usuario asociado a la alarma                              |
| `timestamp`  | DATETIME  | NOT NULL          | Fecha y hora de la última activación o modificación        |

## 3. Relaciones
- Puede estar vinculada a la tabla `usuarios` si se gestionan alarmas personalizadas.
- Consultada por el sistema `control/` y la interfaz `gui/` para permitir al usuario activar, desactivar o modificar alarmas.

## 4. Ejemplos de Consulta SQL
```sql
-- Insertar una nueva alarma
INSERT INTO alarmas (tipo, condicion, accion, estado, usuario, timestamp)
VALUES ('sensorial', 'temperatura > 30', 'activar sonido', 1, 'ana', datetime('now'));

-- Consultar alarmas activas
SELECT * FROM alarmas WHERE estado = 1;

-- Desactivar alarma
UPDATE alarmas SET estado = 0 WHERE id = 5;
```

## 5. Observaciones
- Las alarmas pueden ser gestionadas manualmente desde gui/ o configuradas automáticamente en base a eventos del sistema o condiciones externas.

- El campo condicion puede ser complejo y almacenado como texto, pero se recomienda definir una estructura clara para evitar ambigüedades.

- Se sugiere la implementación de un sistema de notificación para el usuario cuando una alarma es activada.

## 6. Versión y Mantenimiento
- Versión inicial: v1.0

- Última revisión: 2025-05-04

- Responsable técnico: control/, gui/, datos/

> Esta tabla es clave para la gestión de alarmas y alertas del sistema, mejorando la interacción y respuesta de NORA ante condiciones críticas.