# Tabla: `privacidad`

## 1. Descripción Funcional
La tabla `privacidad` almacena los niveles de privacidad de los usuarios en NORA. Permite gestionar qué funcionalidades pueden ser activadas o desactivadas según la configuración de privacidad del usuario. Esto incluye el control sobre el acceso a los datos personales, la grabación de voz, la detección de presencia, y otras funciones sensibles que requieren permisos explícitos del usuario.

## 2. Estructura de la Tabla
| Campo           | Tipo      | Restricciones     | Descripción                                               |
|-----------------|-----------|-------------------|-----------------------------------------------------------|
| `usuario_id`    | INTEGER   | PK, FK            | Identificador del usuario asociado (referencia a `usuarios.id`) |
| `clave`         | TEXT      | NOT NULL          | Nombre de la opción de privacidad (ej. 'grabar_voz', 'modo_privado') |
| `valor`         | TEXT      | NOT NULL          | Valor de la opción (por ejemplo, 'true', 'false', o valores numéricos) |
| `ultima_modificacion` | DATETIME | NOT NULL      | Fecha y hora de la última modificación del parámetro de privacidad |

## 3. Relaciones
- Relacionada con la tabla `usuarios` mediante `usuario_id` (FK).
- Consultada por `voz/`, `gui/`, `interfaz/`, y `datos/` para aplicar configuraciones de privacidad al usuario.

## 4. Ejemplos de Consulta SQL
```sql
-- Establecer configuración de privacidad para grabar voz
INSERT INTO privacidad (usuario_id, clave, valor, ultima_modificacion)
VALUES (1, 'grabar_voz', 'false', datetime('now'));

-- Consultar configuraciones de privacidad para un usuario
SELECT * FROM privacidad WHERE usuario_id = 1;

-- Actualizar la configuración de privacidad de un usuario
UPDATE privacidad SET valor = 'true' WHERE usuario_id = 1 AND clave = 'modo_privado';
```

## 5. Observaciones
- Cada clave de privacidad debe ser gestionada adecuadamente para garantizar que el usuario tenga control sobre qué datos se recopilan o procesan.

- Los valores en valor pueden ser booleanos (para opciones como 'true'/'false') o numéricos, dependiendo del tipo de configuración.

- Se sugiere que el sistema de privacidad sea flexible y escalable para agregar nuevas opciones según se añadan nuevas funcionalidades o módulos.

## 6. Versión y Mantenimiento
- Versión inicial: v1.0

- Última revisión: 2025-05-04

- Responsable técnico: privacidad/, gui/, datos/

> Esta tabla es crucial para garantizar que NORA respete las preferencias de privacidad del usuario y ofrezca un control granular sobre los datos personales.