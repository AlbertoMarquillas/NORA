# Descripción General – Gestión de Información Personal

La gestión de información personal constituye uno de los pilares funcionales de NORA. A través de esta capacidad, el sistema permite al usuario crear, consultar y modificar contenidos vinculados a su identidad, tales como notas, hábitos, rutinas o entradas de agenda. Esta interacción puede realizarse tanto por voz como mediante la interfaz escrita.

---

## 1. Objetivo

Facilitar al usuario un espacio privado y estructurado para registrar información cotidiana, automatizar seguimientos de actividad personal y acceder de forma contextual a datos relevantes. La arquitectura prioriza la privacidad, la trazabilidad local y la simplicidad de acceso.

---

## 2. Categorías de contenido soportado

* **Notas rápidas:** textos breves de libre contenido, anotados por voz o texto.
* **Eventos de agenda:** fechas con actividades asociadas.
* **Hábitos o rutinas:** actividades recurrentes que se pueden registrar y monitorizar.
* **Recordatorios básicos:** alertas internas que pueden ejecutarse según reglas temporales.

---

## 3. Mecanismos de interacción

* **Entrada por voz:** comandos como “apunta que…” o “¿tengo algo hoy?”
* **Entrada por texto:** formulario o campo escrito en GUI
* **Consultas:** verbales o escritas, con respuesta por voz o pantalla
* **Modificación:** eliminación, edición o actualización de elementos

---

## 4. Principios del diseño

* **Control local de los datos** – sin dependencia de servicios externos
* **Persistencia estructurada** – uso de JSON o SQLite
* **Modularidad** – cada tipo de dato se gestiona por un módulo lógico
* **Interfaz dual** – todas las acciones son accesibles por voz y por GUI escrita

---

## 5. Integración con otros módulos

* `dialogo/` – interpretación de intenciones relacionadas con datos
* `voz/` – entrada (ASR) y salida (TTS) de comandos o confirmaciones
* `interfaz_escrita/` – entrada de texto y visualización de contenido
* `datos/` – módulo central de persistencia, acceso y validación de contenido
* `agentes/` – supervisión de contexto, validación de condiciones

---

Este subsistema dota a NORA de una funcionalidad de tipo organizativo y asistencial, manteniendo coherencia con sus principios de privacidad, personalización y expresividad multimodal.
