# Funcionamiento del Módulo SSD1306 en Modo SPI

## 1. Descripción General

El módulo **SSD1306** es un controlador de pantallas OLED monocromáticas utilizado para gestionar pequeñas pantallas gráficas. En el sistema NORA, se emplea una variante de 0.96" configurada para comunicación vía **SPI** (Serial Peripheral Interface), permitiendo una actualización rápida y eficiente de la información visual.

## 2. Interfaz de Comunicación

**Modo seleccionado:** SPI 4-hilos más control de comandos y reset.

**Pines funcionales:**

| Pin del módulo | Función | Descripción |
|:----------------|:--------|:------------|
| GND | Tierra | Conexión a masa común. |
| VCC | Alimentación | 3.3V o 5V según especificación del módulo. |
| D0 | SCLK | Reloj de comunicación SPI (del maestro a la pantalla). |
| D1 | MOSI | Datos enviados desde la Raspberry Pi a la pantalla. |
| RES | Reset | Reinicio físico del controlador. |
| DC | Data/Command | Selección entre comandos de control o datos de visualización. |
| CS | Chip Select | Activación del dispositivo en el bus SPI. |

## 3. Flujo de Funcionamiento Típico

1. **Inicialización física:**
   - Establecer los GPIOs de `RES` y `DC` como salidas.
   - Realizar un reset hardware aplicando una señal de bajo nivel corto en `RES`.

2. **Configuración del SPI:**
   - Activar el controlador SPI0 en Raspberry Pi.
   - Configurar el SPI en modo adecuado (modo 0: CPOL=0, CPHA=0).
   - Velocidad típica recomendada: entre 1 MHz y 8 MHz.

3. **Inicialización del SSD1306:**
   - Enviar secuencia de comandos de configuración: setting de display offset, multiplex ratio, charge pump activation, etc.
   - Estas instrucciones se transmiten con la señal `DC` en bajo (modo comando).

4. **Envío de datos de visualización:**
   - Establecer `DC` en alto.
   - Enviar vía SPI los bytes que representan la imagen gráfica a mostrar.

5. **Actualización continua:**
   - Para animaciones o cambios de estado, repetir el proceso de envío de datos.

## 4. Esquema Básico de Funcionamiento

```text
+---------------+              +-------------------+
| Raspberry Pi  | -- SPI -----> | Pantalla SSD1306   |
| (Maestro)     |              | (Esclavo SPI)      |
+---------------+              +-------------------+
       |                                |
      RES                              Reset
      DC                               Data/Command select
      CS                               Chip Select
```

## 5. Consideraciones para Integración

- **Voltaje de alimentación:** Confirmar compatibilidad con 3.3V en caso de duda; evitar conexión directa a 5V si no está especificado.
- **Activación de SPI:** Habilitar SPI mediante `raspi-config` en la Raspberry Pi.
- **Drivers recomendados:** Uso de librerías como `luma.oled` o `Adafruit_Python_SSD1306` en modo SPI.
- **Gestón eficiente:** Implementar doble buffer en memoria para evitar parpadeos perceptibles al actualizar pantalla.

## 6. Librerías Python sugeridas

- `luma.oled`
- `spidev`
- `RPi.GPIO` o `gpiozero` para gestión de `RES`, `DC`, `CS` si se maneja manualmente.

## 7. Conclusión

La operación del módulo SSD1306 en modo SPI proporciona una solución eficiente para la visualización de información gráfica simple dentro del sistema NORA, garantizando tiempos de respuesta rápidos y un consumo energético reducido.

