# Cambio de Pantalla en el Sistema NORA

## 1. Contexto Inicial

Durante la fase de prototipo del sistema NORA, se ha seleccionado como dispositivo de expresividad visual primaria una pantalla:

- **Modelo:** OLED 0.96” SPI
- **Controlador:** SSD1306
- **Interfaz:** SPI (Serial Peripheral Interface)

La decisión responde a criterios de eficiencia, simplicidad de integración y bajo consumo eléctrico.


## 2. Justificación de la Elección Actual

**Ventajas del OLED SSD1306:**

- **Bajo consumo:** Ideal para operación continua sin sistemas de refrigeración activa.
- **Circuitería sencilla:** Sin necesidad de conversores de nivel de voltaje para 3.3V.
- **Librerías maduras en Python:** Compatibilidad directa con `Adafruit_SSD1306`, `luma.oled`, entre otras.
- **Facilidad de montaje:** Módulo compacto y ligero.
- **Velocidad de actualización:** Adecuada para mostrar animaciones simples como parpadeos, sonrisas o expresiones simbólicas.

**Limitaciones identificadas:**

- **Resolución limitada:** 128×64 píxeles monocromáticos.
- **Expresividad visual restringida:** No permite representar emociones complejas a través de colores o detalles visuales elaborados.


## 3. Plan de Migración Futura

En futuras iteraciones, se contempla la posibilidad de actualizar la pantalla a un modelo:

- **Modelo sugerido:** TFT 1.8” SPI
- **Controlador:** ST7735 (o compatibles)
- **Resolución:** 160×128 píxeles, 65K colores (RGB)

**Impactos esperados:**

| Ámbito | Impacto | Nivel de modificación |
|:--------|:-------|:---------------------|
| Hardware (cableado) | Mínimo: conexiones SPI muy similares | Bajo |
| Software (driver) | Cambio de librería de pantalla (de `luma.oled` a `luma.lcd` o `Adafruit_ST7735`) | Medio |
| Lógica de expresividad | Si se aísla correctamente, no debería cambiar | Bajo |
| Consumo de energía | Aumento moderado por retroiluminación | Bajo-moderado |
| Capacidad expresiva | Aumento considerable | Muy alto |


## 4. Recomendaciones para facilitar el cambio

- **Abstraer el control de pantalla:** Implementar funciones genéricas como `mostrar_emocion(emocion)` o `actualizar_estado_visual(estado)`, sin codificar directamente llamadas específicas a la pantalla OLED.
- **Separar la inicialización de hardware:** Crear un archivo de configuración donde se especifique el tipo de pantalla activo.
- **Utilizar drivers modulares:** Asegurar que el cambio de librería solo afecte al módulo de inicialización de pantalla.
- **Prever funciones para color:** Aunque el OLED actual es monocromo, estructurar funciones gráficas considerando parámetros de color opcionales.


## 5. Conclusión

El uso inicial del **OLED SSD1306** es plenamente adecuado para la fase de prototipo funcional de NORA. Garantiza bajo consumo, simplicidad de integración y madurez de software.

La migración futura a una pantalla **TFT ST7735** es factible, con impacto contenido, siempre que se sigan buenas prácticas de abstracción en el diseño de la interfaz visual. Esto permitirá escalar la expresividad de NORA de manera fluida, mejorando la calidad de la interacción sin una reestructuración profunda del sistema.