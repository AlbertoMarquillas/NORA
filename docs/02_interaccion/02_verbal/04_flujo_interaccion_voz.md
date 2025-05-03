# Flujo de Interacción por Voz – Comando, Recibo y Respuesta

Este documento describe el flujo completo de interacción verbal entre el usuario y NORA, desde la recepción del comando de voz hasta la entrega de una respuesta expresiva multimodal. Este mecanismo es uno de los canales principales de uso cotidiano.

---

## Nombre del flujo

Interacción por voz (comando-recibo-respuesta)

---

## Estado inicial

**STATE\_ACTIVE\_WAIT** o **STATE\_DIALOGUE**

Sistema activo, con el módulo de reconocimiento de voz en espera de entrada.

---

## Evento disparador

Captación de señal vocal por el micrófono activo.

---

## Condición de validación

* Comando reconocido y transcrito por `voz/asr.py`
* Validación de intención mediante `dialogo/interpretador.py`

---

## Acción del sistema

1. Transcripción del audio a texto (ASR)
2. Análisis de intención y entidades
3. Consulta al módulo correspondiente (e.g., `datos/notas.py`, `agenda/consultor.py`)
4. Generación de respuesta verbal con `voz/tts.py`
5. Emisión de la respuesta junto a elementos expresivos coordinados

---

## Estado final

Retorno a **STATE\_ACTIVE\_WAIT** o continuación en **STATE\_DIALOGUE** según contexto

---

## Respuesta multimodal

| Canal      | Respuesta prevista                                            |
| ---------- | ------------------------------------------------------------- |
| Voz        | Ej. “He anotado tu recordatorio.”                             |
| LEDs       | Animación suave de colores cálidos durante respuesta          |
| Pantalla   | Gesto facial positivo (ojos contentos, parpadeo)              |
| Movimiento | Giro leve de cabeza hacia el usuario (si hardware lo permite) |

---

## Acciones complementarias

* Registrar comando y respuesta en `logs/dialogo.log`
* Emitir `EVT_RESPUESTA_GENERADA` al núcleo para sincronización de subsistemas

---

## Diagrama

El archivo `flujo_interaccion_voz.drawio` complementará este documento como representación visual paso a paso.

---

Este flujo constituye la base de la interacción natural y cotidiana con NORA, combinando procesamiento del lenguaje, expresividad física y contexto conversacional.
