# Salida Multimodal de Desactivación en NORA (Respuesta a UID NFC toggle)

## 1. Objetivo

Describir la respuesta multimodal del sistema NORA cuando un UID previamente validado activa el protocolo de desactivación consciente.

## 2. Contexto del Evento

* **Evento desencadenante:** `EVT_NFC_UID_TOGGLE`
* **Estado anterior:** `STATE_ACTIVE` o `STATE_LISTENING`
* **Estado resultante:** `STATE_IDLE`

## 3. Canales de Salida Involucrados

### 3.1. Visual (LEDs RGB WS2812 o indicadores)

* **Color emitido:** Rojo sólido
* **Duración:** 1 segundo mínimo
* **Módulo responsable:** `interfaz/`

### 3.2. Auditivo (altavoz + amplificador)

* **Mensaje:** "Sistema desactivado"
* **Motor TTS:** gestionado por `voz/`
* **Duración estimada:** 1.5–2 segundos

### 3.3. Registro Interno

* **Módulo:** `datos/`
* **Contenido:** Timestamp + UID + evento: `DESACTIVACION_EXITOSA`

## 4. Secuencia de Ejecución

1. UID coincide con el registrado previamente como activo.
2. Se emite el evento `EVT_NFC_UID_TOGGLE`
3. `sistema/` transita a `STATE_IDLE`
4. `interfaz/` activa LED rojo
5. `voz/` sintetiza y emite mensaje de apagado
6. `datos/` registra evento de desactivación

## 5. Consideraciones Técnicas

* Se recomienda un pequeño retardo final (p. ej., 500 ms) antes de desconectar módulos críticos.
* El evento `EVT_DEACTIVATION_CONFIRMED` puede usarse para señalizar el cierre completo.
* Los canales de salida deben ser resistentes a fallos individuales (fallback visual o log en caso de fallo auditivo).

## 6. Diagramas

* Ver sección correspondiente en `protocolo_nfc.drawio`: "Respuesta multimodal a desactivación"
