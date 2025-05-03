# Acciones realizadas – Estado: Procesando

Durante el estado **Procesando**, NORA ejecuta una secuencia de acciones destinadas a interpretar la entrada recibida y producir una respuesta coherente. Este estado puede involucrar operaciones de tipo semántico, inferencial, afectivo o contextual, en función del tipo de entrada y del módulo activo.

---

## 1. Evaluación del contenido de entrada

- Análisis semántico y sintáctico del texto recibido (`dialogo/` → `NLU`)
- Clasificación de intención, extracción de entidades y detección de contexto conversacional
- En casos visuales o gestuales, inferencia directa mediante modelos (`models/`) o reglas definidas en agentes (`/agentes/`)

---

## 2. Consulta de contexto y perfil

- Acceso al módulo `datos/` para recuperar historial, rutinas, agenda o configuraciones del usuario
- Evaluación del estado emocional del sistema o del usuario si está disponible (`agentes/`)
- Aplicación de reglas de contexto (hora, localización, estado del sistema, etc.)

---

## 3. Planificación de la respuesta

- Selección de la acción a ejecutar: respuesta hablada, gesto, cambio de interfaz, activación de periférico, etc.
- Generación de la respuesta estructurada (`CMD_ACTUAR` o `CMD_RESPONDER`)
- Decisión de canal de salida: `voz/`, `interfaz/`, `control/`

---

## 4. Registro y trazabilidad

- Emisión de `EVT_PROCESS_COMPLETED`
- Registro de entrada, resultado de análisis y respuesta generada en el módulo `datos/` (si aplica)
- Actualización del contexto conversacional (estado del diálogo activo, stack de turnos)

---

## 5. Estado visual y señalización

- Expresión facial o animación que indique procesamiento (ej. icono de carga o movimiento de ojos)
- LEDs RGB pueden pulsar suavemente (ej. blanco tenue) indicando actividad cognitiva

---

## Indicadores activos del sistema

| Componente        | Estado durante Procesando                    |
|-------------------|-----------------------------------------------|
| voz/              | TTS bloqueado temporalmente (espera de respuesta) |
| dialogo/          | Activo: generación y comprensión textual      |
| datos/            | Lectura y/o escritura según contexto          |
| modelos/          | Activación si hay inferencia o clasificación  |
| interfaz/         | Muestra animación de espera o actividad       |
