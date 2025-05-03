# Pruebas de Contacto – Validación de Interacción Física

Este documento establece las pruebas necesarias para validar el funcionamiento del subsistema de interacción física en NORA, asegurando la detección fiable de eventos y la ejecución coherente de respuestas.

---

## 1. Objetivo

Verificar que los sensores físicos (IMU, presión, vibración) responden adecuadamente a estímulos estructurales y que el sistema interpreta correctamente los eventos derivados.

---

## 2. Pruebas sugeridas

### 2.1 Golpe controlado

* **Acción:** Golpear suavemente una zona específica de la carcasa
* **Resultado esperado:** `EVT_PHYSICAL_IMPACT`, expresión visual o sonora, registro

### 2.2 Inclinación sostenida

* **Acción:** Inclinar lateralmente el cuerpo de NORA durante más de 5 segundos
* **Resultado esperado:** `EVT_PHYSICAL_TILT_STABLE`, mensaje verbal o gesto visual

### 2.3 Agitación leve

* **Acción:** Sacudir levemente el sistema desde su base
* **Resultado esperado:** Detección de aceleración anómala, registro sin respuesta si modo silencioso activo

### 2.4 Recentrado automático

* **Acción:** Rotar el sistema sobre su eje horizontal
* **Resultado esperado:** `EVT_PHYSICAL_ROTATION` + respuesta motriz o facial compensatoria

---

## 3. Validación técnica

* Revisar `logs/eventos_fisicos.log` para confirmar registros
* Supervisar `estado/fsm.py` para verificar generación y propagación de eventos
* Evaluar latencia entre detección y respuesta (< 300 ms deseable)

---

## 4. Herramientas complementarias

* GUI de depuración con visualización de datos de IMU
* Osciloscopio lógico para verificar señales I²C o SPI si hay problemas
* Modo de diagnóstico con trazado extendido (`modo_debug = true`)

---

Estas pruebas aseguran que el sistema físico de interacción cumple criterios de sensibilidad, robustez y expresividad, integrándose sin conflictos con el resto de subsistemas funcionales.
