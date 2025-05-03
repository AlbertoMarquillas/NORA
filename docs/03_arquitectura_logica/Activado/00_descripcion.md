# Descripción funcional – Estado: Activado

El estado **Activado** representa una condición operacional intermedia en la que el sistema NORA ha salido explícitamente del modo de bajo consumo o reposo, tras validar una fuente legítima de activación. Este estado marca la transición desde un estado pasivo (`Reposo`) a uno de vigilancia activa, pero aún sin iniciar un proceso conversacional o de análisis específico.

Durante este estado:

- El sistema inicializa los módulos funcionales considerados críticos para la interacción (voz, visión, sensores).
- Se habilita la monitorización sensorial con prioridad baja, manteniendo los subsistemas en estado **"ready"**, pero sin activación total de flujo conversacional.
- La FSM principal (`sistema/`) entra en espera de condiciones que habiliten una transición a estados interactivos (`Escucha`, `Atencion`, `Procesando`).

Este estado también permite aplicar una lógica de evaluación previa del entorno por parte de agentes del módulo `/agentes/`, quienes pueden validar condiciones como atención sostenida, intención implícita o presencia continuada.

El estado **Activado** es clave para asegurar que NORA no responde ante estímulos ambiguos, y prepara el sistema para una transición fluida hacia estados de mayor carga cognitiva o expresiva, en función de los eventos captados en el entorno.

**Ejemplos de activación que conducen a este estado:**

- Detección de una tarjeta NFC válida (`EVT_NFC_ACTIVATE`)
- Confirmación de atención visual (`EVT_ATTENTION_GAINED`)
- Detección de la hotword (e.g., “oye NORA”) (`EVT_WAKEWORD`)
