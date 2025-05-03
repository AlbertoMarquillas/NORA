# Integración de Voz – Interacción Verbal

Este documento describe cómo se integran los motores de reconocimiento y síntesis de voz en el sistema NORA. Se detallan las dependencias técnicas, las decisiones arquitectónicas y las funciones clave expuestas por cada módulo.

---

## 1. Reconocimiento de voz (ASR)

### Motor utilizado

* **Motor base:** Vosk (offline)
* **Idioma configurado:** español
* **Modelo:** `vosk-model-small-es-0.42`

### Flujo de procesamiento

```plaintext
[Audio del micrófono] → VAD → Vosk STT → texto limpio → envío a dialogo/
```

### Detalles técnicos

* Umbral de activación por energía + VAD
* Segmentación por silencios
* Transcripción sin puntuación ni tildes
* Desambiguación básica mediante `limpieza_texto()`

---

## 2. Síntesis de voz (TTS)

### Motor utilizado

* **Motor base:** RHVoice o eSpeak NG
* **Interfaz:** subprocess o wrapper Python

### Requisitos

* Respuesta rápida (< 500 ms)
* Voz natural y configurable
* Permitir variantes según emoción (futuro)

### Flujo de salida

```plaintext
[texto respuesta] → plantilla → motor TTS → archivo .wav → salida por altavoz
```

---

## 3. Módulos y funciones expuestas

### `voz/asr.py`

* `iniciar_reconocimiento()`
* `detener_reconocimiento()`
* `obtener_texto()`

### `voz/tts.py`

* `decir(texto: str)`
* `decir_emocion(texto: str, tipo: str)` *(previsto)*

---

## 4. Configuración y pruebas

* Micro conectado vía USB o interfaz interna (dependiendo del hardware)
* Volumen controlado por software
* Pruebas automatizadas con frases de ejemplo
* Modo de prueba sin sintetizar (para scripts headless)

---

## 5. Observaciones

* Ambos motores son locales: no se envía audio ni texto a servicios externos.
* Se puede alternar entre motores según recursos y calidad deseada.
* El módulo `voz/` está desacoplado del flujo principal: recibe y entrega eventos.

Esta integración permite una interacción verbal fluida, privada y compatible con los principios de independencia tecnológica de NORA.
