# Flujo de Activación por NFC

Este documento describe el flujo específico que permite a NORA transitar desde el estado de reposo a un estado operativo tras la detección de una tarjeta NFC válida. Esta secuencia constituye uno de los principales métodos de activación del sistema.

---

## Nombre del flujo

Activación por NFC

---

## Estado inicial

**STATE\_SLEEP** o **STATE\_IDLE**
Todos los módulos principales (voz, visión, diálogo) se encuentran desactivados o en modo de espera pasiva.

---

## Evento disparador

Lectura exitosa de una tarjeta NFC.

---

## Condición de validación

* El UID de la tarjeta debe estar presente en la lista local de usuarios autorizados.
* Validación realizada por el módulo `lectura_nfc.py` mediante comparación con `datos/usuarios/autorizados.json`.

---

## Acción del sistema

* Activación de los módulos `voz/tts.py`, `vision/camara.py` y `dialogo/core.py`
* Transición del estado interno a `STATE_ACTIVE_WAIT`
* Inicialización del registro de sesión (si está habilitado en configuración)

---

## Estado final

Sistema en estado **activo**, preparado para recibir comandos por voz o texto.

---

## Respuesta multimodal

| Canal      | Respuesta                                                                     |
| ---------- | ----------------------------------------------------------------------------- |
| Voz        | “Hola, ¿cómo puedo ayudarte?” (síntesis por `voz/tts.py`)                     |
| LEDs       | Animación verde suave durante 2 segundos (`hardware/led_rgb.py`)              |
| Pantalla   | Activación de ojos abiertos y expresión facial atenta (`expresion/facial.py`) |
| Movimiento | Giro de cabeza hacia adelante (opcional, si hay servo disponible)             |

---

## Acciones complementarias

* Registrar la hora de activación y UID en `logs/registro_sesiones.log`
* Emitir evento `EVT_ACTIVACION_NFC` para su interpretación por `estado/fsm.py`

---

## Diagrama

Un archivo `flujo_activacion_nfc.drawio` acompañará este documento para representar gráficamente el flujo.

---

Este flujo garantiza una activación segura, multimodal y coherente con el diseño general del sistema, constituyendo un punto de entrada clave para la interacción con NORA.
