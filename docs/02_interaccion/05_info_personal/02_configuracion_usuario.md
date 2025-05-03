# Configuración del Usuario – Información Personal

Este documento define los parámetros configurables por el usuario en el contexto de la gestión de información personal dentro del sistema NORA. La configuración determina el comportamiento preferido, el acceso a los datos y la forma en que se interpretan ciertas entradas.

---

## 1. Objetivo

Permitir al usuario ajustar el comportamiento del sistema a sus necesidades, con parámetros que influyen en la privacidad, formatos, respuestas y nivel de automatización en la gestión de su información.

---

## 2. Parámetros configurables básicos

| Parámetro                 | Tipo    | Descripción                                           | Valor por defecto |
| ------------------------- | ------- | ----------------------------------------------------- | ----------------- |
| `nombre_usuario`          | string  | Nombre mostrado en saludos o mensajes personalizados  | “Usuario”         |
| `idioma_respuestas`       | string  | Idioma de TTS y respuestas por voz                    | “es”              |
| `modo_privacidad`         | boolean | Activa modo sin confirmaciones verbales               | `false`           |
| `formato_fecha`           | string  | Formato visual de fechas (ej. `DD/MM/YYYY`)           | “DD/MM/YYYY”      |
| `hora_notificaciones`     | hora    | Hora de recordatorio genérico diario (si está activo) | “20:00”           |
| `confirmacion_al_guardar` | boolean | Requiere o no confirmación explícita al guardar datos | `true`            |

---

## 3. Ubicación de configuración

* Archivo: `datos/usuario/configuracion.json`
* Lectura al iniciar el sistema
* Puede ser modificado vía GUI o comandos del tipo “cambia mi idioma a inglés”

---

## 4. Seguridad y validación

* La configuración se valida en cada arranque
* Parámetros inválidos se sustituyen por valores seguros
* Ciertas configuraciones pueden estar restringidas según el nivel del perfil

---

## 5. Posibles extensiones

* Configuración por perfil NFC o reconocimiento visual
* Varios perfiles de usuario con configuraciones independientes
* Parámetros relacionados con hábitos (frecuencia, ventanas de refuerzo)

---

Esta configuración permite adaptar la experiencia de uso sin comprometer la estructura funcional del sistema, manteniendo modularidad y trazabilidad de cada ajuste aplicado.
