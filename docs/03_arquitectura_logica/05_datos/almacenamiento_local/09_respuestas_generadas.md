# Tabla: `respuestas_generadas`

## 1. Descripción Funcional

La tabla `respuestas_generadas` almacena las salidas físicas o virtuales generadas por NORA durante una interacción. Incluye respuestas auditivas, visuales, faciales, gestuales o combinadas, permitiendo su trazabilidad y análisis posterior. Cada respuesta está vinculada a una `interaccion_id` específica.

## 2. Estructura de la Tabla

| Campo            | Tipo     | Restricciones     | Descripción                                     |
| ---------------- | -------- | ----------------- | ----------------------------------------------- |
| `id`             | INTEGER  | PK, AUTOINCREMENT | Identificador único de la respuesta             |
| `interaccion_id` | INTEGER  | FK NOT NULL       | Referencia a la tabla `interacciones`           |
| `tipo`           | TEXT     | NOT NULL          | Tipo de salida: voz, led, pantalla, gesto, etc. |
| `contenido`      | TEXT     | NOT NULL          | Representación textual de la salida             |
| `timestamp`      | DATETIME | NOT NULL          | Fecha y hora de ejecución                       |

## 3. Relaciones

* FK explícita a `interacciones.id`
* Leída desde `gui/`, `voz/`, `interfaz/`, `sistema/`, `datos/`

## 4. Ejemplos de Consulta SQL

```sql
-- Registrar respuesta de voz
INSERT INTO respuestas_generadas (interaccion_id, tipo, contenido, timestamp)
VALUES (12, 'voz', 'Encantada de ayudarte.', datetime('now'));

-- Obtener respuestas de tipo visual
SELECT * FROM respuestas_generadas WHERE tipo = 'led';
```

## 5. Observaciones

* El campo `contenido` puede contener texto, códigos de color, identificadores de animación, etc.
* Permite analizar qué respuesta se generó ante un estímulo determinado.
* Se recomienda mantener esta tabla como log histórico, no volátil.

## 6. Versión y Mantenimiento

* **Versión inicial:** v1.0
* **Última revisión:** 2025-05-04
* **Responsable técnico:** `voz/`, `interfaz/`, `gui/`, `datos/`

---

> Esta tabla permite documentar, visualizar y evaluar el comportamiento expresivo de NORA a lo largo del tiempo o por interacción.
