# Acciones realizadas – Estado: Escucha

Durante el estado **Escucha**, NORA activa y prioriza su canal auditivo para detectar, capturar e interpretar comandos de voz emitidos por el usuario. Este estado se caracteriza por su sensibilidad al entorno sonoro y por su rol como puerta de entrada a la interacción verbal estructurada.

---

## 1. Activación de entrada de voz

- Activación del módulo `voz/` en modo escucha (`listen_active = True`)
- Inicialización del detector de actividad de voz (VAD)
- Monitoreo continuo del nivel de señal, duración, y pausas

---

## 2. Preprocesamiento de audio

- Grabación de audio en buffer temporal para análisis posterior si se detecta voz válida
- Normalización del volumen de entrada y supresión de ruido (si disponible)
- Identificación opcional del hablante mediante perfil vocal (`voice_profile_match`)

---

## 3. Feedback visual y expresivo

- Iluminación del LED RGB en azul tenue o animación tipo “onda auditiva”
- Cambio de expresión facial en pantalla para indicar “modo escucha” (por ejemplo, oídos activos, mirada centrada)
- Posicionamiento estable del servomotor (si aplica), para mantener orientación hacia el usuario

---

## 4. Temporización y control de contexto

- Inicio de temporizador de espera de voz (`t_listen_timeout`)
- Si se detecta una voz válida, se emite `EVT_SPEECH_RECOGNIZED`  
- Si no se detecta voz en el tiempo configurado, se emite `EVT_LISTEN_TIMEOUT`

---

## 5. Evaluación de calidad

- Si se detecta ruido excesivo, el sistema puede pausar brevemente la escucha (`listen_hard_pause`)
- El módulo `voz/` puede emitir `EVT_MIC_FAILURE` si se produce una desconexión, silencio forzado o bloqueo del dispositivo

---

## Indicadores activos del sistema

| Componente        | Estado durante Escucha                       |
|-------------------|-----------------------------------------------|
| Micrófono         | Activado en modo continuo (VAD activo)       |
| Voz               | ASR en espera de activación de reconocimiento|
| LEDs RGB          | Azul tenue o animación de onda auditiva      |
| Pantalla facial   | Expresión atenta / modo escucha              |
| Servos            | Fijos en orientación al usuario              |
