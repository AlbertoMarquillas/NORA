# Componentes físicos observables por los agentes del sistema NORA


> Versión: 1.0 (24 Abril 2025)

Este documento recoge todos los componentes físicos que conforman la plataforma NORA. Sirve como base para el diseño del diagrama conceptual del sistema.

## 1. Unidad de procesamiento

Este bloque contiene el núcleo computacional del sistema. Es responsable de ejecutar la lógica principal y coordinar los módulos periféricos.

Componente propuesto: **Raspberry Pi 4 Model B**

Justificación:

- Potencia de cómputo suficiente para ejecutar procesamiento de visión y voz en local.
- Gran compatibilidad con periféricos y sensores.
- Comunidad de soporte y abundante documentación.
- Posibilidad de usar Python, que es el lenguaje principal del proyecto.

Datasheet

[Datasheet Raspberry Pi](datasheets/raspberry-pi-4-datasheet.pdf)

## 2. Captación sensorial

Este bloque abarca los componentes que permiten percibir el entorno y al usuario, recopilando datos visuales, sonoros y de proximidad.

Componente propuesto: **Cámara (CSI o USB)**

Justificación:

- Permite visión artificial en tiempo real (detección facial, postural).
- Las cámaras CSI se conectan directamente a la Pi, liberando puertos USB.
- Las USB tienen mayor compatibilidad plug & play si se prefiere flexibilidad.
- Alternativas: Raspberry Pi Camera v2 (CSI), o Logitech C270 (USB).

Agente: 
- Percepción visual

Datasheets

[Datasheet Raspberry Pi Camera Module](datasheets/RPiCamMod2.pdf)  
[Datasheet Raspberry Pi Camera v2](datasheets/2056179.pdf)

Componente propuesto: **Micrófono (digital o analógico)**

Justificación:

- Captura de audio necesario para comandos por voz.
- Los micrófonos USB simplifican la conexión.
- Los analógicos requieren ADC o módulo intermedio.
- Alternativa recomendada: Micrófono USB tipo mini Lavalier.

Agente:
- Voz

Datasheet

[Datasheet Sennheiser XS Lav USB-C](datasheets/sp-1305-v1-1-xs-lav-usb-c-en.pdf)

Componente propuesto: **Módulo NFC (SPI/I2C/UART)**

Justificación:

- Proporciona una forma tangible de activar/desactivar el sistema.
- Bajo consumo, fácil integración, múltiples librerías disponibles en Python.

Agente:
- Identificación 
- Activación

Datasheet

[Datasheet NFC PN532](datasheets/PN532_C1.pdf)

Componente propuesto: **Sensor ultrasónico de proximidad (HC-SR04 o similar)**

Justificación:

- Permite detectar la presencia de un usuario frente al asistente, incluso en condiciones de baja iluminación o sin visión directa.
- Complementa la cámara y mejora la capacidad reactiva del sistema ante movimiento cercano.
- Bajo coste, sencillo de integrar con Raspberry Pi a través de GPIO.

Agente:
- Activación
- Entorno físico

Datasheet

[Datasheet HC-SR04](datasheets/HC-SR04.pdf)

Componente propuesto: **Sensor de temperatura y humedad (DHT22 o BME280)**

Justificación:
- Permite a NORA percibir las condiciones ambientales de confort.
- Útil para adaptar comportamientos o emitir recomendaciones ("La temperatura es alta", "Ambiente seco").
- Bajo consumo y sencilla integración por GPIO o I2C.

Agente:
- Confort ambiental
- Salud ambiental

Alternativas:
- AM2302, Si7021, HTU21D

Datasheet:
- [Datasheet BME280](datasheets/bst-bme280-ds002.pdf)

---

Componente propuesto: **Sensor de luminosidad (LDR o TSL2561)**

Justificación:
- Detecta condiciones de luz ambiente para ajustar la expresión visual (pantalla, LEDs).
- Mejora la adaptabilidad del sistema en diferentes entornos.

Agente:
- Contexto visual
- Iluminación

Alternativas:
- BH1750, TEMT6000

Datasheet:
- [Datasheet TSL2561](datasheets/tsl2561-932888.pdf)

---

Componente propuesto: **Módulo Bluetooth (HC-05 o BLE integrado)**

Justificación:
- Permite detectar dispositivos cercanos (móvil del usuario, wearables).
- Posibilidad de emparejamiento con sensores externos o transferencia de datos.

Alternativas:
- HM-10 (BLE), módulo USB BLE CSR

Agente:
- Presencia 
- Emparejamiento

Datasheet:
- [Datasheet HC-05](datasheets/HC-05.PDF)

---

Componente propuesto: **RTC externo (DS3231)**

Justificación:
- Asegura la precisión horaria en ausencia de conectividad.
- Clave para mantener coherencia temporal en eventos y registros.

Alternativas:
- DS1307, RV-3028-C7

Agente:
- Cronología 
- Sistema base de tiempo

Datasheet:
- [Datasheet DS3231](datasheets/ds3231.pdf)

---

Componente propuesto: **Sensor de calidad del aire (MQ-135 o CCS811)**

Justificación:
- Permite estimar la calidad del aire interior y actuar en consecuencia.
- Aumenta la sensibilidad ambiental y posibles funciones de confort o alerta.

Alternativas:
- SGP30, BME680

Datasheet:
- [Datasheet CCS811](datasheets/CCS811_Datasheet-DS000459.pdf)


Componente propuesto:  **Módulo WiFi externo (ESP8266 o similar)**

Justificación:

- Permite añadir conectividad inalámbrica en caso de que la placa base no la tenga integrada o se desee una conexión secundaria.
- Útil para transmisión de datos remota, sincronización de eventos en red o actualización de software OTA (over-the-air).
- Puede configurarse como cliente o punto de acceso, permitiendo una arquitectura más flexible.
- Compatible con múltiples librerías de red en Python y fácil integración con la Raspberry Pi mediante UART o USB.

Agente:

- Conectividad
- Sincronización remota
- Integración en red local o nube

Datasheets:

- [Datasheet ESP8266 (AI-Thinker)](datasheets/ESP8266.PDF)
- [Datasheet NodeMCU v3 con ESP8266](datasheets/NodeMCUV3.pdf)

## 3. Actuadores

Los actuadores permiten que NORA exprese estados, emociones y respuestas mediante sonido, luz o movimiento físico. Este bloque contempla dispositivos de salida interactiva.

Componente propuesto: **Altavoz Miniatura 20 mm 8 Ω 0.8 W + Amplificador PAM8403**

Justificación:

- Reproduce voz generada por el sistema.
- Compatible directamente con salida de audio de la Raspberry Pi.
- Recomendación: altavoz autoamplificado (USB o jack 3.5mm).

Agente:
- Voz (respuesta auditiva)

Datasheets

[Datasheet Altavoz Miniatura 20 mm 8 Ω 0.8 W](datasheets/SPKM.36.8.B.pdf)  
[Datasheet PAM8403 (Amplificador)](datasheets/PAM8403.pdf)

Componente propuesto: **Pantalla facial animada (OLED o TFT SPI)**

Justificación:

- Representación visual del rostro de NORA.
- Comunicación visual directa con el usuario.
- La OLED es más simple; la TFT puede representar más detalles.
- Alternativa recomendada: OLED 0.96” SPI (SSD1306) para prototipos.

Agente:
- Expresividad 
- Comunicación emocional

Datasheets

[Datasheet Pantalla TFT 1.8" SPI – ST7735](datasheets/ST7735.pdf)

Componente propuesto: **Servomotores SG90/MG90**

Justificación:

- Simulan movimientos físicos de atención, asentimiento, orientación.
- Bajo coste, ampliamente soportados.
- SG90 para prototipo; MG90 si se requiere más torque.

Agente:
- Gesticulación
- Orientación física

Datasheets

[Datasheet SG90](datasheets/SG90-datasheet.pdf)  
[Datasheet MG90](datasheets/MG90S_Tower-Pro.pdf)

Componente propuesto: **LEDs indicadores de estado (adicionales)**

Justificación:

- Informan visualmente al usuario sobre el estado del sistema (NFC activo, escucha, error).
- Bajo coste, alta eficiencia para retroalimentación instantánea.
- Controlables individualmente desde GPIO con resistencias limitadoras.

Agente:
- Estado
- Señalización

Datasheets

[Datasheet Rojo de 5 mm](datasheets/TLDR5800.pdf)
[Datasheet Verde de 3 mm](datasheets/204-15UTC-S400-X9.PDF)

Componente propuesto: **LEDs RGB tipo WS2812 (Neopixel)**

Justificación:

- Simbolizan emociones mediante color (alegría, error, espera…).
- Control digital sencillo, se pueden encadenar.

Agente:
- Expresividad visual

Datasheets

[Datasheet WS2812B](datasheets/WS2812B.pdf)

Componente propuesto: **LEDs indicadores de estado (adicionales)**

Justificación:

- Informan visualmente al usuario sobre el estado del sistema (NFC activo, escucha, error).
- Bajo coste, alta eficiencia para retroalimentación instantánea.
- Controlables individualmente desde GPIO con resistencias limitadoras.

Datasheets

[Datasheet Rojo de 5 mm](datasheets/TLDR5800.pdf)  
[Datasheet Verde de 3 mm](datasheets/204-15UTC-S400-X9.PDF)

Componente propuesto: **LED RGB adicional (indicador de estado)**

Justificación:

- Permite representar múltiples estados del sistema (activo, error, escucha, reposo) con un solo componente mediante codificación por color.
- Simplifica el cableado respecto a LEDs individuales por color.
- Puede integrarse discretamente en el diseño físico de NORA, incluso como "ojo simbólico" o indicador en la carcasa.
- Compatible con GPIO y control por PWM desde la Raspberry Pi.
- Alternativa más expresiva y compacta frente a LEDs individuales tradicionales.
- Bajo coste, alta eficiencia para retroalimentación instantánea.
- Controlables individualmente desde GPIO con resistencias limitadoras.

Datasheets

[Datasheet LED RGB de 5 mm – Cátodo Común](datasheets/upload-5mm_RGB_led_common_cathode.pdf)

Componente propuesto: **Módulo expansor I/O PCF8574 (I²C)**

Justificación:

- Permite añadir hasta 8 pines digitales adicionales usando solo dos pines I²C de la Raspberry Pi.
- Ideal para controlar LEDs, interruptores, o señales digitales de bajo requerimiento temporal.
- Facilita la integración de múltiples módulos sin agotar los GPIOs nativos.
- Compatible con Raspberry Pi mediante librerías Python (como smbus2, RPi.GPIO extendido, etc.).
- Bajo coste, tamaño reducido y posibilidad de usar múltiples unidades (direcciones I²C configurables).

Agente:
- Control físico distribuido 
- Gestión GPIO extendida

Datasheets

[Datasheet PCF8574](datasheets/pcf8574.pdf)



## 4. Estructura y soporte

Este bloque contempla los elementos que permiten montar, proteger y alimentar físicamente al sistema. Proporciona la base física estable para todo el hardware.

Componente propuesto: **Chasis físico o carcasa impresa**

Justificación:

- Soporta e integra todos los componentes físicos de manera organizada.
- Facilita el ensamblado seguro, la disipación térmica y la estética general del sistema.
- Puede personalizarse mediante impresión 3D o diseño artesanal.

Componente propuesto: **Fuente de alimentación 5V 3A (conexión a red eléctrica)**

Justificación:

- Alimenta la Raspberry Pi y todos los periféricos de forma continua y estable.
- Recomendado usar la fuente oficial USB-C de Raspberry Pi (5.1 V 3 A) o fuente conmutada AC-DC de calidad.
- Permite funcionamiento prolongado sin interrupciones, alimentada directamente desde enchufe de pared.

Datasheet

[Link ALIMENTADOR OFICIAL RASPBERRY PI 4 USB-C 5V 3A 15W NEGRO](https://www.tiendatec.es/raspberry-pi/raspberry-pi-alimentacion/1093-alimentador-oficial-raspberry-pi-4-usb-c-5v-3a-15w-negro-644824914886.html)
[Link ALIMENTADOR OFICIAL RASPBERRY PI 4 USB-C 5V 3A 15W NEGRO](https://raspipc.es/1759)

## Base de datos

Componente propuesto:  **Almacenamiento externo (HDD/SSD vía USB)**

  Justificación:
  - Permite extender significativamente la capacidad de almacenamiento local de NORA.
  - Útil para guardar archivos grandes: historiales de vídeo/audio, backups completos, registros prolongados, modelos de IA entrenados, multimedia generada.
  - Ideal para preservar integridad de datos a largo plazo y facilitar exportaciones externas.
  - Conectividad simple mediante USB 2.0/3.0 con soporte nativo en Raspberry Pi.
    Agente:

Agente:
- Datos persistentes 
- Gestión multimedia 
- Soporte de archivos históricos

Datasheets:

- [Ejemplo SSD – Disco Duro Kingston A400 480Gb Disco SSD SATA3 500MB/S](datasheets/SA400S37_latam.pdf)
- [Ejemplo HDD – Seagate Barracuda 1TB](datasheets/barracuda-ds1737-1-1111us.pdf)

## 6. Resumen por agente

Esta sección sintetiza la relación entre los agentes perceptivos y expresivos del sistema NORA y los componentes físicos involucrados en su operación.

| Agente              | Componentes físicos asociados                             |
| ------------------- | --------------------------------------------------------- |
| Voz                 | Micrófono USB, Altavoz + Amplificador                     |
| Percepción visual   | Cámara CSI/USB, Pantalla OLED/TFT                         |
| Expresividad visual | Pantalla OLED/TFT, LEDs RGB WS2812, LED RGB adicional     |
| Activación          | Módulo NFC, Sensor ultrasónico, Botón físico opcional     |
| Estado              | LEDs de estado, LED RGB adicional                         |
| Cronología          | RTC DS3231                                                |
| Confort ambiental   | Sensor de temperatura/humedad, Sensor de calidad del aire |
| Entorno físico      | Sensor de luminosidad, Sensor ultrasónico                 |
| Gestión GPIO extra  | Expansor PCF8574                                          |
| Conectividad        | Módulo WiFi adicional (si no integrado)                   |

## 7. Componentes opcionales para extensiones futuras

Esta sección incluye componentes no imprescindibles en la primera iteración del sistema, pero considerados útiles para versiones futuras:

- **Pantalla táctil capacitiva**: para interacción directa y ampliación del input de usuario.
- **Sensor NDIR de CO₂**: para estimaciones precisas de la calidad del aire interior.
- **Módulo IMU (MPU-6050)**: para percepción del movimiento o inclinación de NORA.
- **Power bank USB 5V**: como fuente redundante ante corte eléctrico breve.
- **Cámara USB alternativa**: en caso de fallo del puerto CSI o necesidad de flexibilidad.

## 8. Activación de componentes según estados y emociones

A continuación, se indican algunos ejemplos de cómo los componentes físicos se activan en función de los estados internos y emociones simuladas de NORA:

- Estado `ESCUCHA`:
  - Iluminación azul (LED RGB / WS2812)
  - Pantalla facial muestra atención (ojos abiertos, cejas altas)
  - Activación de ASR y micrófono

- Estado `ERROR`:
  - Iluminación roja intermitente (LED rojo / RGB)
  - Rostro con gesto de duda o frustración (pantalla)
  - Voz clara con disculpa o repetición de orden

- Emoción “alegría”:
  - Luz verde o amarilla brillante
  - Sonrisa en pantalla facial
  - Voz animada con entonación alta

Estas correspondencias aseguran una respuesta coherente y multimodal ante el usuario, reforzando la expresividad y legibilidad emocional de NORA.
