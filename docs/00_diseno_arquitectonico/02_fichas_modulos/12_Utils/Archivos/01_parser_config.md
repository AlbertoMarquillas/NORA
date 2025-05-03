# Ficha Funcional – `parser_config.py`

## Nombre del archivo:
`parser_config.py`

## Responsabilidad principal:
Leer, validar y proporcionar acceso estructurado a archivos de configuración del sistema NORA, en formatos comunes como JSON, YAML o INI. Permite cargar parámetros de operación de forma flexible y centralizada.

## Entradas esperadas:
- **Tipo de entrada:** Rutas de archivos de configuración, esquemas de validación opcionales.
- **Fuente:** `sistema/`, `control/`, `voz/`, `vision/`, `datos/`, `agentes/`.
- **Formato o protocolo:** Archivos `.json`, `.yaml`, `.ini`.

## Salidas generadas:
- **Tipo de salida:** Diccionarios o estructuras de datos validadas.
- **Destinatario:** Módulos funcionales que requieran parámetros de configuración.
- **Ejemplo de salida:**
  - Diccionario con parámetros de red
  - Configuración de umbrales de sensores cargada dinámicamente

## Módulos relacionados:
- **Entrada desde:** `sistema/`, `control/`, `voz/`, `vision/`, `datos/`, `agentes/`.
- **Salida hacia:** Módulos funcionales.
- **Comunicación bidireccional con:** No aplica (lectura y entrega de datos).

## Dependencias técnicas:
- **Librerías externas:** `json`, `yaml`, `configparser`, `os`.
- **Hardware gestionado:** Ninguno.
- **Protocolos:** Manejo de formatos de configuración estándar.

## Notas adicionales:
`parser_config.py` debe asegurar una carga segura y robusta de configuraciones, validando la existencia de campos esenciales y reportando errores claros en caso de inconsistencias. Debe soportar configuraciones jerárquicas sencillas y preparar la base para parsing avanzado mediante `parser_config_jerarquico.py` si es necesario.