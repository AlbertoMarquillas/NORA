# Hardware de Tacto – Interacción Táctil Directa

Este documento describe los componentes físicos necesarios para implementar la detección de contacto táctil en NORA, sus principios de funcionamiento y su conexión al sistema de control.

---

## 1. Objetivo

Seleccionar e integrar sensores táctiles apropiados para permitir la interacción física directa con el asistente, manteniendo bajo consumo y alta fiabilidad en entornos domésticos.

---

## 2. Tipos de sensores compatibles

| Tipo de sensor             | Tecnología       | Ventajas                             | Limitaciones                          |
| -------------------------- | ---------------- | ------------------------------------ | ------------------------------------- |
| Sensor capacitivo de botón | TTP223 o similar | Fácil integración, económico         | Zona puntual, no multipunto           |
| Pantalla táctil capacitiva | ILI9341 + TP     | Multipunto, visualización incluida   | Mayor coste y complejidad             |
| Sensor capacitivo flexible | MPR121 u otros   | Multizona, sensibilidad configurable | Requiere calibración y software extra |
| Tira conductiva DIY        | Touchpad casero  | Personalizable y de bajo coste       | Menor robustez y precisión            |

---

## 3. Conexión al sistema

* **Interfaces disponibles:**

  * GPIO digital (para sensores simples tipo TTP223)
  * I²C (para sensores multizona tipo MPR121)
  * SPI (si se emplea pantalla táctil con visualización)

* **Microcontrolador:** la Raspberry Pi inicial puede gestionar directamente sensores simples, o delegar en un microcontrolador (STM32, ATmega) si se requieren múltiples zonas o control en tiempo real

---

## 4. Ubicación sugerida

| Zona              | Sensor propuesto  | Función principal                  |
| ----------------- | ----------------- | ---------------------------------- |
| Parte frontal     | Capacitivo simple | Confirmar o despertar              |
| Lateral izquierdo | Capacitivo largo  | Control de navegación o contexto   |
| Parte superior    | Táctil multipunto | Acceso rápido a funciones o gestos |

---

## 5. Consideraciones de diseño

* Aislamiento mecánico para evitar toques falsos por vibración
* Integración visual y ergonómica con la carcasa
* Retroalimentación mediante LEDs o voz tras contacto confirmado

---

El hardware táctil es esencial para cerrar el bucle de interacción física con NORA, aportando inmediatez, accesibilidad y un medio alternativo al canal vocal o visual.
