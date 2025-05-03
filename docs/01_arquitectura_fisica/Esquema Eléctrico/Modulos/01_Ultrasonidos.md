### Módulo: Sensor de Ultrasonidos HC-SR04

Este módulo se encarga de medir distancias mediante el sensor ultrasónico HC-SR04, que emite pulsos de ultrasonido y mide el tiempo de retorno del eco. Forma parte del subsistema de percepción física del entorno de NORA, siendo utilizado principalmente para la detección de presencia o proximidad.

---

#### 1. Descripción funcional del conjunto

El HC-SR04 opera mediante un pin de activación (TRIG) y un pin de recepción (ECHO). Este módulo envía un pulso de 10 µs por TRIG y mide el tiempo hasta recibir el eco en ECHO.

En este diseño:

* Se alimenta desde la rama `5V_Modules` del sistema de potencia general.
* Usa un condensador de desacoplo local para mejorar la estabilidad.
* Se adapta el nivel de señal de salida ECHO mediante un divisor resistivo para proteger la entrada digital.

---

#### 2. Componentes principales

**a) U6 – HC-SR04**

* Sensor ultrasónico estándar de 4 pines: GND, TRIG, ECHO, VCC.
* Alimentación: 5 V.
* Rango: típicamente 2 cm a 4 m.

**b) CAP\_ULTRA**

* Condensador de 100 nF entre VCC y GND del sensor.
* Función: desacoplo de alta frecuencia para evitar errores por ruido en alimentación.

**c) Divisor de tensión en ECHO (R8 y R9)**

* Ambas resistencias son de 10 kΩ.
* Reducción de 5 V a ≈2.5 V. Si se desea llevar ECHO a un pin de 3.3 V seguro, esta división es excesiva. Una mejor opción sería R8 = 20 kΩ y R9 = 10 kΩ para obtener ≈3.3 V.

**d) Resistencia de protección en línea al pin TRIG (R7)**

* 10 kΩ.
* Limita corriente de entrada al sensor en caso de error de configuración del pin.

---

#### 3. Observaciones técnicas

* El uso del condensador de 100 nF es correcto y recomendable.
* La resistencia de 10 kΩ en TRIG es una práctica aceptable como protección pasiva.
* El divisor resistivo para ECHO es funcional, pero su voltaje de salida queda por debajo del umbral lógico para entradas de 3.3 V (2.5 V típicos vs. mínimo lógico \~2 V en muchos microcontroladores). Puede funcionar, pero no es ideal.

---

#### 4. Recomendaciones

* **Ajustar el divisor de tensión en ECHO** si el pin de entrada es de 3.3 V:

  * Usar R8 = 20 kΩ y R9 = 10 kΩ para obtener ≈3.3 V.
  * O utilizar un **clamp con diodo zener de 3.3 V** si se quiere mayor robustez.
* Si se conecta a un microcontrolador tolerante a 5 V (como algunos Arduinos), el divisor actual puede omitirse.
* Incluir un encabezado o conector para facilitar pruebas o desconexión del sensor.

---

#### 5. Conclusión

El módulo de ultrasonidos está correctamente diseñado para una integración segura y funcional con el sistema NORA. Se recomienda ajustar el divisor resistivo para maximizar la compatibilidad lógica si se trabaja con entradas de 3.3 V, como las de la Raspberry Pi. El resto del diseño es limpio, funcional y suficientemente desacoplado.
