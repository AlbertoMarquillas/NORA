# Relaciones e Integridad Referencial en la Base de Datos `nora.db`

## 1. Objetivo

Definir las relaciones lógicas entre tablas, los vínculos explícitos o implícitos entre registros y las medidas de integridad que deben mantenerse para garantizar consistencia, trazabilidad y seguridad en la base de datos local de NORA.

## 2. Relaciones Principales Entre Tablas

| Tabla origen           | Campo clave        | Tabla destino   | Campo referenciado | Relación     |
| ---------------------- | ------------------ | --------------- | ------------------ | ------------ |
| `notas`                | `usuario`          | `usuarios`      | `id`               | FK opcional  |
| `recordatorios`        | `usuario`          | `usuarios`      | `id`               | FK opcional  |
| `uids`                 | `usuario_asociado` | `usuarios`      | `id` o `nombre`    | FK opcional  |
| `respuestas_generadas` | `interaccion_id`   | `interacciones` | `id`               | FK explícita |
| `privacidad`           | `usuario_id`       | `usuarios`      | `id`               | FK estricta  |
| `alarmas`              | `usuario`          | `usuarios`      | `id`               | FK opcional  |

## 3. Integridad Transaccional

* Cada operación de escritura debe realizarse dentro de una transacción controlada (`BEGIN; ... COMMIT;`).
* Los fallos deben provocar `ROLLBACK` y notificación del módulo `datos/`.

## 4. Reglas de Integridad

* No se permiten registros huérfanos en tablas con FK explícitas (`respuestas_generadas`, `privacidad`).
* En caso de eliminación de un usuario, se deben:

  * eliminar en cascada sus UID (si procede),
  * anonimizar notas y recordatorios,
  * eliminar o desactivar alarmas y configuraciones vinculadas.

## 5. Índices Recomendados

* `notas(timestamp)` para orden temporal
* `eventos(fecha, hora)` para recuperación cronológica
* `uids(uid)` como índice primario (clave única)
* `recordatorios(fecha, hora)` para ejecución programada

## 6. Observaciones Técnicas

* La base de datos debe estar en modo `foreign_keys = ON` por defecto en SQLite.
* Todas las relaciones deben estar documentadas en su tabla correspondiente.
* La integridad se mantiene de forma cooperativa entre módulos que escriben (por diseño de acceso único).

## 7. Futuras Ampliaciones

* Posibilidad de usar `TRIGGERS` para auditoría o propagación automática (p. ej., log de eliminación de usuarios).
* Validaciones cruzadas más estrictas en `configuracion` mediante una tabla de metadatos.

---

> Este documento complementa la documentación individual de cada tabla y garantiza coherencia estructural y semántica en todo el sistema de almacenamiento local de NORA.
