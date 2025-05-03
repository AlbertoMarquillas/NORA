# Respuestas Físicas – Interacción ante Eventos Corporales

Este documento define las posibles respuestas del sistema NORA ante la detección de eventos físicos como movimientos, inclinaciones o golpes, permitiendo una reacción multisensorial coordinada que refuerce el vínculo entre estímulo y respuesta.

---

## 1. Objetivo

Proporcionar retroalimentación física, visual o sonora ante la detección de una manipulación directa del sistema, generando expresividad, diagnóstico o acciones defensivas internas.

---

## 2. Tipos de respuesta disponibles

| Canal de salida | Medio asociado            | Tipo de respuesta                            |
| --------------- | ------------------------- | -------------------------------------------- |
| Visual          | LEDs o pantalla           | Cambio de color, expresión de sorpresa       |
| Sonoro          | Altavoz                   | Mensaje verbal o sonido breve de advertencia |
| Motor/físico    | Base giratoria o vibrador | Movimiento compensatorio o reorientación     |
| Datos/log       | Registro interno          | Anotación del evento físico detectado        |

---

## 3. Asociación evento ↔ respuesta

| Evento físico              | Respuesta recomendada                                           |
| -------------------------- | --------------------------------------------------------------- |
| `EVT_PHYSICAL_IMPACT`      | Flash visual + sonido + anotación en `logs/eventos_fisicos.log` |
| `EVT_PHYSICAL_ROTATION`    | Recentrado o expresión ocular de confusión                      |
| `EVT_PHYSICAL_TILT_STABLE` | Mensaje: “¿Me has movido?” o entrada en modo alerta             |

---

## 4. Módulos implicados

* `expresion/`: manejo de reacciones visuales o faciales
* `voz/`: selección de frases predefinidas para eventos físicos
* `motor/`: ejecución de movimientos compensatorios (si hay actuadores)
* `monitor/fisico.py`: gestor de eventos persistentes o repetitivos

---

## 5. Consideraciones contextuales

* Las respuestas físicas no deben ejecutarse si el sistema está en `STATE_SLEEP` salvo si se permite por configuración
* Puede activarse un `modo silencioso` donde solo se registran los eventos sin respuesta externa
* Las respuestas pueden variar según perfil de usuario o tipo de interacción reciente

---

Estas respuestas permiten a NORA reaccionar de forma natural, expresiva y contextualizada ante estímulos físicos externos, reforzando su percepción como asistente corporal sensible e interactivo.
