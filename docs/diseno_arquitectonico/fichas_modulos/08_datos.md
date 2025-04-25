# Ficha Funcional – Módulo de Datos

## Nombre del módulo:
`datos/`

## Responsabilidad principal:
Gestiona el almacenamiento local persistente de toda la información relevante para NORA: notas del usuario, rutinas, historial de interacciones, perfiles, configuraciones y registros de eventos. Permite acceso estructurado y seguro a datos dinámicos o históricos.

## Entradas esperadas:
- Tipo de entrada: comandos de almacenamiento o recuperación, nuevos datos estructurados
- Fuente: `voz/`, `dialogo/`, `sistema/`, `agentes/`
- Formato o protocolo: texto plano, estructuras JSON, eventos internos (`CMD_...`, `EVT_...`)

## Salidas generadas:
- Tipo de salida: datos solicitados, confirmaciones de guardado, eventos de recuperación
- Destinatario: `dialogo/`, `sistema/`, `agentes/`
- Ejemplo de salida:
  - `EVT_DATA_RETRIEVED`
  - `EVT_NOTE_SAVED`
  - Datos de rutina recuperados para activación de recordatorios

## Módulos relacionados:
- Entrada desde: `voz/`, `dialogo/`, `sistema/`, `agentes/`
- Salida hacia: `voz/`, `dialogo/`, `sistema/`, `agentes/`
- Comunicación bidireccional con: todos los módulos que requieren persistencia o consulta de datos

## Dependencias técnicas:
- Librerías externas: `sqlite3`, `dataset`, `SQLAlchemy`, `json`, `datetime`
- Hardware gestionado: almacenamiento local USB (SSD/HDD)
- Protocolos: SQL, JSON

## Notas adicionales:
Permite registrar rutinas, notas, eventos ambientales, perfiles de usuario y hábitos de comportamiento. Además, almacena de forma periódica datos provenientes de todos los sensores del sistema (temperatura, humedad, luminosidad, calidad del aire, presencia física, estado de movimiento) y permite construir un historial detallado de condiciones ambientales y actividades del usuario.

El sistema también gestiona la creación de historias personalizadas basadas en interacciones pasadas, registro de horas de sueño, y permite al usuario definir listas de hábitos que pueden ser seguidas y analizadas, con posibilidad de mejora progresiva mediante módulos de inteligencia artificial.

El diseño considera integridad transaccional, expansión dinámica de la base de datos, protección de la privacidad, capacidad de aprendizaje de patrones de comportamiento y soporte para optimizar futuras conversaciones e interacciones basadas en datos históricos.

## Archivos previstos del módulo:
Listado de archivos `.py` que se espera implementar dentro del directorio `datos/` para estructurar sus funcionalidades.

- `datos_main.py`: Coordinador principal de operaciones de almacenamiento y recuperación.
- `gestion_notas.py`: Almacenamiento y consulta de notas dictadas o creadas.
- `gestion_rutinas.py`: Administración de rutinas y recordatorios personalizados.
- `historial_eventos.py`: Registro de eventos de activación, interacción y comportamiento.
- `gestion_perfiles.py`: Gestión de perfiles de usuario y configuraciones personalizadas.
- `seguimiento_habitos.py`: Almacenamiento y análisis de hábitos de uso y patrones de interacción.
- `agenda_calendario.py`: Administración de citas, recordatorios temporales y eventos de calendario.
- `listas_dinamicas.py`: Gestión de listas de tareas, compras o ideas generadas por el usuario.
- `anotaciones_emocionales.py`: Registro de emociones detectadas asociadas a momentos de interacción.
- `respaldo_datos.py`: Sistema de backup y recuperación segura de la base de datos.
- `optimizacion_queries.py`: Módulo para mejorar el rendimiento de consultas y operaciones sobre la base de datos.
- `gestion_versiones.py`: Versionado automático de entradas para rollback seguro.
- `analisis_habitos.py`: Generación de estadísticas e informes de uso, comportamiento y emociones.
- `gestion_privacidad.py`: Control dinámico de privacidad y retención de datos sensibles.
- `migracion_datos.py`: Exportación e importación segura de bases de datos o perfiles de usuario.
- `busqueda_semantica.py`: Búsqueda inteligente y contextualizada de información almacenada.
- `registro_sensorial.py`: Almacenamiento periódico de datos provenientes de sensores ambientales y físicos.
- `gestion_historial_usuario.py`: Creación y actualización de historias personalizadas del usuario.
- `registro_sueno.py`: Monitoreo y registro de patrones de sueño detectados o introducidos manualmente.
- `gestion_habitos_usuario.py`: Gestión avanzada de listas de hábitos y rutinas diarias con seguimiento de cumplimiento.
- `mejora_habitos_ia.py`: Análisis y recomendación automática de mejoras de hábitos mediante algoritmos de IA ligera.
- `config_datos.py`: Configuración de rutas de bases de datos, opciones de persistencia, backups automáticos.
- `utils_datos.py`: Funciones auxiliares de acceso, validación de integridad y conversión de datos.