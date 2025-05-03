# 04 – Diagrama Conceptual del Sistema NORA

Este documento contiene la representación gráfica y estructurada del sistema NORA, organizada por bloques funcionales y basada en el esquema lógico definido en documentos anteriores. El diagrama ha sido diseñado para ser claro, modular y fácilmente extensible, cumpliendo los requisitos de presentación y documentación técnica.

---

## 1. Objetivo

Reproducir el esquema conceptual de hardware y software del sistema NORA mediante una herramienta gráfica estandarizada (Draw.io), facilitando su uso como material de referencia para el desarrollo, mantenimiento y presentación del proyecto.

---

## 2. Herramienta Utilizada

**draw.io (diagrams.net)**

- Formato editable: `.drawio`
- Formatos exportados: `.pdf` y `.png`
- Estructura modular con colores diferenciados

---

## 3. Criterios de Diseño

- **Claridad visual:** Se evitaron solapamientos y líneas cruzadas. Los bloques están espaciados y agrupados.
- **Uso de formas estándar:** Rectángulos para software, redondeadas para hardware, líneas punteadas para agentes.
- **Colores por categoría:**
  - Verde: sensores físicos
  - Azul: módulos de entrada
  - Naranja: módulos de salida
  - Gris: infraestructura
  - Púrpura: agentes
  - Amarillo: núcleo del sistema
- **Etiquetado explícito:** Cada componente está identificado con su nombre funcional.

---

## 4. Estructura del Diagrama

### A. Bloques de Hardware

Organizados en cuatro subcategorías:

1. **Entrada directa (usuario):**
   - Micrófono USB
   - Cámara CSI/USB
   - Sensor ultrasónico
   - Módulo NFC
   - Módulo Bluetooth
   - Botón físico GPIO

2. **Sensores ambientales:**
   - Sensor temperatura/humedad (DHT22/BME280)
   - Sensor de luz (TSL2561)
   - Sensor de calidad del aire (MQ135/CCS811)
   - RTC DS3231

3. **Salida y expresión:**
   - Altavoz + amplificador
   - Pantalla OLED/TFT
   - LEDs RGB / indicadores
   - Servomotores SG90/MG90

4. **Infraestructura y soporte:**
   - Raspberry Pi 4 Model B
   - Alimentación 5V 3A
   - Almacenamiento externo (HDD/SSD)
   - Expansor I/O (PCF8574)
   - Módulo WiFi externo (ESP8266)

---

### B. Bloques de Software

Organizados según funcionalidad:

1. **Entrada sensorial:** `voz/`, `vision/`, `sensores/`, `activacion/`
2. **Coordinación inteligente:** `agentes/`
3. **Núcleo lógico:** `sistema/`
4. **Expresión y salida:** `interfaz/`, `voz/`, `dialogo/`
5. **Persistencia:** `datos/`
6. **Control físico:** `control/`
7. **Interfaz técnica:** `gui/`
8. **Soporte auxiliar:** `models/`, `utils/`, `tests/`

---

### C. Módulo de Agentes

Ubicado como capa intermedia que modula:

- Entradas desde: `voz/`, `vision/`, `sensores/`
- Salidas hacia: `interfaz/`, `sistema/`, `dialogo/`, `datos/`

Funciones principales:
- Coordinación perceptiva y expresiva
- Gestión de prioridades
- Evaluación contextual
- Modulación emocional

---

## 5. Exportaciones Disponibles

- **[diagrama_nora_conceptual.pdf](diagramas/diagrama_nora_conceptual.pdf)**  
- **[diagrama_nora_conceptual.png](diagramas/diagrama_nora_conceptual.png)**  

---

## 6. Observaciones Finales

Este diagrama constituye la referencia visual oficial del sistema NORA. Toda modificación de arquitectura deberá actualizar este documento y el archivo fuente gráfico correspondiente. Se recomienda mantener consistencia con la documentación técnica y estructural para facilitar escalabilidad futura.