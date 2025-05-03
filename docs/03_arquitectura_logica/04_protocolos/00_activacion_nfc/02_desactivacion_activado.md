# Desactivación de NORA desde Estado Activado mediante NFC

## 1. Objetivo

Especificar el flujo técnico que permite desactivar el sistema NORA cuando se encuentra en estado activo o en escucha, utilizando el mismo UID NFC previamente validado.

## 2. Estado Inicial

* **Estado del sistema:** `STATE_ACTIVE` o `STATE_LISTENING`
* **Módulos activos:** Todos los funcionales: `voz/`, `vision/`, `interfaz/`, `datos/`, etc.
* **Condición contextual:** Sistema operativo y respondiendo al entorno.

## 3. Evento de Desactivación

* **Nombre del evento:** `EVT_NFC_UID_DETECTED`
* **Origen:** Módulo `sensores/` (lector NFC PN532)
* **Payload:** UID leído

## 4. Condición de Validación

* **Verificación:** El UID leído debe coincidir con el último UID que activó el sistema (mecanismo toggle).
* **Evento generado tras validación positiva:** `EVT_NFC_UID_TOGGLE`

## 5. Transición de Estado

* **De:** `STATE_ACTIVE` / `STATE_LISTENING`
* **A:** `STATE_IDLE`
* **Responsable:** Módulo `activacion/`, comunicando cambio a `sistema/`

## 6. Acciones Derivadas

1. Desactivación secuencial y controlada de módulos:

   * Apagado de `voz/` (ASR, TTS)
   * Apagado de `vision/`
   * Apagado de sensores pasivos (`sensores/`, excepto NFC)
   * Apagado de componentes expresivos (`interfaz/`)
2. Emisión de respuesta multimodal:

   * **Visual:** LED rojo
   * **Auditiva:** "Sistema desactivado"
3. Registro del evento en `datos/` como cierre de sesión.

## 7. Notas Técnicas

* El apagado debe ser ordenado, priorizando:

  1. Finalización de tareas en curso
  2. Desactivación de expresividad
  3. Entrada en reposo físico
* El UID activo debe quedar invalidado hasta una nueva activación explícita.

## 8. Eventos Generados

* `EVT_NFC_UID_TOGGLE`
* `EVT_STATE_CHANGED`
* `EVT_DEACTIVATION_CONFIRMED`

## 9. Seguridad

* Sólo se aceptan UID registrados y activos.
* Prevención de rebotes mediante ventana de bloqueo temporal.
* El sistema debe garantizar cierre seguro de módulos activos.

## 10. Diagrama relacionado

* Ver: `protocolo_nfc.drawio` sección "Desactivación desde Estado Activo"
