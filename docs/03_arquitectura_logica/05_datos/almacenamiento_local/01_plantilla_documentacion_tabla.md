# Plantilla Estándar para Documentación de Tablas (Base de Datos NORA)

> Esta plantilla se utilizará para documentar de forma coherente todas las tablas presentes en `nora.db`. Cada archivo `.md` dedicado a una tabla debe seguir esta estructura.

---

## 1. Nombre de la Tabla

`<nombre_tabla>`

## 2. Descripción Funcional

Breve explicación del propósito de la tabla, qué tipo de datos almacena y qué módulo o funcionalidad la utiliza.

## 3. Estructura de la Tabla

| Campo       | Tipo     | Restricciones          | Descripción           |
| ----------- | -------- | ---------------------- | --------------------- |
| `<campo_1>` | `<tipo>` | PK, FK, NOT NULL, etc. | Explicación del campo |
| `<campo_2>` | `<tipo>` |                        |                       |

## 4. Relaciones

* **Claves foráneas:** relaciones con otras tablas (si aplica)
* **Dependencias cruzadas:** módulos o scripts que leen/escriben sobre esta tabla

## 5. Ejemplos de Consulta SQL

```sql
-- Insertar un nuevo registro
INSERT INTO <nombre_tabla> (...) VALUES (...);

-- Obtener los últimos N registros
SELECT * FROM <nombre_tabla> ORDER BY timestamp DESC LIMIT 10;
```

## 6. Observaciones

Notas adicionales sobre particularidades, restricciones de diseño, posibles índices o mecanismos de borrado/caducidad.

## 7. Versión y Mantenimiento

* **Versión inicial:** v1.0
* **Última revisión:** <fecha>
* **Responsable técnico:** \<nombre / módulo>

---

> Todas las tablas del sistema deben seguir este formato para facilitar mantenimiento, integridad y documentación automática futura.
