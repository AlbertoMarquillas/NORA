# Descripción funcional – Estado: Escucha

El estado **Escucha** representa la fase en la que NORA ha sido activada e inicia un proceso de espera activa de comandos verbales del usuario. Durante esta fase, el sistema maximiza la sensibilidad auditiva, reduce el ruido de fondo y monitoriza continuamente la entrada de voz en busca de señales válidas que indiquen intención comunicativa.

Este estado se considera el punto de inicio del canal de entrada verbal en la interacción. Su entrada puede venir precedida de atención visual sostenida (`Atencion`) o directamente de activación (`Activado`) si se ha detectado voz de forma inequívoca.

Durante **Escucha**, el sistema:

- Activa el reconocimiento de voz automático (ASR) y el detector de actividad vocal (VAD).
- Configura los módulos de audio para máxima claridad.
- Adopta un estado visual indicativo de "escucha activa".
- Mantiene el foco visual si procede del estado `Atencion`.

Este estado es sensible al tiempo. Si no se detecta voz válida en un plazo determinado, se revierte a un estado pasivo o intermedio (`Activado`). Si se capta un comando interpretable, se transita a `Procesando`.

**Importancia del estado:**

El estado **Escucha** permite a NORA operar de forma natural, sin necesidad de botones ni interfaces táctiles, mediante la detección directa de la intención verbal. Es esencial para habilitar interacciones fluidas y no invasivas en contextos domésticos o educativos.
