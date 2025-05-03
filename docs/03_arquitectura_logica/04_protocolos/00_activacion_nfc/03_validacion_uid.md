# Validación de UID NFC en el Protocolo de Control de NORA

## 1. Objetivo

Detallar el mecanismo técnico de validación de identificadores únicos (UID) NFC en el sistema NORA para permitir o denegar la activación o desactivación del sistema.

## 2. Entrada del Sistema

* **Dispositivo:** Módulo NFC PN532
* **Formato del dato:** UID en hexadecimal (ejemplo: `0xA1B2C3D4`)
* **Módulo lector:** `sensores/`
* **Evento generado:** `EVT_NFC_UID_DETECTED`

## 3. Proceso de Validación

1. El módulo `sensores/` detecta un UID mediante el lector PN532.
2. Se lanza el evento `EVT_NFC_UID_DETECTED` con el UID como payload.
3. El módulo `activacion/` recibe el evento y solicita validación a `datos/`.
4. El módulo `datos/` verifica si el UID está registrado en la base de datos local (SQLite).
5. Resultado:

   * **UID válido:** se emite `EVT_NFC_UID_VALID`
   * **UID inválido:** se emite `EVT_NFC_UID_INVALID`

## 4. Criterios de Validación

* Coincidencia exacta con entradas válidas de la tabla `usuarios_autorizados`.
* Posibilidad de definir roles o perfiles asociados a cada UID (futuro).

## 5. Seguridad

* No debe haber acceso externo a la base de datos.
* Todos los UID deben ser tratados como sensibles.
* El proceso de validación debe ser atómico y no bloquear el sistema.
* En caso de error en la base de datos, se debe asumir el UID como inválido.

## 6. Eventos Relacionados

* `EVT_NFC_UID_DETECTED`
* `EVT_NFC_UID_VALID`
* `EVT_NFC_UID_INVALID`

## 7. Respuestas del Sistema

* **UID válido:** inicio del flujo de activación/desactivación.
* **UID inválido:** respuesta visual (LED amarillo intermitente) y auditiva ("UID no reconocido").

## 8. Notas Técnicas

* El sistema puede cachear el último UID leído para implementar comportamiento de tipo toggle.
* Los UID pueden tener metadata asociada: nombre, último acceso, nivel de privilegio (no implementado).

## 9. Diagrama Relacionado

* Ver sección de validación UID en `protocolo_nfc.drawio`
