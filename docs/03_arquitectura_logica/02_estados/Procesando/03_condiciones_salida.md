# Condiciones de salida – Estado: Procesando

El estado **Procesando** finaliza una vez que el sistema ha completado la interpretación de la entrada y ha generado una respuesta válida. Las salidas posibles dependen del tipo de acción requerida y del estado del sistema.

---

## 1. Respuesta lista para emisión

- **Evento:** `EVT_PROCESS_COMPLETED`  
  Emitido por el módulo `dialogo/` o por un agente tras haber finalizado la interpretación y planificación de la respuesta.  
  Se desencadena una transición inmediata hacia el estado `Activado`, `Voz`, `Interfaz`, o equivalente.

---

## 2. Acción directa ejecutada

- **Comando generado:** `CMD_ACTUAR`  
  Si la respuesta implica ejecución directa (mover un servo, cambiar expresión, modificar un parámetro), se envía el comando al módulo correspondiente (`interfaz/`, `control/`) y se retorna a `Activado`.

---

## 3. Error durante el procesamiento

- **Evento:** `EVT_PROCESS_FAILURE`  
  Emitido si se produce una excepción, entrada ambigua o inconsistencia en el análisis.  
  Transición directa a `Error`.

---

## 4. Cancelación de proceso

- **Comando:** `CMD_ABORT_PROCESS`  
  Emitido por el módulo `gui/` o por un agente si se considera que la entrada es inválida, redundante o no requiere respuesta.  
  Retorno a `Activado`.

---

## Condiciones adicionales

- En todos los casos, el sistema debe liberar el bloqueo de FSM (`FSM_LOCK = False`) antes de abandonar el estado.
- Si el proceso ha implicado cambios en el perfil, se debe emitir `EVT_PROFILE_UPDATED` antes de transicionar.
- La salida de este estado puede ir acompañada de una expresión visual transitoria (ej. microgesto de comprensión).
