# Ficha Funcional – `historial_eventos.py`

## Nombre del archivo:
`historial_eventos.py`

## Responsabilidad principal:
Registrar y almacenar los eventos de activación, interacción y comportamiento dentro del sistema NORA. Este archivo se encarga de mantener un historial detallado de todas las interacciones del sistema, permitiendo hacer un seguimiento de las acciones realizadas, los eventos importantes que ocurrieron durante la conversación y cualquier otra actividad relevante. Esto proporciona un registro completo para auditoría, análisis o ajustes futuros.

## Entradas esperadas:
- **Tipo de entrada:** Eventos de activación, interacciones del usuario, cambios en el sistema, datos contextuales.
- **Fuente:** `voz/` (para registrar interacciones vocales), `dialogo/` (para registrar el flujo de la conversación), `sistema/` (para registrar cambios en el estado del sistema).
- **Formato o protocolo:** Eventos internos (`EVT_...`), datos en formato JSON, texto plano, parámetros estructurados.

## Salidas generadas:
- **Tipo de salida:** Registro de eventos, confirmaciones de almacenamiento, consultas históricas.
- **Destinatario:** `sistema/`, `dialogo/`, `agentes/` (para consultar eventos pasados y tomar decisiones basadas en ellos).
- **Ejemplo de salida:**
  - `EVT_EVENT_LOGGED` (Evento que indica que un evento ha sido registrado correctamente en el historial).
  - `CMD_QUERY_EVENT_HISTORY` (Instrucción para consultar el historial de eventos de NORA).
  - `AGT_EVENT_HISTORY_RETRIEVED` (Confirmación de que el historial de eventos ha sido recuperado correctamente).

## Módulos relacionados:
- **Entrada desde:** `voz/`, `dialogo/`, `sistema/`, `agentes/` (para registrar cualquier evento relevante de interacción o del sistema).
- **Salida hacia:** `sistema/`, `dialogo/`, `agentes/` (para permitir el acceso a los registros de eventos y utilizar esa información en el sistema).
- **Comunicación bidireccional con:** `sistema/`, `agentes/` para asegurar que el historial de eventos esté disponible para decisiones futuras o para la optimización de la interacción.

## Dependencias técnicas:
- **Librerías externas:** `sqlite3`, `SQLAlchemy` (para la persistencia de eventos en bases de datos locales), `json` (para la serialización de eventos).
- **Hardware gestionado:** Almacenamiento local USB (SSD/HDD) para persistencia de datos de eventos.
- **Protocolos:** SQL, JSON para almacenar y recuperar registros estructurados de eventos.

## Notas adicionales:
Este archivo es clave para ofrecer trazabilidad y visibilidad completa sobre las interacciones dentro del sistema. El registro detallado de eventos es útil no solo para el análisis de comportamiento e interacciones, sino también para la mejora continua del sistema, permitiendo revisar qué ocurrió en interacciones pasadas, cómo se manejaron y cómo pueden optimizarse en el futuro. Además, el historial de eventos permite que NORA ajuste sus respuestas en función de lo que ya ha ocurrido durante la conversación.

## Archivos previstos del módulo:
- `historial_eventos.py`: Registro de eventos de activación, interacción y comportamiento (este archivo).
- Archivos adicionales como `datos_main.py`, `gestion_rutinas.py`, `memoria_conversacional.py`.
