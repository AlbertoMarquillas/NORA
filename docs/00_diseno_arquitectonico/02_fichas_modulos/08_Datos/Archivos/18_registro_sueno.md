# Ficha Funcional – `registro_sueno.py`

## Nombre del archivo:
`registro_sueno.py`

## Responsabilidad principal:
Gestionar el registro de los patrones de sueño detectados o introducidos manualmente por el usuario dentro del sistema NORA. Este archivo se encarga de almacenar y analizar los datos relacionados con las horas de sueño del usuario, ofreciendo la posibilidad de registrar y consultar patrones de sueño, así como realizar recomendaciones basadas en esos datos.

## Entradas esperadas:
- **Tipo de entrada:** Datos de sueño (horas de descanso, duración, calidad del sueño), entradas manuales del usuario.
- **Fuente:** `voz/` (para recibir información de sueño proporcionada por el usuario), `sistema/` (para registrar patrones de sueño basados en sensores u otros dispositivos).
- **Formato o protocolo:** Datos estructurados en formato JSON, texto plano, eventos internos (`CMD_...`, `EVT_...`).

## Salidas generadas:
- **Tipo de salida:** Datos de sueño registrados, patrones de sueño recuperados, recomendaciones basadas en el análisis de sueño.
- **Destinatario:** `sistema/`, `dialogo/`, `agentes/` (para utilizar los datos de sueño en el contexto de la conversación o para hacer recomendaciones).
- **Ejemplo de salida:**
  - `EVT_SLEEP_DATA_SAVED` (Evento que indica que los datos de sueño han sido guardados correctamente).
  - `EVT_SLEEP_PATTERN_RETRIEVED` (Evento que indica que el patrón de sueño ha sido recuperado exitosamente).
  - Recomendaciones basadas en el sueño, como "Estás durmiendo menos de lo recomendado. Intenta dormir más de 7 horas al día."

## Módulos relacionados:
- **Entrada desde:** `voz/` (para recibir comandos o datos manuales sobre el sueño), `sistema/` (para integrar sensores o dispositivos relacionados con el monitoreo del sueño).
- **Salida hacia:** `sistema/`, `agentes/`, `dialogo/` (para compartir los datos de sueño y las recomendaciones generadas).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que los datos de sueño sean utilizados correctamente en el contexto de la interacción.

## Dependencias técnicas:
- **Librerías externas:** `sqlite3`, `SQLAlchemy` (para persistencia de datos de sueño en bases de datos locales), `json` (para almacenar y recuperar los datos de sueño).
- **Hardware gestionado:** Sensores de monitoreo de sueño (si están disponibles) y almacenamiento local (SSD/HDD) para persistencia de los datos.
- **Protocolos:** SQL, JSON para almacenar y recuperar datos estructurados de los patrones de sueño.

## Notas adicionales:
Este archivo es crucial para permitir que NORA registre y analice los patrones de sueño del usuario, lo que puede ser utilizado para ofrecer recomendaciones personalizadas y mejorar el bienestar general del usuario. Al integrar el registro del sueño con otras interacciones del sistema, NORA puede ayudar a los usuarios a establecer hábitos de sueño más saludables y proporcionar información valiosa sobre la calidad de su descanso.

## Archivos previstos del módulo:
- `registro_sueno.py`: Monitoreo y registro de patrones de sueño detectados o introducidos manualmente (este archivo).
- Archivos adicionales como `datos_main.py`, `seguimiento_habitos.py`, `analisis_habitos.py`.
