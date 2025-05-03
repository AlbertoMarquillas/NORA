# Diseño de Interfaz – Interacción Escrita por GUI

Este documento describe la estructura visual y funcional de la interfaz gráfica que permite la interacción escrita con NORA. El diseño busca ser intuitivo, limpio y adaptable, tanto en su versión local (pantalla integrada) como en su acceso remoto (web).

---

## 1. Objetivo

Diseñar una interfaz clara que permita al usuario escribir comandos, recibir respuestas visuales y acceder a funciones organizativas de forma directa, replicando lo ofrecido por la voz.

---

## 2. Componentes visuales principales

* **Campo de entrada de texto:** para escribir comandos o preguntas
* **Zona de respuesta visual:** muestra la respuesta de NORA
* **Botones de acción rápida:** para notas, agenda, hábitos, ayuda
* **Indicador de estado:** color o icono que muestra el estado actual del sistema
* **Log de conversación (opcional):** permite revisar interacciones anteriores

---

## 3. Flujo visual general

```plaintext
+---------------------------------------------------+
| NORA (Interfaz Escrita)                           |
|---------------------------------------------------|
| [ Estado actual ]                                 |
|                                                   |
| > ¿Qué tengo hoy?                                 |
|   Hoy tienes: cita médica a las 10:30             |
|                                                   |
| [ Campo de entrada ] [Enviar]                     |
+---------------------------------------------------+
```

---

## 4. Tecnologías previstas

* **Modo local:** `Tkinter` o `PyQt` para GUI integrada
* **Modo remoto:** `React` + `Flask/FastAPI` como backend de texto
* **Backend común:** análisis de intención con `dialogo/interpretador.py`

---

## 5. Comportamiento esperado

* El envío de texto ejecuta el mismo flujo que un comando por voz
* El sistema responde visualmente en la misma zona de interfaz
* Se puede integrar con un sistema de historial local

---

Este diseño de interfaz garantiza que la interacción escrita sea tan expresiva y funcional como la verbal, y permite extender NORA a entornos sin microfonía o con requisitos de discreción.
