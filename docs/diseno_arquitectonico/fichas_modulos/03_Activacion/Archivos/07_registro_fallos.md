# Ficha Específica – `registro_fallos.py`

## Nombre del archivo:
`registro_fallos.py`

## Responsabilidad principal:
Registrar de forma estructurada todos los intentos fallidos de activación del sistema NORA, incluyendo su causa, fuente de activación implicada y contexto temporal, para su análisis posterior.

## Entradas esperadas:
- Datos de intentos fallidos (evento rechazado, fuente de activación, timestamp, contexto).

## Salidas generadas:
- Registros persistentes de fallos de activación para auditoría y análisis.

## Funcionalidades principales:
- Creación de registros de cada intento de activación fallido.
- Clasificación del motivo de fallo (fuente no válida, combinación insuficiente, modo no molestar activo, etc.).
- Almacenamiento organizado en archivos locales o base de datos ligera.
- Posibilidad de consulta histórica de fallos registrados.

## Dependencias técnicas:
- `json`, `csv`, `sqlite3` – Almacenamiento de registros.
- `datetime` – Registro de tiempos exactos.
- `os`, `pathlib` – Gestión de rutas y archivos de datos.

