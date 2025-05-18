# 01 - Git y Commits Limpios

Este documento recopila las buenas prácticas que estoy aprendiendo para usar Git de forma profesional, con especial énfasis en los commits semánticos y estructurados.

---

## 1. Commits semánticos

Los commits semánticos siguen una convención clara para estructurar los mensajes y facilitar el control de versiones, revisión de historial y automatización de changelogs.

### 🧩 Formato general

```
<tipo>[opcional alcance]: <descripción breve>
```

**Ejemplo:**

```
feat(voz): añade detección de palabra clave personalizada
```

---

## 2. Tipos comunes

| Tipo       | Descripción                                             |
| ---------- | ------------------------------------------------------- |
| `feat`     | Nueva funcionalidad                                     |
| `fix`      | Corrección de errores                                   |
| `docs`     | Cambios en la documentación                             |
| `style`    | Formato (espacios, indentación, sin cambio funcional)   |
| `refactor` | Refactorización sin cambio funcionalidad externa        |
| `perf`     | Mejora de rendimiento                                   |
| `test`     | Añadir o modificar tests                                |
| `chore`    | Tareas de mantenimiento (builds, scripts, dependencias) |
| `build`    | Cambios relacionados con la construcción o packaging    |
| `ci`       | Cambios en integración continua o workflows automáticos |

---

## 3. Buenas prácticas

* **Escribir en imperativo.** Ejemplo: “¡Añade módulo NFC!”, no “Añadido módulo NFC”.
* **Primera línea ≤ 72 caracteres.**
* **Usar mensajes claros, específicos y enfocados a una tarea.**
* **Evitar commits acumulativos tipo “cambios varios” o “update”.**
* **Referenciar tareas o tickets si se usa Jira o similar.**

---

## 4. Commits con breaking changes

Cuando un cambio rompe compatibilidad, debe indicarse explícitamente:

```
feat(api): elimina endpoint /v1/status

BREAKING CHANGE: Todos los clientes deben usar /v2/status en adelante.
```

---

## 5. Herramientas útiles

* **Commitizen (`cz`)**: interfaz CLI para crear commits guiados.
* **Husky + Commitlint**: fuerza validaciones antes del push.
* **Conventional Changelog**: genera changelogs automáticos.

---

## 6. Ejemplos reales en este proyecto

```
feat(frontend): añade botón de interacción en la landing
fix(rtc): corrige lectura no bloqueante del registro 0x0F
docs(gui): explica estados posibles en el grafo FSM
```

---

## 7. Recursos

* [https://www.conventionalcommits.org](https://www.conventionalcommits.org)
* [https://www.npmjs.com/package/commitizen](https://www.npmjs.com/package/commitizen)
* [https://typicode.github.io/husky](https://typicode.github.io/husky)
* [https://github.com/conventional-changelog/commitlint](https://github.com/conventional-changelog/commitlint)
