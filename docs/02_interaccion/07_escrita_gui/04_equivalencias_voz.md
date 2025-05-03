# Equivalencias Escrita ↔ Voz – Interacción GUI

Este documento establece las correspondencias funcionales entre los comandos escritos introducidos por el usuario y sus equivalentes verbales. El objetivo es asegurar una experiencia coherente y completa, independientemente del canal de entrada empleado.

---

## 1. Principio de equivalencia funcional

Todo comando o consulta que puede realizarse mediante voz, debe poder replicarse por texto escrito. Esto incluye:

* Comandos de acción directa
* Consultas informativas
* Creación o modificación de datos personales
* Ajustes de configuración

---

## 2. Tabla de equivalencias típicas

| Entrada por voz                 | Entrada escrita equivalente     | Resultado                              |
| ------------------------------- | ------------------------------- | -------------------------------------- |
| “¿Qué hora es?”                 | `que hora es`                   | Respuesta con la hora actual           |
| “Apunta que debo comprar pilas” | `apunta que debo comprar pilas` | Añade nota “debo comprar pilas”        |
| “¿Tengo algo hoy?”              | `tengo algo hoy`                | Consulta de eventos para el día        |
| “Recuérdame beber agua”         | `recuérdame beber agua`         | Crea recordatorio con ese texto        |
| “Enciende la luz”               | `enciende la luz`               | Comando hacia actuador correspondiente |

> El sistema es insensible a mayúsculas, puntuación y tildes en entrada escrita.

---

## 3. Consideraciones técnicas

* `dialogo/interpretador.py` aplica la misma lógica de parsing
* No hay distinción semántica entre texto procedente de voz o GUI
* Los contextos activos son compartidos si el usuario es el mismo

---

## 4. Respuestas equivalentes

* Voz: respuesta sintetizada con TTS
* Texto: salida renderizada por `interfaz_escrita/respuesta.py`

---

## 5. Excepciones

* Algunos comandos pueden requerir interacción multi-turno que en GUI puede resolverse con formularios
* Las confirmaciones pueden mostrarse como botones o diálogos en lugar de mensajes verbales

---

Este sistema de equivalencia garantiza accesibilidad total a las funciones del sistema y refuerza la coherencia de la experiencia del usuario independientemente del medio de interacción preferido.
