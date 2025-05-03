# Condiciones de entrada – Estado: Atencion

El sistema NORA entra en el estado **Atencion** cuando se cumplen condiciones perceptivas que indican una intención de interacción visual por parte del usuario. La transición es gestionada por la FSM (`sistema/`) y puede ser modulada o confirmada por los agentes del módulo `/agentes/`.

---

## 1. Detección visual sostenida

- **Evento:** `EVT_ATTENTION_GAINED`  
  Emitido por el módulo `vision/` tras detección de rostro humano orientado hacia la cámara frontal durante un tiempo superior a un umbral (`T_ATTENTION_SUSTAIN`).  
  Este evento debe mantenerse estable durante una ventana temporal configurable (ej. >1.5 s).

---

## 2. Presencia contextual confirmada

- **Evento combinado:** `EVT_PRESENCE_CONFIRMED` + `EVT_ATTENTION_GAINED`  
  Ambos eventos deben estar activos para evitar falsas activaciones por ruido visual (ej. objetos o movimiento irrelevante).

---

## 3. Validación por agentes

- Los agentes del sistema (`/agentes/`) validan la intención si se cumple alguna de las siguientes condiciones:

  - La atención visual proviene de un usuario identificado (reconocimiento facial).
  - No hay condiciones inhibidoras activas (fatiga del sistema, privacidad, etc.).
  - El sistema no está ocupado (`STATE_BUSY = False`).

---

## 4. Transición desde estado previo

- **Origen válido:** `Activado`  
  El estado **Atencion** solo se puede alcanzar desde `Activado`, nunca directamente desde `Reposo` o estados terminales.

---

## Consideraciones adicionales

- La entrada a este estado puede ser cancelada si se pierde el contacto visual antes de confirmar la intención sostenida.
- Umbrales de validación como tiempo, distancia, ángulo de la mirada y entorno visual son configurables y adaptables según perfil.
