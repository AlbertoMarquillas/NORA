# Ficha Funcional – `seguimiento_habitos.py`

## Nombre del archivo:
`seguimiento_habitos.py`

## Responsabilidad principal:
Gestionar el almacenamiento y análisis de hábitos de uso y patrones de interacción del usuario dentro del sistema NORA. Este archivo se encarga de registrar y realizar un seguimiento de las actividades del usuario, como rutinas diarias, hábitos de comportamiento o preferencias de interacción, para ayudar a personalizar la experiencia de NORA y proporcionar recomendaciones para mejorar el bienestar y la eficiencia.

## Entradas esperadas:
- **Tipo de entrada:** Datos sobre hábitos, registros de actividades del usuario, cambios en las rutinas.
- **Fuente:** `voz/` (para recibir comandos de creación o actualización de hábitos), `dialogo/` (para registrar hábitos relacionados con la interacción), `sistema/` (para obtener datos contextuales de las actividades del usuario).
- **Formato o protocolo:** Texto plano, datos estructurados en formato JSON, eventos internos (`CMD_...`, `EVT_...`).

## Salidas generadas:
- **Tipo de salida:** Confirmación de hábito guardado, análisis de hábitos, estadísticas de uso, recomendaciones.
- **Destinatario:** `dialogo/`, `sistema/`, `agentes/` (para integrar los hábitos registrados y realizar acciones relacionadas).
- **Ejemplo de salida:**
  - `EVT_HABIT_SAVED` (Evento que indica que un hábito ha sido guardado exitosamente).
  - `EVT_HABIT_ANALYZED` (Evento que indica que el análisis de los hábitos ha sido completado).
  - Recomendaciones para mejorar los hábitos, como "Podrías intentar seguir este hábito durante 30 minutos al día".

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir instrucciones del usuario sobre hábitos), `dialogo/` (para registrar información relevante sobre el comportamiento del usuario), `sistema/` (para obtener datos contextuales sobre las actividades del usuario).
- **Salida hacia:** `dialogo/`, `sistema/`, `agentes/` (para proporcionar recomendaciones basadas en los hábitos analizados).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para integrar los hábitos con el flujo general de NORA y generar recomendaciones personalizadas.

## Dependencias técnicas:
- **Librerías externas:** `sqlite3`, `SQLAlchemy` (para persistencia de datos de hábitos y actividades), `json` (para la serialización de los hábitos), `pandas` (para análisis de datos y generación de estadísticas).
- **Hardware gestionado:** Almacenamiento local (SSD/HDD) para persistencia de hábitos y registros.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos de hábitos, eventos internos para coordinar las recomendaciones.

## Notas adicionales:
Este archivo es clave para permitir que NORA se convierta en un asistente más proactivo y útil, ayudando al usuario a mejorar su bienestar o su eficiencia mediante el seguimiento y análisis de sus hábitos. Además, la capacidad de realizar recomendaciones personalizadas basadas en estos hábitos puede mejorar la experiencia de NORA, creando interacciones más relevantes y enfocadas en el usuario. **`seguimiento_habitos.py`** también permite que NORA detecte patrones y sugiera modificaciones en las rutinas para fomentar un comportamiento positivo o más saludable.

## Archivos previstos del módulo:
- `seguimiento_habitos.py`: Almacenamiento y análisis de hábitos de uso y patrones de interacción (este archivo).
- Archivos adicionales como `datos_main.py`, `gestion_rutinas.py`, `analisis_habitos.py`.
