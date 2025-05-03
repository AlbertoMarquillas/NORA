# Ficha Funcional – `utils_control.py`

## Nombre del archivo:
`utils_control.py`

## Responsabilidad principal:
Proporcionar funciones auxiliares de soporte para el módulo `control/`, incluyendo utilidades de acceso y configuración de hardware, manipulación de GPIOs, lectura de sensores de sistema, control de temporizadores y generación de logs estructurados.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes de funciones auxiliares, parámetros de hardware o sistema.
- **Fuente:** `control_main.py`, submódulos de `control/`.
- **Formato o protocolo:** Llamadas internas a funciones utilitarias.

## Salidas generadas:
- **Tipo de salida:** Resultados de funciones de soporte, lecturas de estado, logs de operaciones auxiliares.
- **Destinatario:** `control_main.py`, submódulos de `control/`, `sistema/`.
- **Ejemplo de salida:**
  - Estado de un pin GPIO
  - Resultado de un test de conectividad
  - Log de operación auxiliar

## Módulos relacionados:
- **Entrada desde:** `control_main.py`, `supervision_estado.py`, `gestion_expansor_io.py`, `gestion_energia.py`, etc.
- **Salida hacia:** `control_main.py`, submódulos de `control/`.
- **Comunicación bidireccional con:** Sistema operativo y GPIOs.

## Dependencias técnicas:
- **Librerías externas:** `RPi.GPIO`, `smbus2`, `psutil`, `os`, `subprocess`, `time`, `logging`.
- **Hardware gestionado:** GPIOs, expansores I/O, interfaces de sistema.
- **Protocolos:** GPIO, I2C.

## Notas adicionales:
`utils_control.py` facilita la modularización del código del módulo `control/`, permitiendo evitar redundancias y estandarizar operaciones comunes como lectura de temperaturas, control de pines digitales, mediciones de carga del sistema o manejo de errores recurrentes. Su diseño debe ser sencillo, robusto y extensible.