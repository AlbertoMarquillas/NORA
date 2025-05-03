# Activación de NORA desde Estado Reposo mediante NFC

## 1. Objetivo

Definir detalladamente el flujo técnico que permite la activación de NORA desde el estado de reposo tras la detección de una etiqueta NFC válida.

## 2. Estado Inicial

* **Estado del sistema:** `STATE_IDLE`
* **Módulos activos:** Solo `sensores/` y `activacion/` escuchando eventos mínimos.
* **Consumo energético:** Mínimo. Se encuentra en espera.

## 3. Evento de Activación

* **Nombre del evento:** `EVT_NFC_UID_DETECTED`
* **Origen:** Módulo `sensores/` (lectura del PN532)
* **Payload:** UID capturado (formato hexadecimal)

## 4. Condición de Validación

* **Verificación:** UID debe coincidir con uno previamente registrado en `datos/`
* **Evento generado tras validación positiva:** `EVT_NFC_UID_VALID`

## 5. Transición de Estado

* **De:** `STATE_IDLE`
* **A:** `STATE_ACTIVE`
* **Responsable:** Módulo `activacion/`, mediante comando a `sistema/`

## 6. Acciones Derivadas

1. Activación de sensores visuales (`vision/`) y auditivos (`voz/`)
2. Activación de módulos de expresividad (`interfaz/`)
3. Emisión de respuesta multimodal:

   * **Visual:** LED verde
   * **Auditiva:** Síntesis de voz: "Sistema activado"
4. Registro del evento en `datos/` (historial de activaciones)

## 7. Notas Técnicas

* La transición puede estar sujeta a condiciones adicionales evaluadas por `agentes/` (ej. contexto horario, perfil activo).
* El sistema puede establecer un retardo mínimo antes de permitir nueva detección NFC para evitar rebotes o doble activación accidental.

## 8. Eventos Generados

* `EVT_NFC_UID_VALID`
* `EVT_STATE_CHANGED`
* `EVT_ACTIVATION_CONFIRMED`

## 9. Seguridad

* UID debe ser validado contra la base de datos local.
* El sistema debe ignorar cualquier UID no registrado.
* Se debe evitar que múltiples activaciones simultáneas causen conflictos.

## 10. Diagrama relacionado

* Ver: `protocolo_nfc.drawio` sección "Activación desde Reposo"
