### Módulo: Comunicación Bluetooth – HC-05

Este módulo proporciona conectividad inalámbrica básica por Bluetooth utilizando el transceptor HC-05. Se utiliza para enviar o recibir comandos desde dispositivos móviles o para activar el sistema NORA mediante eventos externos gestionados por el módulo `activacion/` o `sensores/`.

---

#### 1. Descripción funcional del conjunto

El HC-05 permite comunicación UART con un microcontrolador a través de los pines `TXD` y `RXD`. La alimentación se proporciona a 5 V, mientras que las señales UART se adaptan a niveles seguros mediante un divisor resistivo para `BT_RX`.

---

#### 2. Componentes principales

**a) Módulo Bluetooth HC-05 (HC1)**

* Alimentación: 5 V.
* Lógica UART a nivel TTL 3.3 V (aunque tolera 5 V en `TXD`).
* Pines relevantes:

  * `TXD`: salida de datos desde el módulo.
  * `RXD`: entrada de datos desde el microcontrolador.
  * `KEY` y `STATE`: no utilizados en este esquema (configuración AT y estado).

**b) Divisor de tensión para `BT_RX`**

* `R1_DIV_BLE` = 2 kΩ
* `R2_DIV_BLE` = 1 kΩ
* Reduce nivel de 5 V a \~3.3 V en la entrada `RXD` del HC-05.

---

#### 3. Observaciones técnicas

* El divisor resistivo está correctamente dimensionado para proteger el pin `RXD` del módulo.
* La línea `BT_TX` se conecta directamente al controlador, que debe ser capaz de leer niveles de 3.3 V como lógicos altos (típico en Raspberry Pi).
* Las líneas `KEY` y `STATE` están sin uso; esto es válido si el módulo opera solo en modo esclavo por defecto.
* Las masas están correctamente unidas para evitar errores de comunicación UART.

---

#### 4. Recomendaciones

* Si se planea reconfigurar el módulo por comandos AT, conectar también el pin `KEY` y diseñar lógica para activarlo.
* Documentar si el módulo funciona en modo esclavo o maestro, y a qué velocidad UART está configurado (por defecto 9600 baudios).
* Añadir protección contra inversión de polaridad o corto en alimentación si el módulo se intercambia frecuentemente.

---

#### 5. Conclusión

El módulo está correctamente integrado con adaptación de niveles adecuada para comunicación UART. Es funcional para activar eventos o intercambiar datos con el sistema. Para configuración avanzada o depuración, podría contemplarse el uso del pin `KEY`.
