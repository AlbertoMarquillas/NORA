# Tabla: `usuarios`

## 1. Descripción Funcional
La tabla `usuarios` almacena los perfiles de los usuarios del sistema NORA, permitiendo asociar configuraciones y datos personales con cada usuario. A través de esta tabla, se gestionan las preferencias, interacciones, y configuraciones específicas para cada persona que interactúa con el sistema.

## 2. Estructura de la Tabla
| Campo           | Tipo      | Restricciones     | Descripción                                               |
|-----------------|-----------|-------------------|-----------------------------------------------------------|
| `id`            | INTEGER   | PK, AUTOINCREMENT | Identificador único del usuario                           |
| `nombre`        | TEXT      | NOT NULL          | Nombre del usuario (puede ser genérico o personalizado)   |
| `uid_default`   | TEXT      | FK (opcional)     | UID NFC por defecto para el usuario                       |
| `preferencias`  | TEXT      | NULLABLE          | Datos de preferencias en formato JSON (por ejemplo: volumen, privacidad) |
| `ultimo_acceso` | DATETIME  | NOT NULL          | Fecha y hora del último acceso al sistema                  |
| `admin`         | INTEGER   | DEFAULT 0         | Indicador de si el usuario es administrador (1 = sí, 0 = no) |

## 3. Relaciones
- Puede estar vinculada a la tabla `uids` si se gestionan múltiples usuarios con diferentes identificadores NFC.
- Relacionada con la tabla `configuracion` para la persistencia de preferencias específicas.
- Relacionada con `notas`, `recordatorios`, y otros datos personales generados por el usuario.

## 4. Ejemplos de Consulta SQL
```sql
-- Insertar nuevo usuario
INSERT INTO usuarios (nombre, preferencias, ultimo_acceso, admin) VALUES ('ana', '{"volumen": "80", "modo_privado": "false"}', datetime('now'), 0);

-- Obtener detalles de un usuario por nombre
SELECT * FROM usuarios WHERE nombre = 'ana';

-- Consultar usuarios activos por último acceso
SELECT * FROM usuarios WHERE ultimo_acceso >= datetime('now', '-30 days');
```

## 5. Observaciones
- Los valores en el campo preferencias deben ser validados como JSON válido al ser almacenados.

- Se recomienda implementar funciones para la modificación de preferencias del usuario sin necesidad de acceso directo a la base de datos.

- El uid_default puede ser opcional si se usan múltiples métodos de autenticación.

## 6. Versión y Mantenimiento
- Versión inicial: v1.0

- Última revisión: 2025-05-04

- Responsable técnico: sistema/, gui/, datos/

> Esta tabla es esencial para la personalización y gestión de perfiles de usuario en NORA.