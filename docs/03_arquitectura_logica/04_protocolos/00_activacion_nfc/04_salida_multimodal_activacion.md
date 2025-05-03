# Salida Multimodal de Activación en NORA (Respuesta a UID NFC válido)

## 1. Objetivo

Documentar la respuesta multimodal del sistema NORA tras la activación consciente mediante un UID NFC válido, especificando los canales y formas de salida utilizadas.

## 2. Contexto del Evento

* **Evento desencadenante:** `EVT_NFC_UID_VALID`
* **Estado anterior:** `STATE_IDLE`
* **Estado resultante:** `STATE_ACTIVE`

## 3. Canales de Salida Involucrados

### 3.1. Visual (Hardware: LEDs RGB WS2812 / indicadores GPIO)

* **Color emitido:** Verde sólido
* **Duración:** 1 segundo mínimo
* **Módulo responsable:** `interfaz/`

### 3.2. Auditivo (Hardware: altavoz + amplificador)

* **Mensaje:** "Sistema activado"
* **Motor TTS:** gestionado por `voz/`
* **Librería sugerida:** pyttsx3 o equivalente offline
* **Tiempo de reproducción estimado:** 1.5–2 segundos

### 3.3. Registro Interno (Software: base de datos local)

* **Módulo:** `datos/`
* **Contenido:** Timestamp + UID + evento: `ACTIVACION_EXITOSA`

## 4. Secuencia de Ejecución

1. Se valida el UID.
2. `activacion/` emite `EVT_NFC_UID_VALID`
3. `sistema/` cambia a `STATE_ACTIVE`
4. `interfaz/` activa LED verde
5. `voz/` sintetiza y reproduce el mensaje de activación
6. `datos/` registra el evento

## 5. Consideraciones Técnicas

* Las salidas deben poder ejecutarse de forma concurrente o no bloqueante.
* En caso de fallo de algún canal (p. ej., altavoz desconectado), debe ejecutarse el resto sin error global.
* Puede utilizarse un evento consolidado: `EVT_ACTIVATION_CONFIRMED`

## 6. Diagramas

* Ver sección correspondiente en `protocolo_nfc.drawio`: "Respuesta multimodal a activación"
