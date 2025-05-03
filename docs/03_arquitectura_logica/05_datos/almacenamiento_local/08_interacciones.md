# Tabla: `interacciones`

## 1. Descripción Funcional

La tabla `interacciones` almacena sesiones de interacción entre el usuario y el sistema NORA. Una interacción representa un bloque coherente de actividad perceptiva y expresiva, iniciado por el usuario o el entorno, y finalizado automáticamente o por comando. Permite agrupar eventos, entradas, respuestas y datos sensoriales bajo una misma instancia temporal y contextual.

## 2. Estructura de la Tabla

| Campo         | Tipo     | Restricciones     | Descripción                                   |
| ------------- | -------- | ----------------- | --------------------------------------------- |
| `id`          | INTEGER  | PK, AUTOINCREMENT | Identificador único de la interacción         |
| `usuario`     | TEXT     | NULLABLE          | Usuario que inició o participó                |
| `inicio`      | DATETIME | NOT NULL          | Timestamp de inicio                           |
| `fin`         | DATETIME | NULLABLE          | Timestamp de finalización                     |
| `tipo`        | TEXT     | NOT NULL          | Naturaleza: voz, gui, gesto, sensor, NFC...   |
| `descripcion` | TEXT     | NULLABLE          | Texto opcional con resumen o anotación manual |

## 3. Relaciones

* Puede relacionarse con `usuarios`, `respuestas_generadas`, `eventos`, `sensores_log`, etc.
* Es la tabla padre de `respuestas_generadas` mediante `interaccion_id`.

## 4. Ejemplos de Consulta SQL

```sql
-- Iniciar una nueva interacción
INSERT INTO interacciones (usuario, inicio, tipo) VALUES ('ana', datetime('now'), 'voz');

-- Cerrar una interacción
UPDATE interacciones SET fin = datetime('now') WHERE id = 10;

-- Listar interacciones del día
SELECT * FROM interacciones WHERE date(inicio) = date('now');
```

## 5. Observaciones

* Una interacción puede no tener `fin` definido si está en curso.
* El campo `tipo` permite análisis por canal dominante de entrada o salida.
* Útil para análisis de comportamiento, agrupación de datos o control de sesión.

## 6. Versión y Mantenimiento

* **Versión inicial:** v1.0
* **Última revisión:** 2025-05-04
* **Responsable técnico:** `sistema/`, `voz/`, `gui/`, `datos/`

---

> Esta tabla sirve como unidad central de agrupación contextual para la trazabilidad y análisis de la actividad del usuario en NORA.
