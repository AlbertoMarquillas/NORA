# Ficha Funcional – `config_datos.py`

## Nombre del archivo:
`config_datos.py`

## Responsabilidad principal:
Gestionar la configuración de las rutas de las bases de datos, las opciones de persistencia de datos y los backups automáticos dentro del sistema NORA. Este archivo se encarga de definir las configuraciones para el almacenamiento de datos, la frecuencia de los backups, las políticas de conservación de datos y las opciones de optimización de la base de datos. Garantiza que los datos se gestionen de manera eficiente y segura a lo largo del tiempo.

## Entradas esperadas:
- **Tipo de entrada:** Configuraciones de rutas de base de datos, opciones de persistencia, configuraciones de backups y optimización de base de datos.
- **Fuente:** `sistema/` (para recibir configuraciones globales sobre almacenamiento), `datos/` (para definir rutas y políticas de persistencia).
- **Formato o protocolo:** Archivos de configuración JSON, eventos internos de configuración (`CMD_...`, `EVT_...`).

## Salidas generadas:
- **Tipo de salida:** Confirmaciones de configuraciones aplicadas, eventos de actualización de configuración, informes de estado.
- **Destinatario:** `sistema/`, `datos/` (para aplicar las configuraciones de almacenamiento y optimización).
- **Ejemplo de salida:**
  - `EVT_CONFIG_UPDATED` (Evento que indica que las configuraciones de almacenamiento o backup han sido actualizadas).
  - `CMD_APPLY_DB_CONFIG` (Instrucción para aplicar las configuraciones de base de datos).
  - `AGT_BACKUP_CONFIGURED` (Confirmación de que las opciones de backup han sido correctamente configuradas).

## Módulos relacionados:
- **Entrada desde:** `sistema/` (para recibir configuraciones generales), `datos/` (para establecer configuraciones de base de datos y persistencia).
- **Salida hacia:** `sistema/`, `datos/` (para aplicar las configuraciones de persistencia y optimización de la base de datos).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar las configuraciones de datos con el flujo general del sistema.

## Dependencias técnicas:
- **Librerías externas:** `json` (para leer y escribir configuraciones de almacenamiento), `sqlite3`, `SQLAlchemy` (para definir y gestionar rutas de base de datos locales).
- **Hardware gestionado:** Almacenamiento local (SSD/HDD) o almacenamiento en la nube para persistencia de datos.
- **Protocolos:** SQL, JSON para gestionar las rutas de la base de datos y las opciones de backup.

## Notas adicionales:
Este archivo es fundamental para garantizar que NORA maneje eficientemente el almacenamiento de datos y los backups, permitiendo que el sistema se mantenga optimizado y que los datos del usuario estén siempre disponibles y seguros. Además, **`config_datos.py`** permite configurar las rutas de base de datos y las políticas de backup de forma flexible, adaptándose a las necesidades del sistema y de los usuarios. Esto asegura que la persistencia de los datos sea fiable, y que en caso de fallo, los datos puedan ser restaurados sin pérdidas.

## Archivos previstos del módulo:
- `config_datos.py`: Configuración de rutas de bases de datos, opciones de persistencia, backups automáticos (este archivo).
- Archivos adicionales como `datos_main.py`, `respaldo_datos.py`, `optimizacion_queries.py`.
