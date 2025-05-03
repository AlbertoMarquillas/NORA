# Patrones de Interacción – Interacción Táctil Directa

Este documento define los patrones de contacto físico que NORA puede interpretar como señales significativas dentro del subsistema táctil. Cada patrón corresponde a un gesto, combinación de zonas o tipo de contacto, asociado a una acción o transición de estado específica.

---

## 1. Objetivo

Permitir al usuario emitir comandos o respuestas mediante gestos táctiles simples y reproducibles, facilitando una comunicación física intuitiva sin depender de la voz ni del texto.

---

## 2. Tipos de patrones reconocidos

| Patrón táctil                | Descripción                          | Acción asociada                            |
| ---------------------------- | ------------------------------------ | ------------------------------------------ |
| Toque simple (tap)           | Contacto breve en zona específica    | Confirmación, activación local             |
| Toque prolongado (hold > 2s) | Mantener contacto sin movimiento     | Cancelar, pausar o entrar en modo especial |
| Doble toque                  | Dos taps rápidos consecutivos        | Cambiar modo o confirmar en contexto       |
| Deslizamiento                | Movimiento táctil de una zona a otra | Navegar entre menús o cambiar expresión    |
| Secuencia de zonas           | Tocar varias zonas en orden          | Comando compuesto (futuro)                 |

---

## 3. Lógica de interpretación

* Los eventos táctiles se recogen mediante `sensores/tacto.py`
* El análisis se realiza en `agentes/tacto.py` según el historial y duración
* Se evalúan:

  * Duración del contacto
  * Cantidad de zonas implicadas
  * Tiempo entre eventos sucesivos
  * Contexto actual del sistema (`estado/fsm.py`)

---

## 4. Contexto de ejecución

* En `STATE_IDLE` o `STATE_ACTIVE_WAIT`, un toque puede activar al sistema
* En `STATE_DIALOGUE`, un toque puede confirmar o cancelar un paso
* En `STATE_SLEEP`, solo el toque prolongado puede reactivar NORA (si permitido)

---

## 5. Recomendaciones de diseño de interacción

* Usar patrones simples y evitar secuencias largas
* Asociar respuesta inmediata visual o sonora a cada gesto reconocido
* Permitir configuración por usuario avanzado en `config/tacto_gestos.json`

---

Estos patrones fortalecen la comunicación natural con el sistema, y permiten ampliar su expresividad física sin necesidad de medios auditivos o visuales complejos.
