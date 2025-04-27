## 05 Conexiones Funcionales entre Módulos

Esta capa adicional en el diagrama representa los flujos de información, control o energía entre los distintos componentes. Se utiliza para enriquecer la comprensión del sistema sin sobrecargar el diseño.

### Tipología de Conexiones Funcionales

| Tipo de conexión | Ejemplo                   | Color sugerido | Estilo              |
| ---------------- | ------------------------- | -------------- | ------------------- |
| Datos digitales  | I2C, UART, SPI, USB, BLE  | Azul           | Línea continua      |
| Control lógico   | GPIO, eventos FSM         | Naranja        | Línea continua fina |
| Flujo multimedia | Audio, vídeo              | Verde oscuro   | Línea gruesa        |
| Alimentación     | 5V, GND                   | Rojo oscuro    | Línea punteada      |
| Flujo abstracto  | Eventos software-software | Gris           | Línea punteada      |

### Conexiones específicas a representar

- `Micrófono` → `voz/` [Audio – Verde]
- `Cámara` → `vision/` [Vídeo – Verde]
- `Sensor HC-SR04` → `sensores/` [GPIO – Naranja]
- `NFC` → `sensores/` [I2C/UART – Azul]
- `Sensores ambientales` → `sensores/` [I2C – Azul]
- `Pantalla, LEDs, Servos` ← `interfaz/` [PWM/SPI – Naranja]
- `Altavoz` ← `voz/` [Audio – Verde]
- `Expansor PCF8574` ↔ `control/` [I2C – Azul]
- `WiFi externo` ↔ `control/` [UART – Azul]
- `Botón físico` → `activacion/` [GPIO – Naranja]
- `SSD/HDD externo` ↔ `datos/` [USB – Azul]

**Conexiones software ↔ software:**

- `vision/`, `voz/`, `sensores/` → `agentes/` [Eventos – Gris punteado]
- `agentes/` → `interfaz/`, `voz/`, `sistema/` [Modulación – Gris punteado]
- `activacion/` → `sistema/` [Cambio de estado – Naranja]
- `sistema/` → `interfaz/`, `voz/`, `dialogo/` [Comandos – Naranja]
- `voz/` ↔ `dialogo/` [Texto – Azul]
- `sistema/` ↔ `datos/` [Acceso – Azul]
- `gui/` ↔ módulos varios [Supervisión – Azul]
- `tests/` → todos [Pruebas – Gris claro punteado]

### Recomendaciones gráficas

- Usa capas separadas en la herramienta (ej. `Hardware`, `Software`, `Conexiones`, `Agentes`).
- Utiliza curvas o puntos de anclaje para evitar cruces.
- Etiqueta líneas con `I2C`, `UART`, `GPIO`, `Video`, `Evento`, etc.
- Incluye leyenda de colores y tipos de línea.

---

## 4. Exportación del Diagrama

El diagrama fue implementado en [nombre de la herramienta utilizada] y exportado en los siguientes formatos:

- Formato visual: `diagrama_nora_funcional.png` y `diagrama_nora_funcional.pdf`
- Formato editable: `diagrama_nora_funcional.drawio`

---

## 5. Links al archivo

- [Diagrama funcional (PNG)](diagramas/diagrama_nora_funcional.png)
- [Diagrama funcional (PDF)](diagramas/diagrama_nora_funcional.pdf)


---

## 6. Próximos pasos

- Finalizar representación de conexiones funcionales sin ambigüedades.
- Validar visualmente con el equipo técnico.
- Preparar la siguiente subtarea: representación de interacción usuario ↔ sistema.

