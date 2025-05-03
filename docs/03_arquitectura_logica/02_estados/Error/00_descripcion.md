# Descripción funcional – Estado: Error

El estado **Error** representa una condición de fallo operacional en la que el sistema NORA ha detectado una anomalía crítica que impide el funcionamiento normal de uno o más módulos. Esta anomalía puede estar relacionada con hardware, software o condiciones del entorno que comprometen la integridad del ciclo de interacción.

Al entrar en este estado, la FSM detiene temporalmente todas las operaciones interactivas y se inicia una rutina de contención supervisada por el módulo `sistema/`, que puede incluir:

- Notificación visual y acústica del error.
- Aislamiento del módulo afectado.
- Intento automático de recuperación si está definido.
- Registro detallado del incidente en el módulo `datos/`.

El estado **Error** tiene carácter transitorio. Su permanencia está condicionada al éxito o fracaso de los intentos de recuperación, o a la intervención manual a través de la interfaz `gui/`.

**Clasificación de errores típicos:**

- **Errores técnicos:** pérdida de cámara, fallo de sensores, fallo de inicialización.
- **Errores lógicos:** estado inconsistente, evento inválido, conflicto de FSM.
- **Errores críticos:** fallo del sistema operativo, pérdida de red (si crítica), sobretemperatura.

Este estado garantiza que el sistema no opere bajo condiciones degradadas que puedan comprometer la experiencia de usuario o la estabilidad funcional.
