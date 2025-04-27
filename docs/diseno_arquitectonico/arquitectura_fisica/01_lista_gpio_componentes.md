# Lista de Componentes Conectados por GPIO – Sistema NORA

**Objetivo:**  
Identificar todos los componentes físicos que utilizan pines GPIO de la Raspberry Pi para su señalización, control o alimentación controlada, diferenciando entradas y salidas.

## 1. Servomotores SG90/MG90 (x2 o x3)

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Servomotor 1**     | Movimiento de cabeza               | PWM                       | GPIO18 (Pin 12)     | Salida PWM para controlar la posición del servo. |
| **Servomotor 2**     | Movimiento del cuerpo              | PWM                       | GPIO13 (Pin 33)     | Salida PWM para controlar el movimiento.         |

## 2. Pantalla OLED/TFT SPI (SSD1306/ST7735)

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Pantalla OLED/TFT** | Expresión visual del rostro        | SPI o I²C (según modelo)  | GPIO10 (MOSI), GPIO11 (SCK), GPIO8 (CS), GPIO9 (DC), GPIO25 (RST) | Conexión SPI: MOSI (Data), SCK (Reloj), CS (Chip Select), DC (Data Command), RST (Reset). |

## 3. LEDs RGB WS2812 (Neopixels)

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **LED RGB WS2812**   | Iluminación emocional (cambio de colores) | Señal digital temporizada | GPIO21 (Pin 40)     | Control de los LEDs con señal de datos serial. |

## 4. Módulo NFC PN532

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Módulo NFC**       | Activación por proximidad           | UART, SPI o I²C           | GPIO2 (SDA), GPIO3 (SCL) o GPIO14 (TX), GPIO15 (RX) | Conexión mediante I²C o UART, según la configuración. |

## 5. Micrófono USB (Alternativa: GPIO/I2S)

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Micrófono USB**    | Entrada de audio                   | USB                       | No aplica (conexión USB) | Si se usa micrófono GPIO/I2S, se pueden usar los pines GPIO para I2S. |

## 6. Altavoz (vía PWM directo)

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Altavoz**          | Salida de audio                    | PWM o DAC (si aplica)     | GPIO19 (Pin 35)     | Salida PWM controlada por software para el altavoz. |

## 7. Sensor ultrasónico HC-SR04

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Sensor HC-SR04**   | Detección de presencia             | Digital (ON/OFF)          | GPIO17 (Pin 11) (Trigger), GPIO27 (Pin 13) (Echo) | Usando 2 pines GPIO: Trigger para iniciar la medición, Echo para recibir la señal de retorno. |

## 8. Sensor de temperatura/humedad DHT22/BME280

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **DHT22/BME280**     | Lectura de temperatura y humedad  | Digital                   | GPIO4 (Pin 7)       | Señal digital de lectura de datos.               |

## 9. Sensor de luminosidad TSL2561

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Sensor TSL2561**   | Medición de luz ambiental          | I²C                       | GPIO2 (SDA), GPIO3 (SCL) | Comunicación I2C, requiere GPIO para SDA y SCL.  |

## 10. RTC DS3231

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **RTC DS3231**       | Reloj en tiempo real               | I²C                       | GPIO2 (SDA), GPIO3 (SCL) | Comunicación I2C para acceso al reloj.           |

## 11. Botón físico (GPIO)

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Botón físico**     | Activación manual                  | Digital (ON/OFF)          | GPIO17 (Pin 11)     | Entrada con pull-up o pull-down configurable.    |

## 12. Módulo Bluetooth (HC-05)

| Componente          | Función                            | Tipo de Señal / Protocolo | Pin GPIO Asignado   | Descripción del Pin                                |
|---------------------|------------------------------------|---------------------------|---------------------|--------------------------------------------------|
| **Bluetooth**        | Comunicación con dispositivos cercanos | UART                     | GPIO14 (TX), GPIO15 (RX) | Comunicación serie entre Raspberry Pi y dispositivo. |

---

## **Conclusión**:

Cada componente debe ser asignado a un pin específico de la Raspberry Pi de acuerdo a sus características de señal. Las conexiones digitales (GPIO), PWM, I2C, y UART tienen que estar bien gestionadas para evitar conflictos y asegurar la correcta interacción entre los módulos. Además, se debe considerar la alimentación de los componentes y sus pines de tierra (GND).
