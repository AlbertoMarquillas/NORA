# Elección de Plataforma para Programación en Python – Proyecto NORA

## ✅ Estrategia Recomendada

Desarrollar inicialmente sobre **Raspberry Pi** usando **Python estándar**, y en una fase futura migrar a una CPU embebida que soporte **MicroPython**, para mantener el mismo lenguaje en la PCB final.

---

## 🧱 Etapas

### Fase actual – Raspberry Pi (Python)

* Soporte completo de Python 3.x
* Bibliotecas ampliamente compatibles:

  * `RPi.GPIO`, `gpiozero`, `serial`, `smbus`, `spidev`, `Adafruit_DHT`, etc.
* Sistema operativo completo (Raspbian / Raspberry Pi OS)
* Perfecto para prototipado rápido, visualización, pruebas en tiempo real

### Fase futura – Microcontrolador con Python embebido

Para mantener Python, se recomienda el uso de plataformas con soporte **MicroPython**.

---

## 📊 Comparativa de plataformas embebidas con soporte Python

| Plataforma        | Lenguaje              | Comunicación | GPIO/I²C/SPI/UART | WiFi/Bluetooth         | Soporte MicroPython       | Ideal para                          |
| ----------------- | --------------------- | ------------ | ----------------- | ---------------------- | ------------------------- | ----------------------------------- |
| **RP2040 (Pico)** | MicroPython/C         | USB/Serial   | ✅                 | ❌                      | ✅ Oficial                 | PCB dedicada minimalista con Python |
| **ESP32**         | MicroPython/C         | UART/WiFi    | ✅                 | ✅ Integrado            | ✅ Oficial + forks         | Proyectos conectados, inalámbricos  |
| **STM32**         | C/C++/CircuitPython\* | UART/SWD     | ✅                 | ❌ (en modelos básicos) | ⚠ Parcial / Adafruit fork | Proyectos industriales complejos    |

> `*` CircuitPython es una variante de MicroPython desarrollada por Adafruit, con menos control pero más facilidades para principiantes.

---

## 📦 Detalle de opción recomendada: Raspberry Pi Pico (RP2040)

| Característica        | Valor                                  |
| --------------------- | -------------------------------------- |
| CPU                   | Dual-core Cortex-M0+ @ 133 MHz         |
| RAM                   | 264 KB                                 |
| Flash externa         | Hasta 16 MB                            |
| GPIO disponibles      | 26 (incluye PWM, ADC, UART, SPI, I²C)  |
| Alimentación          | 3.3 V lógica                           |
| Precio                | ≈ 5 €                                  |
| Lenguaje              | MicroPython / C                        |
| Soporte               | Oficial por la Raspberry Pi Foundation |
| Librerías disponibles | `machine`, `uasyncio`, `time`, etc.    |

---

## 🔌 Compatibilidad con NORA

| Requisito del sistema NORA | ¿Compatible con RP2040 / ESP32? |
| -------------------------- | ------------------------------- |
| Bus I²C compartido         | ✅                               |
| UART para Bluetooth        | ✅                               |
| PWM para servos/audio      | ✅                               |
| Entradas digitales         | ✅                               |
| Alimentación 3.3 V lógica  | ✅                               |
| Código Python              | ✅ (con MicroPython adaptado)    |

---

## ⚠ Consideraciones al migrar

* Deberás adaptar las librerías de Python de la Raspberry Pi a **MicroPython** (simplificadas)
* Evitar dependencias con librerías que usen el sistema operativo (como `os`, `socket` a bajo nivel)
* Posible limitación de memoria RAM para procesos grandes

---

## ✅ Conclusión

* Continúa el desarrollo en **Raspberry Pi con Python 3.x**
* Planea migrar en el futuro a una **RP2040** o **ESP32** si deseas mantener **Python en hardware embebido**
* MicroPython es estable, bien documentado y suficiente para todas las funciones actuales de NORA

---
