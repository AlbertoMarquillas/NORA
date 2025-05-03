### Módulo: Interfaz GPIO – Raspberry Pi 4 (conector J1)

Este módulo representa la interfaz de conexión entre la Raspberry Pi 4 (RBP4) y el resto del sistema NORA mediante su cabecera de 40 pines (J1). Permite el acceso a buses I2C, SPI, UART, entradas digitales, salidas PWM y líneas de control. Además, proporciona la posibilidad de alimentar la RPi desde fuente externa mediante `5V_RPI4` y `GND_RPI4`.

---

#### 1. Descripción funcional del conjunto

La cabecera de 40 pines expone múltiples interfaces:

* **Alimentación externa**: 5 V y GND directamente desde el bloque de potencia.
* **Bus I2C**: SDA (GPIO2), SCL (GPIO3).
* **Bus SPI**: SPI\_CLK (GPIO11), SPI\_MISO (GPIO9), SPI\_MOSI (GPIO10), múltiples CS.
* **UART**: BT\_RX (GPIO15), BT\_TX (GPIO14).
* **PWM**: PWM\_AUDIO, PWM\_Servo1, PWM\_Servo2.
* **GPIO**: entradas y salidas digitales para control, activación y eventos.

---

#### 2. Conexiones relevantes destacadas

* **Alimentación:**

  * Pin 2 o 4 → `5V_RPI4`
  * Pin 6, 9, 14, 20, 30, 34, 39 → cualquier `GND_RPI4` (uno basta, más mejora integridad)

* **I2C:**

  * Pin 3 (GPIO2) → SDA
  * Pin 5 (GPIO3) → SCL

* **SPI:**

  * Pin 19 (MOSI), 21 (MISO), 23 (SCLK)
  * Pin 24 (CS Mic), 18 (CS OLED)

* **UART (Bluetooth):**

  * Pin 8 (TX), 10 (RX)

* **PWM:**

  * PWM\_AUDIO → GPIO12 (Pin 32)
  * PWM\_Servo1 → GPIO18 (Pin 12)
  * PWM\_Servo2 → GPIO13 (Pin 33)

* **GPIO para control y sensores:**

  * `Btn`, `Trigger(Ultra)`, `Echo(Ultra)`, `DC_OLED`, `RST_OLED`, `RSTPD_N`, `P32_INT0`, `RTC_SOUT`, `LEDS-IN`

---

#### 3. Observaciones técnicas

* La alimentación de la RPi desde pines 2/4 es válida con una fuente de 5 V estabilizada, como la LRS-35-5 del sistema.
* Conectar una sola línea GND es suficiente, pero conectar al menos dos mejora estabilidad.
* El pin 1 (3.3 V) no debe conectarse a la fuente externa, ya que es una salida regulada interna de la RPi.
* Todos los buses están distribuidos adecuadamente y con separación de funciones.

---

#### 4. Recomendaciones

* Usar cables de sección ≥20 AWG para las líneas de alimentación `5V_RPI4` y `GND_RPI4`.
* Documentar el uso exacto de cada GPIO (in/out, pull-up/down, función secundaria).
* Si se usan múltiples periféricos SPI, considerar multiplexado de CS o control por software.
* Mantener baja impedancia de GND en todo el sistema para evitar falsos disparos o ruido.

---

#### 5. Conclusión

Este módulo centraliza la conexión entre la Raspberry Pi 4 y todos los subsistemas de NORA. Su diseño es correcto, con adecuada asignación de buses y líneas de alimentación. Alimentar la RPi directamente desde la fuente de 5 V del sistema es totalmente válido y ha sido bien implementado. Se sugiere verificar la correcta configuración de los GPIOs desde el software de arranque para evitar conflictos.
