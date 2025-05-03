# Ficha Funcional – `datos_main.py`

## Nombre del archivo:
`datos_main.py`

## Responsabilidad principal:
Orquestar las operaciones principales de almacenamiento y recuperación de datos dentro del sistema NORA. Este archivo se encarga de gestionar el acceso y la persistencia de toda la información relevante, como las notas del usuario, rutinas, historial de interacciones, perfiles, configuraciones y registros de eventos. Asegura que los datos sean almacenados de manera eficiente y se puedan recuperar rápidamente cuando sea necesario.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de almacenamiento o recuperación de datos, nuevas estructuras de datos.
- **Fuente:** `voz/`, `dialogo/`, `sistema/`, `agentes/` (para recibir datos de interacción y configuraciones).
- **Formato o protocolo:** Texto plano, estructuras JSON, eventos internos (`CMD_...`, `EVT_...`).

## Salidas generadas:
- **Tipo de salida:** Confirmaciones de guardado, datos solicitados, eventos de recuperación.
- **Destinatario:** `dialogo/`, `sistema/`, `agentes/` (para compartir la información almacenada y gestionada).
- **Ejemplo de salida:**
  - `EVT_DATA_RETRIEVED` (Evento que indica que los datos han sido recuperados correctamente).
  - `EVT_NOTE_SAVED` (Evento que indica que una nota ha sido guardada exitosamente).
  - Datos de rutina recuperados para la activación de recordatorios.

## Módulos relacionados:
- **Entrada desde:** `voz/`, `dialogo/`, `sistema/`, `agentes/` (para almacenar y recuperar información relevante para cada módulo).
- **Salida hacia:** `voz/`, `dialogo/`, `sistema/`, `agentes/` (para proporcionar datos almacenados o recuperados).
- **Comunicación bidireccional con:** Todos los módulos que requieren persistencia o consulta de datos para realizar sus operaciones.

## Dependencias técnicas:
- **Librerías externas:** `sqlite3`, `dataset`, `SQLAlchemy`, `json`, `datetime` (para el manejo de bases de datos y almacenamiento estructurado).
- **Hardware gestionado:** Almacenamiento local USB (SSD/HDD) para persistencia de datos.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos estructurados.

## Notas adicionales:
Este archivo es crucial para garantizar que NORA pueda acceder y almacenar datos de manera eficiente, desde las interacciones pasadas hasta las configuraciones de usuario y eventos contextuales. **`datos_main.py`** también proporciona la funcionalidad para gestionar el historial de interacciones, las rutinas y los perfiles de usuario, asegurando que NORA ofrezca una experiencia personalizada y coherente. Además, este archivo maneja la persistencia de datos relacionados con sensores ambientales y el comportamiento del usuario, lo que permite crear historias personalizadas y mejorar las interacciones futuras basadas en datos históricos.

## Archivos previstos del módulo:
- `datos_main.py`: Coordinador principal de operaciones de almacenamiento y recuperación (este archivo).
- Archivos adicionales como `gestion_notas.py`, `gestion_rutinas.py`, `historial_eventos.py`.
