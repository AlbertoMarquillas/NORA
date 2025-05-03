# Estructura General de Almacenamiento de Datos en NORA

## 1. Objetivo

Definir la arquitectura general del sistema de almacenamiento local de datos en NORA, basada en una base de datos SQLite (`nora.db`) que opera en modo completamente offline. Se documentan los tipos de datos almacenados, las tablas principales y su propósito funcional.

## 2. Requisitos Generales

* Sistema de almacenamiento local y autónomo (sin conexión remota).
* Acceso desde los módulos Python mediante la biblioteca `sqlite3`.
* Consultas rápidas, consistencia estructural y trazabilidad.
* Soporte para futuras tareas de análisis, personalización o aprendizaje automático local.

## 3. Tipos de Datos a Almacenar

* **Notas dictadas** por el usuario (vía módulo `voz/`)
* **Recordatorios o hábitos** generados o planificados
* **Eventos relevantes** del sistema (activaciones, errores, cambios de estado)
* **UIDs NFC** autorizadas para interacción
* **Preferencias y configuración** local del sistema
* **Interacciones multimodales** y respuestas generadas
* **Datos de sensores ambientales** registrados de forma estructurada
* **Alarmas**, niveles de privacidad y último estado persistente

## 4. Archivo de Base de Datos

* **Nombre:** `nora.db`
* **Ubicación:** sistema de archivos local dentro de `~/.nora/` o ruta definida en configuración
* **Modo de acceso:** lectura/escritura exclusiva desde proceso principal de NORA

## 5. Tablas Principales

| Tabla                  | Descripción breve                                                  |
| ---------------------- | ------------------------------------------------------------------ |
| `notas`                | Notas dictadas por el usuario, asociadas a un timestamp            |
| `recordatorios`        | Eventos planificados o hábitos con reglas de repetición            |
| `eventos`              | Historial de eventos del sistema, incluyendo activaciones y fallos |
| `uids`                 | Identificadores NFC autorizados localmente                         |
| `configuracion`        | Valores clave-valor de preferencias generales del sistema          |
| `interacciones`        | Registro de interacciones del usuario con NORA                     |
| `respuestas_generadas` | Salidas físicas generadas: voz, luces, rostro, etc.                |
| `usuarios`             | Perfil básico y preferencias del usuario                           |
| `sensores_log`         | Muestras periódicas o puntuales de sensores físicos                |
| `alarmas`              | Definiciones de alarmas activas por condición u horario            |
| `privacidad`           | Niveles de privacidad por usuario y funcionalidad                  |
| `estado_sistema`       | Estado persistente del sistema tras su última sesión               |

## 6. Diagramas y Scripts

* El archivo `09_script_creacion_nora_db.sql` contiene el script de creación completa.
* El diagrama ER correspondiente será generado más adelante como visualización auxiliar (opcional).

## 7. Módulos Python Relevantes

* `datos/gestion_sqlite.py` → Funciones de acceso a la base de datos
* `datos/backup.py` → Gestión de respaldos y restauración
* `utils/sql_helpers.py` → Funciones auxiliares (conexiones, queries seguras)

## 8. Seguridad y Acceso

* Acceso exclusivo desde procesos controlados por NORA.
* Sin sincronización externa ni API de red.
* Los datos son locales, en texto plano o cifrados opcionalmente (por módulo `gestion_secretos.py`)

---

Este documento sirve como índice y referencia de la estructura general de almacenamiento. Cada tabla será documentada de forma independiente siguiendo el estándar definido en `01_plantilla_documentacion_tabla.md`.
