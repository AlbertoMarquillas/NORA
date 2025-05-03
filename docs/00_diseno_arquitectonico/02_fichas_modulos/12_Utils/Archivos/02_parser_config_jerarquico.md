# Ficha Funcional – `parser_config_jerarquico.py`

## Nombre del archivo:
`parser_config_jerarquico.py`

## Responsabilidad principal:
Leer y validar archivos de configuración jerárquicos y anidados en el sistema NORA, aplicando validación de esquemas y resolviendo referencias internas. Facilita la gestión de configuraciones complejas de módulos avanzados.

## Entradas esperadas:
- **Tipo de entrada:** Rutas de archivos de configuración complejos, esquemas de validación opcionales.
- **Fuente:** `sistema/`, `control/`, `voz/`, `vision/`, `datos/`, `agentes/`.
- **Formato o protocolo:** Archivos `.json`, `.yaml` con estructuras jerárquicas.

## Salidas generadas:
- **Tipo de salida:** Diccionarios estructurados validados, configuraciones resueltas.
- **Destinatario:** Módulos funcionales que requieran configuraciones anidadas.
- **Ejemplo de salida:**
  - Configuración de red con múltiples interfaces
  - Definición de flujos de diálogo con estructura multinivel

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `control/`, `voz/`, `vision/`, `datos/`, `agentes/`.
- **Salida hacia:** Módulos funcionales.
- **Comunicación bidireccional con:** No aplica (entrega de estructuras de datos).

## Dependencias técnicas:
- **Librerías externas:** `json`, `yaml`, `jsonschema`, `os`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Validación contra esquemas JSON Schema opcionales.

## Notas adicionales:
`parser_config_jerarquico.py` debe ser capaz de identificar configuraciones anidadas, aplicar validaciones recursivas y resolver referencias internas si las configuraciones incluyen vínculos o parámetros derivados. Su uso es esencial en módulos que manejan flujos dinámicos o configuraciones estructuralmente complejas en NORA.

