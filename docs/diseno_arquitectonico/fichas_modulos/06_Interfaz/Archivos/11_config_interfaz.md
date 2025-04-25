# Ficha Funcional – `config_interfaz.py`

## Nombre del archivo:
`config_interfaz.py`

## Responsabilidad principal:
Definir los parámetros gráficos y de visualización para la interfaz de NORA, incluyendo configuraciones de colores, tiempos de animación, y otros parámetros relacionados con las salidas visuales y físicas del sistema. Este archivo permite ajustar dinámicamente el comportamiento visual de NORA, haciendo que las expresiones y animaciones se adapten a las preferencias del sistema o del usuario.

## Entradas esperadas:
- **Tipo de entrada:** Parámetros de configuración gráfica, valores de tiempo, configuraciones de colores, ajustes de animación.
- **Fuente:** Archivos de configuración, configuraciones del sistema, módulos `sistema/`, `agentes/`, `interfaz/` que modifican la apariencia y tiempos de las animaciones.
- **Formato o protocolo:** Archivos de configuración (`config.json` o similares), parámetros de color y tiempo en formato JSON.

## Salidas generadas:
- **Tipo de salida:** Actualización de las configuraciones gráficas, colores de LEDs, tiempos de animación, parámetros de visualización.
- **Destinatario:** `interfaz/`, `agentes/`, `sistema/` (para aplicar los parámetros de configuración a las salidas visuales y físicas).
- **Ejemplo de salida:**
  - `AGT_COLOR_SCHEME_UPDATED` (Evento que indica que el esquema de colores ha sido actualizado).
  - `CMD_UPDATE_ANIMATION_TIMING` (Instrucción para ajustar los tiempos de animación según los parámetros configurados).
  - `EVT_CONFIGURATION_APPLIED` (Evento que confirma que la configuración de la interfaz ha sido aplicada correctamente).

## Módulos relacionados:
- **Entrada desde:** Archivos de configuración (`config.json`), configuraciones del sistema (`sistema/`), parámetros de color y tiempo definidos en otros módulos.
- **Salida hacia:** `interfaz/`, `sistema/`, `agentes/` (para aplicar las configuraciones y parámetros gráficos).
- **Comunicación bidireccional con:** `interfaz/`, `sistema/` para asegurar que las configuraciones sean consistentes con el comportamiento global de NORA.

## Dependencias técnicas:
- **Librerías externas:** `json` (para leer y escribir archivos de configuración), `Pillow` (para gestionar imágenes y animaciones gráficas), `RPi.GPIO` (si se usa para configuración de hardware como LEDs o servomotores).
- **Hardware gestionado:** Pantalla OLED/TFT, LEDs RGB WS2812 (Neopixels), servomotores SG90/MG90.
- **Protocolos:** I2C, SPI, eventos internos para manejar la configuración de la interfaz gráfica.

## Notas adicionales:
Este archivo es fundamental para la personalización del comportamiento visual de NORA. A través de `config_interfaz.py`, se pueden definir todos los parámetros que afectan la apariencia visual y la experiencia del usuario, como los colores de los LEDs, los tiempos de animación, o los ajustes de visualización. La capacidad de modificar estos parámetros dinámicamente hace que el sistema sea flexible y adaptable, permitiendo ajustarlo a las preferencias del usuario o las necesidades específicas de la situación.

## Archivos previstos del módulo:
- `config_interfaz.py`: Configuración de parámetros gráficos, colores, tiempos de animaciones (este archivo).
- Archivos adicionales como `interfaz_main.py`, `pantalla_facial.py`, `leds_rgb.py`.
