# Tabla: `recordatorios`

## 1. Descripción Funcional

La tabla `recordatorios` almacena eventos planificados definidos por el usuario. Pueden ser creados mediante comandos de voz (`voz/`) o manualmente desde la interfaz gráfica (`gui/`). Estos eventos incluyen alarmas, rutinas, y recordatorios con fecha, hora y posibles repeticiones. Son gestionados internamente por el sistema para emitir alertas o ejecutar acciones a la hora prevista.

## 2. Estructura de la Tabla

| Campo        | Tipo    | Restricciones     | Descripción                                         |
| ------------ | ------- | ----------------- | --------------------------------------------------- |
| `id`         | INTEGER | PK, AUTOINCREMENT | Identificador único del recordatorio                |
| `titulo`     | TEXT    | NOT NULL          | Título breve del evento                             |
| `fecha`      | DATE    | NOT NULL          | Fecha del evento                                    |
| `hora`       | TIME    | NOT NULL          | Hora exacta del evento                              |
| `repeticion` | TEXT    | NULLABLE          | Frecuencia opcional: diaria, semanal, mensual, etc. |
| `usuario`    | TEXT    | NULLABLE          | Usuario asociado                                    |
| `activo`     | INTEGER | DEFAULT 1         | Estado del recordatorio (1 = activo, 0 = inactivo)  |

## 3. Relaciones

* Puede estar vinculada a `usuarios` para segmentación multiusuario.
* Consultada por `sistema/`, `control/`, `voz/` y `gui/`.

## 4. Ejemplos de Consulta SQL

```sql
-- Insertar recordatorio diario
INSERT INTO recordatorios (titulo, fecha, hora, repeticion, usuario) 
VALUES ('Tomar pastilla', '2025-05-05', '09:00', 'diaria', 'ana');

-- Consultar próximos recordatorios activos
SELECT * FROM recordatorios 
WHERE activo = 1 AND date(fecha) >= date('now') 
ORDER BY fecha, hora LIMIT 10;
```

## 5. Observaciones

* Las repeticiones pueden gestionarse internamente o como referencia textual.
* Se recomienda sincronizar estos eventos con un gestor de tareas del sistema NORA (`control/`).
* El campo `activo` permite marcar recordatorios completados o descartados sin borrarlos.

## 6. Versión y Mantenimiento

* **Versión inicial:** v1.0
* **Última revisión:** 2025-05-04
* **Responsable técnico:** `voz/`, `gui/`, `control/`, `datos/`

---

> Esta tabla forma parte de la lógica de planificación y rutinas personales en NORA.
