# Descripción funcional – Estado: Procesando

El estado **Procesando** representa la fase en la que NORA analiza una entrada previamente recibida —ya sea de tipo verbal, visual o gestual— con el objetivo de generar una respuesta coherente, adecuada al contexto y alineada con el modelo de interacción activo.

Este estado es transitorio y computacionalmente intensivo. Su duración depende de la complejidad de la entrada, del modelo utilizado (`models/`) y de la acción requerida (respuesta verbal, gesto físico, actualización de perfil, etc.).

Durante **Procesando**, NORA:

- Ejecuta tareas de interpretación semántica, clasificación, inferencia o análisis estadístico sobre la entrada.
- Consulta módulos internos (`datos/`, `agentes/`) para enriquecer el contexto y adecuar la respuesta.
- Genera una respuesta estructurada que se traducirá en acciones concretas a través de los módulos `voz/`, `interfaz/` o `control/`.

**Importancia del estado:**

El estado **Procesando** es el núcleo cognitivo temporal de NORA. Garantiza que toda entrada significativa recibida se transforma en una acción racional o expresiva, reforzando la sensación de coherencia e inteligencia del sistema.
