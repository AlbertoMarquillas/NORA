# Tabla: `configuracion`

## 1. Descripción Funcional

La tabla `configuracion` actúa como repositorio de parámetros clave-valor que afectan al comportamiento general de NORA. Permite almacenar ajustes persistentes como el volumen, nivel de sensibilidad, modos activos, rutas locales, flags booleanos, entre otros. Estos valores pueden ser consultados o modificados por cualquier módulo o desde la interfaz `gui/`.

## 2. Estructura de la Tabla

| Campo   | Tipo | Restricciones | Descripción                                            |
| ------- | ---- | ------------- | ------------------------------------------------------ |
| `clave` | TEXT | PK            | Nombre del parámetro de configuración                  |
| `valor` | TEXT | NOT NULL      | Valor asociado (interpretado como string, bool o num.) |

## 3. Relaciones

* Tabla independiente, sin claves foráneas.
* Consultada por `sistema/`, `control/`, `voz/`, `gui/`, `datos/` y cualquier módulo configurable.

## 4. Ejemplos de Consulta SQL

```sql
-- Establecer volumen inicial
INSERT INTO configuracion (clave, valor) VALUES ('volumen', '75');

-- Leer valor de un parámetro
SELECT valor FROM configuracion WHERE clave = 'modo_privado';

-- Actualizar parámetro existente
UPDATE configuracion SET valor = 'true' WHERE clave = 'autoinicio';
```

## 5. Observaciones

* Todos los valores se almacenan como texto, pero deben ser interpretados por el módulo que los utilice.
* Se recomienda inicializar esta tabla con valores por defecto en la instalación del sistema.
* Ideal para guardar rutas de acceso, umbrales, flags de depuración o ajustes de usuario.

## 6. Versión y Mantenimiento

* **Versión inicial:** v1.0
* **Última revisión:** 2025-05-04
* **Responsable técnico:** `sistema/`, `gui/`, `datos/`

---

> Esta tabla es esencial para proporcionar persistencia configurable al comportamiento de NORA de forma modular y transparente.
