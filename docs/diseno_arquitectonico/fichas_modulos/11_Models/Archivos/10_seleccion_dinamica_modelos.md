# Ficha Funcional – `seleccion_dinamica_modelos.py`

## Nombre del archivo:
`seleccion_dinamica_modelos.py`

## Responsabilidad principal:
Gestionar la selección automática y dinámica del modelo de inteligencia artificial más adecuado para cada tarea en NORA, basándose en el contexto operativo, los recursos disponibles y las condiciones de entrada.

## Entradas esperadas:
- **Tipo de entrada:** Información de contexto (carga de CPU/GPU, tipo de tarea, calidad de entrada, prioridad de respuesta).
- **Fuente:** `vision/`, `voz/`, `dialogo/`, `agentes/`, `supervision_estado.py`.
- **Formato o protocolo:** Datos estructurados de estado y solicitudes de inferencia.

## Salidas generadas:
- **Tipo de salida:** Referencias a modelos seleccionados, logs de decisión de selección.
- **Destinatario:** `models_main.py`, `vision/`, `voz/`, `dialogo/`, `agentes/`.
- **Ejemplo de salida:**
  - Selección de modelo ligero para reconocimiento facial bajo alta carga de CPU
  - Cambio a modelo de alta precisión en condiciones normales

## Módulos relacionados:
- **Entrada desde:** `vision/`, `voz/`, `dialogo/`, `agentes/`, `supervision_estado.py`.
- **Salida hacia:** `models_main.py`, módulos funcionales.
- **Comunicación bidireccional con:** `models_main.py` para actualización de referencias dinámicas.

## Dependencias técnicas:
- **Librerías externas:** `numpy`, `json`, `psutil`.
- **Hardware gestionado:** CPU y GPU (para detección de carga y disponibilidad).
- **Protocolos:** Evaluación dinámica de contexto operativo.

## Notas adicionales:
`seleccion_dinamica_modelos.py` debe implementar políticas de selección configurables (priorizar velocidad, priorizar precisión, balance adaptativo) y ser capaz de cambiar modelos activos en tiempo de ejecución de forma transparente para el resto del sistema. Su implementación permite optimizar el desempeño global y la adaptabilidad de NORA ante condiciones cambiantes.