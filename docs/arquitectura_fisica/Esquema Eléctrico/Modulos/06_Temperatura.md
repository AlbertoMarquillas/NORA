### Módulo: Sensor de Temperatura MCP9902T

Este módulo permite la lectura digital de temperatura mediante el sensor MCP9902T-AE/RW, conectado por bus I2C al sistema NORA. Su objetivo es proporcionar información térmica local y remota para el módulo `sensores/`, que puede ser usada para adaptar comportamiento, activar ventilación o registrar condiciones ambientales.

---

#### 1. Descripción funcional del conjunto

El MCP9902T es un sensor térmico digital con dos canales: uno interno y uno externo, que pueden conectarse a diodos térmicos. Se comunica vía I2C (SMCLK/SMDATA) y permite la configuración de alertas mediante pines dedicados.

---

#### 2. Componentes principales

**a) MCP9902T-AE/RW**

* Sensor digital de temperatura con interfaz I2C.
* Alimentación: 3.3 V.
* Canales de temperatura:

  * **Interno** (integrado).
  * **Externo** (DP1/DN1), aquí sin conexión.
* Dirección I2C definida por `THERM/ADDR` (pin 4).
* Señal de alerta opcional en pin 6 (`ALERT/THERM2`).

**b) Condensador de desacoplo (C-DESACOPLO\_TEMP)**

* 100 nF entre VDD y GND.
* Filtro local para estabilidad de alimentación.

**c) Líneas de comunicación I2C**

* `SMCLK` (SCL), `SMDATA` (SDA): líneas del bus I2C.
* No se observan resistencias pull-up locales (ver recomendaciones).

---

#### 3. Observaciones técnicas

* La alimentación a 3.3 V es correcta y compatible con el dispositivo.
* El condensador de desacoplo está bien ubicado.
* El sensor está siendo usado únicamente con su canal interno, lo cual es válido.
* El pin `THERM/ADDR` parece estar conectado a GND, lo que configura la dirección I2C en su valor por defecto (0x18).
* El pin `ALERT/THERM2` no está conectado; aceptable si no se usan alertas de hardware.

---

#### 4. Recomendaciones

* Verificar la presencia de resistencias pull-up en SDA y SCL en el bus general. Si no existen, añadir 4.7 kΩ a 3.3 V.
* Documentar explícitamente la dirección I2C seleccionada (ej. 0x18 si `ADDR` a GND).
* Dejar test points o pads para posibles futuras conexiones a DP1/DN1 si se desea usar el canal externo.
* Añadir silkscreen o documentación indicando el uso exclusivo del canal interno, para evitar confusiones.

---

#### 5. Conclusión

Este módulo está correctamente implementado para monitorizar temperatura interna con el sensor MCP9902T. La conexión I2C, alimentación y desacoplo son adecuados. Se recomienda validar que el bus I2C disponga de pull-ups y documentar claramente la configuración de dirección y uso interno del sensor.
