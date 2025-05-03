### Módulo: Sensor de Luminosidad TSL2561

Este módulo permite la medición de la intensidad lumínica ambiente mediante el sensor digital TSL2561, comunicándose por bus I2C con el sistema NORA. El objetivo es dotar al sistema de percepción contextual visual (ej. regulación de expresividad en pantalla o LEDs según luz ambiental).

---

#### 1. Descripción funcional del conjunto

El sensor TSL2561 proporciona valores digitales proporcionales a la intensidad de luz recibida, operando en dos canales (infrarrojo y visible) para mejorar la precisión. La comunicación se realiza por bus I2C (líneas SDA y SCL). Este sensor es gestionado por el módulo `sensores/`.

---

#### 2. Componentes principales

**a) TSL2561**

* Sensor de luminosidad digital.
* Alimentación: 3.3 V (conforme con `3V3_Modules`).
* Comunicación: I2C (pines SDA y SCL).
* Dirección I2C seleccionable mediante pin `ADDR_SEL`.
* Salida de interrupción `INT` no utilizada en este esquema.

**b) Líneas de conexión**

* `SDA` y `SCL`: conectadas al bus I2C compartido del sistema.
* `ADDR_SEL`: en estado bajo (GND), define dirección por defecto (0x39).
* `INT`: sin conexión (no se usan interrupciones).

---

#### 3. Observaciones técnicas

* La alimentación a 3.3 V es correcta para este sensor, y compatible con la Raspberry Pi.
* La línea de interrupción `INT` está sin uso; esto es aceptable si se trabaja por sondeo.
* No se observa ninguna resistencia pull-up en las líneas I2C. Esto podría generar fallos de comunicación si no existen en otro punto del bus.

---

#### 4. Recomendaciones

* Confirmar que las líneas `SDA` y `SCL` tienen resistencias pull-up (típicamente 4.7 kΩ) en algún punto del bus. Si no están integradas en el bus central, deben añadirse aquí.
* Etiquetar claramente las conexiones `SDA` y `SCL` para facilitar depuración.
* Si se requiere respuesta más rápida o detección de umbral de luz, se puede considerar el uso de la línea `INT` en futuras revisiones.

---

#### 5. Conclusión

Este módulo está correctamente planteado para la función de detección de luminosidad dentro de NORA. Es compacto y compatible a nivel de tensión y comunicación. Se recomienda únicamente verificar la presencia de resistencias pull-up en el bus I2C general para asegurar fiabilidad en la transmisión de datos.
