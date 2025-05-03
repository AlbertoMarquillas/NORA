### Módulo: Servomotores PWM (expresividad física)

Este módulo proporciona la conexión eléctrica y el desacoplo adecuado para el control de dos servomotores SG90/MG90 a través de señales PWM. Se utilizan en NORA para control de expresión facial, orientación u otras acciones físicas animadas.

---

#### 1. Descripción funcional del conjunto

Cada servomotor se alimenta con 5 V y se controla mediante una señal PWM (`PWM_Servo1`, `PWM_Servo2`). Se han implementado filtros y diodos de protección por cada unidad para estabilizar el funcionamiento y proteger contra picos de corriente inversa.

---

#### 2. Componentes principales por cada servomotor

**a) Servomotor (SG90 o MG90)**

* Alimentación: 5 V.
* Control: señal PWM típica de 50 Hz.
* Consumo nominal: 100–250 mA (picos hasta 500 mA bajo carga).

**b) Diodo Schottky (D2, D5 – 1N5819)**

* Conectado en antiparalelo desde 5 V hacia GND.
* Función: protección contra inversión o retorno de corriente inducida por motor.
* El 1N5819 es adecuado por su baja caída de tensión y rápida respuesta.

**c) Condensadores electrolíticos (C4, C6 – 1000 µF)**

* Filtrado de baja frecuencia.
* Amortiguan caídas de tensión al inicio del movimiento o bajo carga súbita.

**d) Condensadores cerámicos (C3, C5 – 100 nF)**

* Filtrado de alta frecuencia para supresión de picos transitorios.

---

#### 3. Observaciones técnicas

* El uso de 1000 µF por servomotor es adecuado si se alimentan desde una fuente de baja impedancia como el LRS-35-5.
* La combinación de condensador electrolítico + cerámico mejora la estabilidad ante perturbaciones.
* Los diodos Schottky son apropiados y su orientación es correcta.
* El diseño está claramente separado por canal, permitiendo futuras ampliaciones o control individual.

---

#### 4. Recomendaciones

* Verificar que las masas (`GND_Modules`) estén correctamente conectadas con la tierra lógica del controlador PWM para evitar referencias flotantes.
* Si se amplía a más de 2 servos o se requiere uso concurrente con carga alta, considerar un bus de alimentación dedicado con regulación específica para servos.
* Añadir TVS o fusible PTC si se busca mayor robustez frente a cortocircuitos o bloqueo mecánico del servo.

---

#### 5. Conclusión

El módulo está bien diseñado para operar con seguridad y estabilidad dos servomotores en el sistema NORA. La protección contra picos, el desacoplo energético y la separación de señales son apropiados. Es recomendable mantener una buena gestión térmica y asegurar una masa común con el controlador para evitar comportamientos erráticos.
