# Descripción – Interacción Física Avanzada

Este documento introduce la interacción basada en eventos físicos estructurales captados por sensores internos de NORA, como movimientos, inclinaciones, impactos o manipulación directa del cuerpo del dispositivo. Este tipo de entrada, aún experimental, permite ampliar las capacidades perceptivas del sistema más allá de canales tradicionales.

---

## 1. Objetivo

Detectar y reaccionar ante estímulos físicos como desplazamientos, golpes, inclinación o manipulación manual del dispositivo, permitiendo que NORA responda con expresiones adecuadas o cambios de estado autónomos.

---

## 2. Ejemplos de interacción física

| Evento físico detectado               | Posible acción desencadenada                   |
| ------------------------------------- | ---------------------------------------------- |
| El usuario inclina ligeramente a NORA | Giro ocular o expresión de desequilibrio       |
| El sistema es desplazado              | Activación de expresión de sorpresa + registro |
| Golpe en la carcasa                   | Entrada en estado de diagnóstico o alarma leve |
| Agitación o vibración brusca          | Reinicio de módulos no críticos                |

---

## 3. Componentes necesarios

* **IMU (Inertial Measurement Unit):** acelerómetro y giroscopio (e.g., MPU-6050, BNO055)
* **Sensores de presión o contacto estructural**
* **Fijación mecánica sensible** para interpretación contextual

---

## 4. Integración con el sistema

* `sensores/imu.py`: adquisición y filtrado de datos físicos
* `agentes/fisico.py`: interpretación de eventos y lógica contextual
* `estado/fsm.py`: generación de eventos como `EVT_PHYSICAL_*`
* `expresion/`, `voz/`, `pantalla/`: respuesta coordinada

---

## 5. Estados y condiciones de activación

* La detección se evalúa constantemente en segundo plano
* En `STATE_IDLE` o `STATE_SLEEP`, algunos eventos pueden reactivar al sistema
* Se puede ajustar la sensibilidad o activar solo en modo diagnóstico

---

Esta capacidad fortalece la dimensión corporal y simbólica de NORA, permitiendo respuestas perceptivas a estímulos físicos y reforzando su carácter tangible e interactivo.
