# Tabla: `uids`

## 1. Descripción Funcional

La tabla `uids` almacena los identificadores NFC autorizados para activar o desactivar el sistema NORA. Estos UIDs se obtienen del lector NFC PN532 y se validan localmente mediante esta tabla. Puede ser gestionada desde el módulo `activacion/`, pero también permite visualización y edición desde la interfaz `gui/`.

## 2. Estructura de la Tabla

| Campo              | Tipo     | Restricciones | Descripción                                      |
| ------------------ | -------- | ------------- | ------------------------------------------------ |
| `uid`              | TEXT     | PK            | UID NFC en formato hexadecimal (ej. 'A1B2C3D4')  |
| `usuario_asociado` | TEXT     | NULLABLE      | Nombre del usuario asignado                      |
| `fecha_registro`   | DATETIME | NOT NULL      | Fecha y hora de incorporación a la base de datos |
| `comentario`       | TEXT     | NULLABLE      | Nota descriptiva (ej. "llavero rojo")            |

## 3. Relaciones

* Relación directa con posibles usuarios definidos en `usuarios` (opcional).
* Usada en validación por `sensores/`, `activacion/` y gestionada desde `gui/`.

## 4. Ejemplos de Consulta SQL

```sql
-- Añadir nuevo UID autorizado
INSERT INTO uids (uid, usuario_asociado, fecha_registro, comentario)
VALUES ('A1B2C3D4', 'ana', datetime('now'), 'llavero rojo');

-- Buscar UID existente
SELECT * FROM uids WHERE uid = 'A1B2C3D4';
```

## 5. Observaciones

* Los UIDs son únicos y deben mantenerse en formato hexadecimal limpio.
* No se elimina automáticamente: el sistema debe ofrecer funciones de gestión de seguridad.
* El módulo `datos/` puede ofrecer respaldo de esta tabla cifrado si se requiere.

## 6. Versión y Mantenimiento

* **Versión inicial:** v1.0
* **Última revisión:** 2025-05-04
* **Responsable técnico:** `activacion/`, `gui/`, `datos/`

---

> Esta tabla es crítica para la seguridad del sistema. Su validación correcta determina el acceso físico a las funcionalidades de NORA.
