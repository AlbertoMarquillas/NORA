# Sensores IMU – Interacción Física Avanzada

Este documento describe los sensores inerciales necesarios para la detección de movimientos, inclinaciones y golpes en NORA, así como su integración en el sistema de análisis de eventos físicos.

---

## 1. Objetivo

Captar datos tridimensionales de aceleración y orientación para interpretar interacciones físicas estructurales realizadas sobre el cuerpo del sistema NORA.

---

## 2. Tipos de sensores contemplados

| Sensor   | Componentes integrados             | Ventajas                        | Limitaciones                   |
| -------- | ---------------------------------- | ------------------------------- | ------------------------------ |
| MPU-6050 | Acelerómetro + giroscopio          | Amplia documentación, económico | Requiere filtrado por software |
| BNO055   | IMU con fusión integrada           | Salida directa de orientación   | Mayor coste                    |
| MPU-9250 | Acelerómetro + gyro + magnetómetro | Datos completos con heading     | Más complejo de integrar       |

---

## 3. Datos relevantes

* **Aceleración lineal:** para detectar golpes o vibraciones
* **Velocidad angular:** para medir rotaciones e inclinación
* **Orientación absoluta (si disponible):** permite saber si el sistema ha sido girado o volteado

---

## 4. Conexión e integración

* **Interfaz:** I²C preferido, también disponible SPI
* **Frecuencia de muestreo sugerida:** 50–100 Hz
* **Archivo de adquisición:** `sensores/imu.py`
* **Módulo de interpretación:** `agentes/fisico.py`

---

## 5. Procesamiento de datos

* Filtro de paso bajo para eliminar ruido
* Umbrales configurables para detección de eventos físicos (`config/imu_eventos.json`)
* Posibilidad de fusión de sensores para mayor robustez (kalman/madgwick)

---

## 6. Ejemplos de eventos extraíbles

| Patrón detectado            | Evento generado            |
| --------------------------- | -------------------------- |
| Pico súbito de aceleración  | `EVT_PHYSICAL_IMPACT`      |
| Giro superior a X° en eje Y | `EVT_PHYSICAL_ROTATION`    |
| Inclinación mantenida > 5s  | `EVT_PHYSICAL_TILT_STABLE` |

---

La correcta integración de sensores IMU dota a NORA de percepción física contextualizada, permitiéndole responder al entorno con realismo y robustez ante manipulación directa.
