# Descripción – Interacción Táctil Directa

Este documento describe la interacción basada en contacto físico directo entre el usuario y el cuerpo del sistema NORA, mediante superficies capacitivas, sensores táctiles o pantallas sensibles al tacto. Esta forma de entrada permite una comunicación física y simbólica sin necesidad de voz ni texto.

---

## 1. Objetivo

Facilitar acciones de control o interacción simbólica mediante el tacto, como confirmaciones, navegación por interfaz física o señales de atención.

---

## 2. Tipos de interacción previstas

* **Toque simple:** para activar o confirmar una acción
* **Toque prolongado:** para pausar, cancelar o entrar en modo especial
* **Deslizamiento:** navegación o cambio de estado (si hay pantalla táctil)
* **Patrones gestuales:** combinación de toques o zonas tocadas

---

## 3. Superficies previstas

| Tipo de sensor           | Posible ubicación  | Función prevista                         |
| ------------------------ | ------------------ | ---------------------------------------- |
| Pantalla capacitiva      | Frente o cabeza    | Navegación por menú o entrada rápida     |
| Sensores capacitivos     | Laterales o base   | Confirmación, activación, control físico |
| Zonas metálicas aisladas | Estructura externa | Señales táctiles simbólicas              |

---

## 4. Condiciones de activación

* El sistema debe estar en `STATE_ACTIVE_WAIT` o `STATE_ATTENTION`
* Se requiere validación de que el contacto es humano (ruido térmico o capacitancia)
* Puede combinarse con detección de presencia visual

---

## 5. Integración con otros módulos

* `sensores/tacto.py` – detección física básica
* `agentes/tacto.py` – interpretación de patrones
* `estado/fsm.py` – transición según acción física
* `expresion/`, `voz/`, `motor/` – retroalimentación asociada

---

La interacción táctil directa refuerza el carácter físico del asistente NORA, facilitando un vínculo natural y accesible para usuarios que prefieran el contacto frente a la entrada verbal o textual.
