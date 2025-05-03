# Privacidad – Gestión de Información Personal

Este documento recoge las directrices técnicas y filosóficas relacionadas con la protección de la privacidad en la interacción entre el usuario y NORA. La gestión de datos personales (notas, hábitos, agenda, rutinas) requiere un tratamiento cuidadoso para garantizar confidencialidad, trazabilidad local y control por parte del usuario.

---

## 1. Principios Fundamentales

* **Privacidad por diseño:** el sistema está concebido para no depender de conexiones externas ni servidores de terceros.
* **Control local:** toda la información personal se almacena y procesa localmente en la unidad principal (Raspberry Pi).
* **No persistencia no autorizada:** no se guardan datos si el usuario no ha emitido un comando o evento explícito de almacenamiento.
* **Visibilidad del usuario:** el usuario puede consultar, editar o eliminar cualquier elemento guardado mediante comandos verbales o interfaz escrita.

---

## 2. Ubicación y formato del almacenamiento

* **Ruta base:** `datos/usuario/`

* **Estructura recomendada:**

  * `notas/` → ficheros `.txt` individuales o JSON con timestamps
  * `agenda/` → entradas por fecha, formato estructurado (ej. SQLite o JSON)
  * `rutinas/` → conjunto de hábitos con estado, frecuencia y últimos registros

* **Formato preferente:**

  * `.json` para estructura jerárquica
  * `.sqlite` para consultas eficientes si el volumen aumenta

---

## 3. Acceso y modificación

* Mediante comandos de voz (“¿Qué tengo hoy?”, “Guarda una nota”) o GUI escrita.
* Validación opcional por usuario registrado (ej. tarjeta NFC o ID persistente).
* En el futuro: integración de perfiles múltiples por ID visual, NFC o credenciales GUI.

---

## 4. Medidas de protección técnicas

* **Acceso por módulo único:** solo el módulo `datos/` puede leer/escribir sobre los archivos.
* **Opcional:** cifrado de archivos sensibles (`gestion_secretos.py`)
* **Logs restringidos:** eventos sensibles no aparecen en logs de depuración salvo que se active modo explícito.
* **Sin transmisión remota:** no se transmite información personal a través de red salvo configuración expresa.

---

## 5. Futuras extensiones

* **Modo confidencial:** ocultar confirmaciones verbales en la gestión de datos sensibles.
* **Sistema de permisos por tipo de dato.**
* **Backup cifrado local.**
* **Restauración autorizada desde GUI con autenticación mínima.**

---

## 6. Relación con módulos del sistema

* `datos/` → único punto de persistencia.
* `dialogo/` → interpreta intención del usuario relacionada con datos.
* `voz/` y `interfaz_escrita/` → canal de entrada.
* `agentes/` → pueden bloquear, confirmar o modificar peticiones en base al contexto.

---

La privacidad en NORA no es una funcionalidad adicional, sino un eje estructural del sistema. Su mantenimiento requiere tanto decisiones arquitectónicas como claridad en los flujos de uso ofrecidos al usuario.
