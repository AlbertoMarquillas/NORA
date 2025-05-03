### Módulo: Pantalla OLED 0.96” – SSD1306 (SPI)

Este módulo permite la visualización gráfica en el sistema NORA a través de una pantalla OLED de 0.96 pulgadas controlada por el controlador SSD1306 mediante interfaz SPI. Es utilizado por el módulo `interfaz/` para mostrar expresividad visual, estado del sistema o interacciones básicas.

---

#### 1. Descripción funcional del conjunto

La pantalla se comunica con el controlador principal mediante bus SPI. Dispone de líneas dedicadas para `CS` (chip select), `DC` (data/command) y `RST` (reset), además de las líneas estándar `SCLK` y `MOSI`. Alimentación y masa provienen de las líneas compartidas de 5 V y GND.

---

#### 2. Componentes principales

**a) Pantalla OLED SSD1306 (U3)**

* Controlador: SSD1306 en modo SPI.
* Resolución típica: 128×64 píxeles.
* Pines relevantes:

  * `SCLK`: reloj SPI.
  * `MOSI`: datos SPI.
  * `CS`: chip select.
  * `DC`: indica si el dato es comando o contenido.
  * `RST`: reinicio de la pantalla.
* Alimentación: 5 V.

**b) Condensador de desacoplo (C9 – 100 nF)**

* Entre VCC y GND.
* Filtra rizado de alimentación local para estabilidad del módulo.

---

#### 3. Observaciones técnicas

* El uso de SPI mejora la velocidad de actualización respecto al modo I2C.
* La línea `RST` permite reinicio controlado desde software.
* El controlador SSD1306 es ampliamente soportado por librerías como `Adafruit_SSD1306` o `luma.oled` en Python.

---

#### 4. Recomendaciones

* Confirmar compatibilidad de niveles lógicos: si la pantalla opera internamente a 3.3 V, las señales SPI desde un sistema a 5 V podrían requerir adaptación.
* Añadir resistencia pull-up (\~10 kΩ) en `RST` si no se inicializa activamente desde el software.
* Documentar el pinout real del módulo físico si difiere del orden lógico del SSD1306.

---

#### 5. Conclusión

El módulo está correctamente diseñado para operar en modo SPI con todos los pines necesarios accesibles. Se recomienda verificar compatibilidad de niveles eléctricos y asegurar la inicialización por software para una operación estable.
