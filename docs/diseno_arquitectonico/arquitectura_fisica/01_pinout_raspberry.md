# Pinout de la Raspberry Pi – Asignación de Pines GPIO

**Objetivo:**  
Este documento contiene la revisión del pinout oficial de la Raspberry Pi utilizada en el proyecto, detallando las funciones de cada pin GPIO, con especial énfasis en los pines PWM, I²C, SPI, UART, y las consideraciones eléctricas. Esto es esencial para una asignación precisa y evitar conflictos por funciones reservadas.

## 1. Resumen del Pinout

### 1.1 Pines con Salida PWM
Los pines con capacidad PWM por defecto son:

| Pin GPIO | Función          | Comentarios                             |
|----------|------------------|-----------------------------------------|
| GPIO12   | PWM              | Para controlar servomotores.            |
| GPIO13   | PWM              | Para controlar servomotores.            |
| GPIO18   | PWM              | Para control de frecuencia o luz.       |
| GPIO19   | PWM              | Para control de frecuencia o luz.       |

### 1.2 Pines I²C
Los pines I²C son utilizados para la comunicación con dispositivos como sensores y expansores de E/S.

| Pin GPIO | Función          | Comentarios                             |
|----------|------------------|-----------------------------------------|
| GPIO2    | SDA (I²C Data)   | Línea de datos I²C.                     |
| GPIO3    | SCL (I²C Clock)  | Línea de reloj I²C.                     |

### 1.3 Pines SPI
Los pines SPI se usan para la comunicación de alta velocidad con dispositivos periféricos como pantallas o tarjetas SD.

| Pin GPIO | Función          | Comentarios                             |
|----------|------------------|-----------------------------------------|
| GPIO10   | MOSI             | Master Out Slave In (Datos de salida).  |
| GPIO11   | SCK              | Clock (Reloj de sincronización).       |
| GPIO9    | MISO             | Master In Slave Out (Datos de entrada). |

### 1.4 Pines UART
Los pines UART permiten la comunicación serie con otros dispositivos.

| Pin GPIO | Función          | Comentarios                             |
|----------|------------------|-----------------------------------------|
| GPIO14   | TX (Transmisión) | Línea de transmisión de datos.         |
| GPIO15   | RX (Recepción)   | Línea de recepción de datos.           |

## 2. Observaciones Relevantes

### 2.1 Evitar Duplicidad de Funciones en Pines Compartidos
Es importante tener en cuenta que algunos pines de la Raspberry Pi pueden tener múltiples funciones asignadas, como los pines de UART que pueden usarse para SPI en algunos casos. Asegúrate de verificar qué otros módulos o funciones están utilizando un pin antes de asignarlo a un componente específico.

### 2.2 Limitación de Pines Disponibles para PWM
Existen solo 4 pines PWM por defecto en la Raspberry Pi (GPIO12, 13, 18, 19). Si el proyecto requiere más pines PWM, se pueden usar expansores I/O como el **PCF8574** (por I²C) para añadir más pines digitales, pero para PWM se debe tener en cuenta que la Raspberry Pi no soporta más pines PWM de forma nativa.

### 2.3 Consideraciones Eléctricas
- **3.3V vs 5V**: Muchos de los pines GPIO de la Raspberry Pi funcionan a **3.3V**. No es recomendable conectar dispositivos que operen a 5V directamente a los pines GPIO sin un convertidor de nivel, ya que esto podría dañar la placa.
- **GND**: Asegúrate de conectar todos los componentes que necesitan alimentación a uno de los pines **GND** de la Raspberry Pi.

## 3. Enlace al Diagrama Oficial

Consulta el diagrama oficial de pines de la Raspberry Pi utilizada en el proyecto en el siguiente enlace:  
[Pinout de la Raspberry Pi](https://pinout.xyz)

---

Este documento se actualizará conforme avance el proyecto y se vayan definiendo las conexiones exactas para evitar cualquier posible conflicto de pines.
