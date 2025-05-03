### Módulo: Reloj en Tiempo Real – DS1307 con cristal externo

Este módulo proporciona funcionalidad de reloj en tiempo real (RTC) al sistema NORA, permitiendo mantener la hora incluso tras apagones, gracias a la batería de respaldo. La información horaria es gestionada por el módulo `sistema/` mediante interfaz I2C.

---

#### 1. Descripción funcional del conjunto

El chip DS1307 mantiene fecha y hora mediante un cristal de 32.768 kHz y una batería tipo botón CR2032. Se comunica con la Raspberry Pi o microcontrolador principal mediante bus I2C. Opcionalmente, puede generar una señal de salida horaria (`SOUT`) filtrada con un diodo.

---

#### 2. Componentes principales

**a) DS1307 (U1)**

* Reloj en tiempo real con bus I2C (SCL/SDA).
* Alimentación primaria: 5 V.
* Alimentación secundaria: `VBAT` conectada a batería de respaldo.
* Señal `SOUT`: pulso de 1 Hz o señal programada.

**b) Cristal de 32.768 kHz (XTAL-32.768KHZ)**

* Resonador necesario para el temporizador interno del DS1307.
* Conectado entre X1 y X2.

**c) Batería CR2032 (U2)**

* Permite mantener el RTC en funcionamiento en ausencia de alimentación principal.
* Porta-pila tipo KLSS-CR2032-01.

**d) Diodo D3 (1N4148)**

* Bloquea retorno de corriente desde el pin `SOUT`, protegiendo el RTC o el sistema.

**e) Resistencias de pull-up (R1, R2)**

* 4.7 kΩ conectadas a `SCL` y `SDA`.
* Establecen niveles lógicos adecuados para la comunicación I2C.

**f) Condensador de desacoplo (C2 – 100 nF)**

* Entre VCC y GND para estabilidad de alimentación del chip.

---

#### 3. Observaciones técnicas

* El uso del DS1307 es adecuado para RTC básico.
* El cristal tiene valor y disposición correctos.
* La inclusión de pull-ups en el módulo evita dependencia de otros puntos del bus.
* `SOUT` puede ser útil como fuente de pulso periódico si se emplea con una interrupción externa.
* Alimentación y respaldo están correctamente integradas.

---

#### 4. Recomendaciones

* Asegurar correcta orientación del diodo D3 si se usa `RTC_SOUT`.
* Verificar si el firmware hace uso de `SOUT`. Si no, considerar dejarlo no conectado.
* Documentar la configuración horaria por defecto al encendido (si se inicializa desde software).
* Confirmar que el controlador principal puede tolerar niveles I2C a 5 V o usar adaptadores de nivel si trabaja a 3.3 V.

---

#### 5. Conclusión

El diseño del módulo RTC es completo y adecuado para mantener la hora en el sistema NORA. La combinación de respaldo por batería, filtrado, cristal y pull-ups locales garantiza estabilidad y autonomía. Se recomienda revisar la integración de `SOUT` si se desea aprovechar esa señal.
