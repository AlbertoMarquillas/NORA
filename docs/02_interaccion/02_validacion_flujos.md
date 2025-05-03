# Validación de Flujos de Interacción vs Estados del Sistema

Este documento valida que todos los flujos de interacción definidos se alineen correctamente con el modelo de estados operativos del sistema NORA. La revisión garantiza consistencia lógica para una futura implementación del núcleo FSM.

---

## 1. Estados operativos definidos

* **STATE\_SLEEP**: sistema en reposo, consumo mínimo, sin respuesta activa
* **STATE\_IDLE**: sistema encendido, sin interacción ni atención activada
* **STATE\_ACTIVE\_WAIT**: atención activa, listo para interactuar
* **STATE\_ATTENTION**: atención específica a presencia o gesto
* **STATE\_DIALOGUE**: procesamiento activo de entrada de usuario
* **STATE\_ERROR**: error no recuperable inmediato o respuesta fallida

---

## 2. Tabla de validación por flujo

| Flujo                         | Estado inicial      | Estado final            | ¿Válido? | Observaciones                                            |
| ----------------------------- | ------------------- | ----------------------- | -------- | -------------------------------------------------------- |
| Activación por NFC            | `STATE_SLEEP`       | `STATE_ACTIVE_WAIT`     | ✅        | Transición válida desde reposo por evento externo NFC    |
| Interacción por voz           | `STATE_ACTIVE_WAIT` | `STATE_DIALOGUE` → WAIT | ✅        | FSM transita a diálogo y regresa a espera tras respuesta |
| Detección visual de presencia | `STATE_ACTIVE_WAIT` | `STATE_ATTENTION`       | ✅        | Se activa atención visual sin cambiar canal principal    |
| Ausencia prolongada           | `STATE_ATTENTION`   | `STATE_SLEEP`           | ✅        | FSM entra en reposo por inactividad prolongada           |
| Manejo de errores             | `STATE_DIALOGUE`    | `STATE_ERROR` → WAIT    | ✅        | FSM permite transitar brevemente al estado de error      |
| Registro de nota              | `STATE_DIALOGUE`    | `STATE_ACTIVE_WAIT`     | ✅        | Acción ejecutada con retorno al estado activo            |

---

## 3. Evaluación de cobertura

* Todos los estados han sido utilizados al menos en un flujo
* No existen flujos redundantes o inconsistentes
* Las transiciones FSM son reversibles o compensadas cuando es necesario
* No se detectan solapamientos entre flujos: cada uno cubre un caso distinto

---

## 4. Decisiones adicionales

* No se requiere añadir nuevos estados, pero pueden definirse **subestados internos** para FSM avanzada:

  * `STATE_DIALOGUE_WAIT_INPUT`
  * `STATE_DIALOGUE_CONFIRM_ACTION`

* Se sugiere incorporar banderas de contexto (`interaccion_activa`, `atencion_visual`, `usuario_autenticado`) para refinar transiciones sin inflar la FSM

---

## 5. Conclusión

El modelo FSM actual es suficiente para soportar todos los flujos documentados hasta el momento. Su implementación podrá mantenerse clara y robusta, garantizando que las decisiones del sistema sean predecibles y modulables.

Todos los flujos han sido validados sin ambigüedades ni conflictos.
