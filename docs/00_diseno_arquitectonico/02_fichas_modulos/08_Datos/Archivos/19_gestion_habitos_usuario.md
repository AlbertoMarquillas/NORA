# Ficha Funcional – `gestion_habitos_usuario.py`

## Nombre del archivo:
`gestion_habitos_usuario.py`

## Responsabilidad principal:
Gestionar las rutinas y hábitos diarios del usuario dentro de NORA, incluyendo el seguimiento y control de hábitos de uso, metas y tareas diarias. Este archivo se encarga de permitir que el usuario defina, registre y supervise sus hábitos diarios o metas a largo plazo, proporcionando feedback sobre el progreso y ofreciendo recomendaciones de mejora si es necesario.

## Entradas esperadas:
- **Tipo de entrada:** Comandos de creación o actualización de hábitos, datos de progreso de hábitos, solicitudes de seguimiento de hábitos.
- **Fuente:** `voz/` (para recibir comandos sobre hábitos y metas del usuario), `dialogo/` (para interactuar con las rutinas y metas), `sistema/` (para proporcionar información sobre el estado de los hábitos).
- **Formato o protocolo:** Texto plano, estructuras JSON para registrar hábitos, eventos internos (`CMD_...`, `EVT_...`).

## Salidas generadas:
- **Tipo de salida:** Confirmación de hábito guardado, estadísticas de progreso, recomendaciones de mejora de hábitos.
- **Destinatario:** `dialogo/`, `sistema/`, `agentes/` (para gestionar el progreso de los hábitos y hacer recomendaciones basadas en el seguimiento).
- **Ejemplo de salida:**
  - `EVT_HABIT_SAVED` (Evento que indica que un hábito ha sido guardado correctamente).
  - `EVT_HABIT_PROGRESS` (Evento que muestra el progreso de un hábito).
  - Recomendaciones sobre hábitos como "Intenta hacer ejercicio todos los días para mejorar tu salud."

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir instrucciones de hábitos o metas del usuario), `dialogo/` (para registrar la interacción y la creación de nuevos hábitos).
- **Salida hacia:** `dialogo/`, `sistema/`, `agentes/` (para proporcionar estadísticas de hábitos y recomendaciones personalizadas).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para coordinar el seguimiento de hábitos y asegurar que los datos de los hábitos sean coherentes en todo el sistema.

## Dependencias técnicas:
- **Librerías externas:** `sqlite3`, `SQLAlchemy` (para almacenamiento persistente de hábitos y progreso), `json` (para la serialización de los hábitos), `pandas` (para el análisis y seguimiento de hábitos).
- **Hardware gestionado:** Almacenamiento local (SSD/HDD) para persistencia de los datos de hábitos y rutinas.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos estructurados de los hábitos, comunicación interna para realizar seguimiento y análisis de progreso.

## Notas adicionales:
Este archivo es clave para permitir que NORA ayude al usuario a gestionar y mejorar sus hábitos. Al registrar y analizar el progreso de las rutinas diarias o metas del usuario, NORA puede ofrecer recomendaciones personalizadas para mejorar la productividad, salud o bienestar del usuario. También proporciona una visión detallada de los hábitos y su evolución a lo largo del tiempo, permitiendo que el sistema se ajuste a las necesidades del usuario en función de sus metas.

## Archivos previstos del módulo:
- `gestion_habitos_usuario.py`: Gestión avanzada de listas de hábitos y rutinas diarias con seguimiento de cumplimiento (este archivo).
- Archivos adicionales como `seguimiento_habitos.py`, `analisis_habitos.py`, `memoria_conversacional.py`.
