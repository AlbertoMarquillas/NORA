# Ficha Funcional – `autoafinado_modelos.py`

## Nombre del archivo:
`autoafinado_modelos.py`

## Responsabilidad principal:
Realizar el ajuste automático de hiperparámetros y el reentrenamiento ligero de modelos de IA en NORA basándose en datos recientes del usuario o del entorno. Optimiza el desempeño del sistema sin necesidad de intervención manual constante.

## Entradas esperadas:
- **Tipo de entrada:** Datos de entrenamiento incremental, métricas de desempeño actuales, configuraciones de optimización.
- **Fuente:** `datos/`, `gestion_fine_tuning.py`, `agentes/`.
- **Formato o protocolo:** Tensores de datos, parámetros de ajuste, estructuras de evaluación.

## Salidas generadas:
- **Tipo de salida:** Modelos autoafinados, reportes de mejora de desempeño, actualizaciones de hiperparámetros.
- **Destinatario:** `models_main.py`, `datos/`, `agentes/`.
- **Ejemplo de salida:**
  - Modelo de predicción de hábitos reentrenado con datos de la última semana
  - Ajuste automático de learning rate en modelo de emociones vocales

## Módulos relacionados:
- **Entrada desde:** `datos/`, `gestion_fine_tuning.py`, `agentes/`.
- **Salida hacia:** `models_main.py`, `datos/`, `agentes/`.
- **Comunicación bidireccional con:** `models_main.py` para gestión de nuevos modelos generados.

## Dependencias técnicas:
- **Librerías externas:** `TensorFlow`, `PyTorch`, `scikit-learn`, `numpy`, `optuna` (opcional para optimización avanzada).
- **Hardware gestionado:** GPU opcional para reentrenamiento eficiente.
- **Protocolos:** Protocolo de entrenamiento incremental controlado.

## Notas adicionales:
`autoafinado_modelos.py` debe balancear el beneficio de la actualización contra el riesgo de sobreajuste, utilizando estrategias como validación cruzada, early stopping y comparación con desempeño histórico antes de reemplazar un modelo existente. Su implementación permite que NORA se adapte de forma continua y autónoma al comportamiento y contexto cambiantes del usuario.

