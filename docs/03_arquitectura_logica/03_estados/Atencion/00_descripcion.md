# Descripción funcional – Estado: Atencion

El estado **Atencion** representa la fase en la que NORA ha detectado y validado una fuente de atención visual sostenida por parte del usuario. Esta condición activa una respuesta de focalización perceptiva, en la cual el sistema ajusta su orientación, expresión visual y canales sensoriales para optimizar la interacción cercana y dirigida.

Este estado se considera un punto intermedio entre la vigilancia pasiva (`Activado`) y la interacción explícita (`Escucha`, `Procesando`). Su propósito principal es establecer contacto "no verbal" con el usuario, reconociendo la intención de interacción sin requerir todavía una entrada de voz o gesto claro.

Durante **Atencion**, NORA:

- Enfoca visualmente al usuario mediante control de cámara y servomotores.
- Adopta una expresión facial adaptada al contexto (por ejemplo, expresión neutral activa).
- Aumenta la prioridad de los módulos de entrada (`voz/`, `vision/`) en modo escucha.

Este estado permite que los módulos y agentes preparen la transición hacia una conversación natural o una acción específica, evaluando de forma continua si existe intención comunicativa, emocional o funcional.

**Importancia del estado:**

El estado **Atencion** es clave para una interacción fluida y no invasiva, ya que permite que NORA reconozca la disposición del usuario sin exigir un comando inmediato, mejorando la naturalidad en entornos domésticos o educativos.
