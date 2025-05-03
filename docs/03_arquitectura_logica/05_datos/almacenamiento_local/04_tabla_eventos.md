# Tabla: `eventos`

## 1. Descripción Funcional

La tabla `eventos` sirve como registro estructurado de sucesos relevantes en el sistema NORA. Incluye activaciones, desactivaciones, errores, transiciones de estado, comandos del usuario y cualquier otro evento que se desee auditar o analizar. Estos eventos pueden ser generados desde cualquier módulo del sistema y consultados desde `gui/` para diagnóstico o visualización histórica.

## 2. Estructura de la Tabla

| Campo         | Tipo    | Restricciones     | Descripción                                      |
| ------------- | ------- | ----------------- | ------------------------------------------------ |
| `id`          | INTEGER | PK, AUTOINCREMENT | Identificador único del evento                   |
| `tipo`        | TEXT    | NOT NULL          | Categoría general del evento (info, error, etc.) |
| `descripcion` | TEXT    | NOT NULL          | Descripción textual del evento                   |
| `fecha`       | DATE    | NOT NULL          | Fecha del evento                                 |
| `hora`        | TIME    | NOT NULL          | Hora del evento                                  |
| `origen`      | TEXT    | NULLABLE          | Módulo que generó el evento (ej. `voz/`, `gui/`) |

## 3. Relaciones

* Sin claves foráneas directas, pero puede asociarse indirectamente con acciones registradas en otras tablas.
* Utilizado por `sistema/`, `voz/`, `activacion/`, `control/`, y `gui/`.

## 4. Ejemplos de Consulta SQL

```sql
-- Insertar un evento de activación
INSERT INTO eventos (tipo, descripcion, fecha, hora, origen)
VALUES ('info', 'Activación por NFC', date('now'), time('now'), 'activacion/');

-- Consultar eventos de error
SELECT * FROM eventos WHERE tipo = 'error' ORDER BY fecha DESC, hora DESC;
```

## 5. Observaciones

* Puede servir como base para sistemas de logging local y depuración.
* Se recomienda limpiar periódicamente los registros antiguos.
* La columna `origen` es útil para trazabilidad, pero no obligatoria.

## 6. Versión y Mantenimiento

* **Versión inicial:** v1.0
* **Última revisión:** 2025-05-04
* **Responsable técnico:** `sistema/`, `gui/`, `control/`, `datos/`

---

> Esta tabla es el núcleo del sistema de trazabilidad y monitoreo interno de NORA.
