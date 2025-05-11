"""
config_gpios.py – Configuración centralizada de GPIOs y buses hardware para el sistema NORA.
Incluye asignaciones físicas, direcciones I²C y referencias documentales para sensores y actuadores.
"""

# === Bus I²C principal ===
I2C_BUS = 1  # En Raspberry Pi 4, el bus I²C estándar usa GPIO2 (SDA) y GPIO3 (SCL)

# === Sensor de Temperatura (MCP9902) ===
TEMP_SENSOR_I2C_ADDR = 0x18     # Dirección I2C con THERM/ADDR a GND
TEMP_SDA_GPIO = 2               # GPIO2 → SDA → pin físico 3
TEMP_SCL_GPIO = 3               # GPIO3 → SCL → pin físico 5
TEMP_VCC_PIN = 1                # 3V3 → pin físico 1
TEMP_GND_PIN = 6                # GND → pin físico 6

# === Botón físico (activación manual) ===
BTN_GPIO = 4                    # GPIO4 → pin físico 7

# === Sensor de presencia ultrasónico (modo avanzado) ===
ULTRASONIC_TRIGGER_GPIO = 17    # GPIO17 → Trigger → pin físico 11
ULTRASONIC_ECHO_GPIO = 27       # GPIO27 → Echo → pin físico 13

# === SPI general (Audio, OLED, NFC compartido) ===
SPI_MOSI = 10                   # GPIO10 → pin físico 19
SPI_MISO = 9                    # GPIO9  → pin físico 21
SPI_CLK = 11                    # GPIO11 → pin físico 23

# === Micrófono digital por SPI (chip select) ===
SPI_CS_MICROPHONE = 25          # GPIO25 → pin físico 22

# === RTC (DS3231) – Señal de salida de alarma ===
RTC_SOUT_GPIO = 6               # GPIO6 → pin físico 31

# === Servos físicos ===
PWM_SERVO_1_GPIO = 18           # GPIO18 (no documentado en tabla, común para servo principal)
PWM_SERVO_2_GPIO = 13           # GPIO13 → pin físico 33

# === Salida de audio por PWM ===
PWM_AUDIO_GPIO = 19            # GPIO19 → pin físico 35

# === Pantalla OLED (digital control) ===
DC_OLED_GPIO = 26              # GPIO26 → pin físico 37
SPI_CS_OLED = 24               # GPIO24 → chip select OLED (no explicitado pero reservado)

# === LEDs RGB de expresión facial ===
LEDS_IN_GPIO = 21              # GPIO21 → pin físico 40

# === Pines no usados (reservados para expansión futura) ===
RESERVED_GPIO_12 = 12          # GPIO12 → pin físico 32
RESERVED_GPIO_16 = 16          # GPIO16 → pin físico 36
RESERVED_GPIO_20 = 20          # GPIO20 → pin físico 38
