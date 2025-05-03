# Ficha Funcional – `utils_main.py`

## Nombre del archivo:
`utils_main.py`

## Responsabilidad principal:
Coordinar el acceso a las funciones auxiliares del módulo `utils/` de NORA. Centraliza la importación de utilidades comunes, facilitando su disponibilidad organizada para todos los módulos funcionales del sistema.

## Entradas esperadas:
- **Tipo de entrada:** Solicitudes internas de servicios auxiliares (parsing, logging, cálculos, eventos, temporización).
- **Fuente:** `sistema/`, `voz/`, `vision/`, `interfaz/`, `control/`, `datos/`, `agentes/`.
- **Formato o protocolo:** Llamadas a funciones o instancias de utilidades.

## Salidas generadas:
- **Tipo de salida:** Acceso a funciones utilitarias centralizadas.
- **Destinatario:** Todos los módulos funcionales.
- **Ejemplo de salida:**
  - Funciones de parsing de configuración
  - Funciones de generación de eventos
  - Funciones matemáticas y de normalización

## Módulos relacionados:
- **Entrada desde:** Todos los módulos funcionales del sistema.
- **Salida hacia:** Submódulos de `utils/`.
- **Comunicación bidireccional con:** No aplica (coordinación pasiva).

## Dependencias técnicas:
- **Librerías externas:** `os`, `json`, `yaml`, `logging`, `math`, `datetime`, `numpy`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Uso interno de utilidades.

## Notas adicionales:
`utils_main.py` debe actuar como un punto de acceso unificado a las utilidades comunes, evitando duplicación de importaciones en los módulos principales. Facilita la modularidad, la legibilidad y el mantenimiento del código, asegurando una estructura organizada y escalable del sistema de utilidades.