# Privacidad – Configuración del Usuario

Este documento complementa el tratamiento general de privacidad del sistema NORA, centrándose en los aspectos específicos vinculados a la configuración del usuario. Establece mecanismos de protección, visibilidad y control de los parámetros configurables por el usuario final.

---

## 1. Visibilidad de la configuración

* Todos los parámetros de configuración son consultables por el usuario mediante comandos como “¿cuál es mi idioma?” o “¿tengo el modo privacidad activado?”
* La interfaz escrita permite revisar todos los ajustes activos en una vista centralizada
* No se requiere acceso root ni privilegios especiales para lectura en modo usuario autenticado

---

## 2. Protección de cambios

* Los cambios en configuración requieren validación explícita por comando verbal o GUI confirmada
* Algunos cambios (modo privacidad, nombre de usuario) pueden estar sujetos a confirmación secundaria si el sistema detecta posible ambigüedad
* En modo compartido (futuro multiusuario), ciertos campos serán protegidos por ID o NFC

---

## 3. Privacidad operacional

* El modo `modo_privacidad = true` evita que se emitan respuestas verbales con información sensible (notas, agenda, hábitos)
* Las operaciones sensibles (como exportar configuración) solo están habilitadas en modo avanzado y con confirmación
* Los accesos y cambios se registran internamente si se habilita `log_confidencial` (modo auditoría)

---

## 4. Supresión o restablecimiento

* El usuario puede solicitar “restablecer mi configuración” para volver a los valores por defecto
* Se puede eliminar de forma segura el archivo `configuracion.json` para forzar regeneración limpia
* Las copias anteriores (si las hubiera) no son conservadas salvo que esté activo el modo de respaldo manual

---

## 5. Relación con otros subsistemas

| Subsistema               | Implicación en privacidad de configuración                 |
| ------------------------ | ---------------------------------------------------------- |
| `voz/`                   | Puede omitir o suavizar respuestas según `modo_privacidad` |
| `interfaz_escrita/`      | Adapta visibilidad de campos según el nivel de usuario     |
| `dialogo/`               | Bloquea intenciones que impliquen exposición no deseada    |
| `datos/configuracion.py` | Módulo central de control de acceso y validación           |

---

Esta política asegura que la configuración personal no solo sea persistente y personalizable, sino también controlada, reversible y segura ante usos no autorizados o contextos no deseados.
