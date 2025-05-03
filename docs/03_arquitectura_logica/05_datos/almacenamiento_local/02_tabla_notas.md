# Tabla: `notas`

## 1. Descripción Funcional

La tabla `notas` almacena los mensajes dictados por el usuario a través del módulo `voz/`, o bien ingresados manualmente desde la interfaz gráfica `gui/`. Estas notas pueden ser solicitadas, consultadas o gestionadas desde el diálogo conversacional o desde la interfaz visual. Su propósito principal es servir como almacenamiento rápido y recuperable de contenidos de voz transcritos a texto o introducidos como texto plano.

## 2. Estructura de la Tabla

| Campo       | Tipo     | Restricciones     | Descripción                               |
| ----------- | -------- | ----------------- | ----------------------------------------- |
| `id`        | INTEGER  | PK, AUTOINCREMENT | Identificador único de la nota            |
| `usuario`   | TEXT     | NULLABLE          | Usuario que creó la nota (voz o interfaz) |
| `contenido` | TEXT     | NOT NULL          | Texto de la nota (dictado o escrito)      |
| `timestamp` | DATETIME | NOT NULL          | Fecha y hora de creación                  |

## 3. Relaciones

* Puede estar vinculada indirectamente a la tabla `usuarios` si se activa la gestión multiusuario.
* Leída/escrita por `voz/`, `gui/`, `dialogo/`, y `datos/`.

## 4. Ejemplos de Consulta SQL

```sql
-- Insertar nueva nota
INSERT INTO notas (usuario, contenido, timestamp) VALUES ('ana', 'Comprar café', datetime('now'));

-- Recuperar últimas 5 notas
SELECT * FROM notas ORDER BY timestamp DESC LIMIT 5;

-- Buscar notas con palabra clave
SELECT * FROM notas WHERE contenido LIKE '%café%';
```

## 5. Observaciones

* No se elimina automáticamente: el sistema debe ofrecer mecanismo manual de borrado o limpieza periódica.
* Las notas pueden visualizarse, leerse en voz alta o exportarse desde `voz/` o `gui/`.
* Se recomienda permitir edición o etiquetado en versiones futuras.

## 6. Versión y Mantenimiento

* **Versión inicial:** v1.0
* **Última revisión:** 2025-05-04
* **Responsable técnico:** `voz/`, `gui/`, `datos/`

---

> Esta tabla forma parte del núcleo funcional del sistema de interacción y registro de notas personales en NORA.
