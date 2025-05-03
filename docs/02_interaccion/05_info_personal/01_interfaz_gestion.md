# Interfaz de Gestión – Información Personal

Este documento detalla la interfaz de usuario prevista para la gestión escrita de notas, hábitos y agenda en NORA. Esta vía de interacción complementa la entrada por voz y permite mayor precisión, revisión y control por parte del usuario, especialmente en entornos donde la interacción verbal no sea adecuada.

---

## 1. Objetivo

Proporcionar un entorno gráfico accesible desde dispositivos locales (pantalla integrada o acceso remoto) para consultar y modificar información personal registrada en el sistema.

---

## 2. Funcionalidades previstas

* **Visualización cronológica** de notas y eventos
* **Formulario de entrada rápida** para nuevas notas o tareas
* **Gestión de hábitos**: marcar como cumplido, ver progreso
* **Editor de agenda**: agregar, mover o eliminar eventos
* **Exportación de datos** en JSON o CSV (modo avanzado)

---

## 3. Estructura propuesta (GUI básica)

* **Panel izquierdo**: selector de categoría (`Notas`, `Agenda`, `Rutinas`)
* **Zona central**: contenido filtrado y editable
* **Zona inferior o modal**: entrada de texto, confirmaciones
* **Iconos**: agregar, editar, borrar, marcar como hecho

> En sistemas sin pantalla táctil, se puede acceder mediante navegador desde otro dispositivo conectado a la red local.

---

## 4. Tecnología sugerida

* **Frontend:** Tkinter (modo local) o React (modo web)
* **Backend:** Flask o FastAPI enlazado al módulo `datos/`
* **Almacenamiento:** acceso a estructura `datos/usuario/`

---

## 5. Seguridad y acceso

* Acceso protegido por PIN o ID NFC (si corresponde)
* Control de sesión en modo remoto (token local o IP autorizada)
* Posibilidad futura de perfiles múltiples con permisos diferenciados

---

## 6. Relación con otras interfaces

* **Voz y texto** son equivalentes funcionalmente a la GUI
* **Confirmaciones** pueden mostrarse visualmente aunque se actúe por voz
* **Interacción remota** futura puede extender esta interfaz en paralelo a la local

---

La interfaz de gestión escrita constituye una herramienta esencial para consolidar la utilidad práctica de NORA como asistente organizativo, integrando precisión manual con automatización asistida.
