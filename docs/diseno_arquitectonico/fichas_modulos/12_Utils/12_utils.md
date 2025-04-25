# Ficha Funcional – Módulo de Utilidades

## Nombre del módulo:
`utils/`

## Responsabilidad principal:
Proporcionar funciones auxiliares, parsers de configuración, herramientas de logging estructurado, cálculos matemáticos y geométricos, generación y gestión de eventos, y otras utilidades compartidas entre todos los módulos del sistema NORA.

## Entradas esperadas:
- Tipo de entrada: peticiones de servicios auxiliares (parsing, conversión, cálculos, logging)
- Fuente: todos los módulos funcionales
- Formato o protocolo: estructuras de datos estándar, texto plano, parámetros numéricos

## Salidas generadas:
- Tipo de salida: resultados de operaciones auxiliares, eventos estructurados, registros de logs
- Destinatario: módulos funcionales que requieran soporte transversal
- Ejemplo de salida:
  - Evento emitido con estructura estándar
  - Parsing de archivos JSON de configuración
  - Cálculo de distancia entre dos puntos o normalización de vectores

## Módulos relacionados:
- Entrada desde: todos los módulos (`sistema/`, `voz/`, `vision/`, `interfaz/`, `control/`, etc.)
- Salida hacia: todos los módulos que requieran funciones comunes
- Comunicación bidireccional con: no aplica directamente (módulo pasivo)

## Dependencias técnicas:
- Librerías externas: `json`, `yaml`, `logging`, `math`, `datetime`, `os`, `random`, `numpy`
- Hardware gestionado: ninguno
- Protocolos: uso interno de funciones estándar

## Notas adicionales:
El módulo `utils/` centraliza todas las herramientas comunes para evitar duplicación de código en el sistema. Incluye parsers de configuración, validadores, generadores de eventos, funciones matemáticas y de temporización, loggers estructurados y utilidades de conversión o formateo de datos.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `utils/` para estructurar sus funcionalidades.

- `utils_main.py`: Coordinador principal de utilidades disponibles.
- `parser_config.py`: Lectura y validación de archivos de configuración (`.json`, `.yaml`, `.ini`).
- `parser_config_jerarquico.py`: Parsing avanzado de configuraciones anidadas con validación de esquemas.
- `gestion_eventos.py`: Creación y emisión de eventos internos estructurados.
- `eventos_asincronos.py`: Emisión y gestión de eventos en modo asincrónico (`asyncio`).
- `logger_sistema.py`: Inicialización y gestión de logging estructurado para todo el sistema.
- `logger_distribuido.py`: Logging distribuido por módulo con control de niveles y salida diferenciada.
- `cálculos_matemáticos.py`: Funciones matemáticas, geométricas y estadísticas básicas.
- `gestion_tiempos.py`: Temporización, medición de intervalos y gestión de retardos cooperativos.
- `validadores.py`: Funciones para validar estructuras de datos, parámetros de entrada y configuraciones.
- `conversion_formatos.py`: Conversión de unidades, formatos de fecha/hora, codificación segura de datos.
- `gestion_random.py`: Funciones para generación controlada de números aleatorios o elecciones estocásticas.
- `normalizacion_vectores.py`: Funciones específicas para normalización de vectores, escalado y operaciones sobre arrays.
- `generador_ids_unicos.py`: Generación segura de identificadores únicos para eventos, sesiones o recursos.
- `gestion_secretos.py`: Almacenamiento y recuperación segura de credenciales y datos sensibles.

