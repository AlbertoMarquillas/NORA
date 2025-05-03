# Gestión de Usuarios – Interacción Escrita por GUI

Este documento define el comportamiento previsto del sistema NORA respecto al acceso de usuarios identificados a través de la interfaz gráfica. Incluye el mecanismo de autenticación, segmentación de datos personales y persistencia de sesión para cada usuario.

---

## 1. Objetivo

Permitir que cada usuario acceda de forma segura a su espacio privado de información personal (notas, hábitos, agenda, configuración) mediante un sistema de login escrito, ya sea local o remoto.

---

## 2. Flujo de autenticación previsto

```plaintext
[Inicio del sistema] → [Pantalla de login] → Usuario introduce credenciales
                   ↓
            [Validación] → Acceso a su panel personal de información
```

### Métodos posibles

* **Usuario + contraseña** (local, por GUI)
* **ID NFC** (combinable con interfaz física)
* **PIN temporal** (modo invitado o acceso limitado)

---

## 3. Segmentación de datos

Cada usuario tiene su propio subdirectorio dentro de `datos/usuario/`, por ejemplo:

```plaintext
datos/usuario/laura/
├── notas.json
├── agenda.db
├── habitos.json
├── configuracion.json
```

Esta estructura garantiza la separación y protección de la información entre perfiles.

---

## 4. Gestión de sesión

* La sesión se mantiene activa durante el uso de la GUI
* Puede haber cierre manual o automático tras tiempo de inactividad
* Las sesiones remotas usan token local de sesión con validación básica

---

## 5. Niveles de usuario

| Tipo             | Permisos                                                                |
| ---------------- | ----------------------------------------------------------------------- |
| Usuario estándar | Accede y edita solo su información                                      |
| Usuario admin    | Puede crear/eliminar perfiles, ver logs, modificar configuración global |

---

## 6. Interacción prevista con GUI

* **Pantalla de login inicial** con selección o introducción de usuario
* **Formulario para alta de nuevos usuarios** si el acceso está permitido
* **Panel personalizado** al iniciar sesión, con contenido asociado

---

Este sistema de gestión de usuarios garantiza seguridad básica, organización estructurada de datos y adaptabilidad para entornos compartidos o personales, fortaleciendo la usabilidad y control del sistema NORA.
