### Módulo: Captura de Audio – Micrófono Electret con Amplificador y ADC

Este módulo permite la captura de audio analógico a través de un micrófono electret, su acondicionamiento mediante un amplificador específico y posterior digitalización con un ADC SPI. Es parte del subsistema auditivo de NORA, gestionado por el módulo `voz/`.

---

#### 1. Descripción funcional del conjunto

El audio es captado por un micrófono electret y enviado a un amplificador de audio (MAX9814) con ganancia programable. La salida amplificada se filtra y se dirige a un conversor ADC de 10 bits (MCP3008), que transforma la señal en digital para su procesamiento posterior.

---

#### 2. Componentes principales

**a) Micrófono electret (POM-5046P-C3310-R)**

* Micrófono pasivo con salida analógica.
* Conectado a GND y al pin MIC\_INPUT del amplificador.

**b) Amplificador MAX9814ETD+**

* Alimentación: 5 V.
* Entrada MICIN (pin 8) conectada al micrófono.
* Salida MICOOUT (pin 7) va al ADC.
* Pines auxiliares:

  * `MICBIAS`: proporciona polarización al micrófono.
  * `GAIN`, `A/R`: control de ganancia y ataque/release.
* Desacoplo local con C1 (100 nF) y filtrado de entrada con C1/C2 (1 µF).
* Pull-down en la salida (100 kΩ) para estabilizar nivel de reposo.

**c) MCP3008 – ADC SPI de 10 bits**

* Alimentación: 5 V.
* Canal 0 (CH0) recibe señal analógica desde el MAX9814.
* Bus SPI:

  * `CLK`, `CS/SHDN`, `DIN`, `DOUT` conectados al controlador.
  * `R1` (1.8 kΩ) y `R2` (3.3 kΩ) forman un divisor en `MISO` para adaptar nivel a 3.3 V.

---

#### 3. Observaciones técnicas

* El uso del MAX9814 es muy apropiado para micrófonos electret por su integración de ganancia automática (AGC).
* El filtrado de entrada y desacoplo son correctos y ajustados a recomendaciones de datasheet.
* El divisor resistivo en la línea MISO SPI es válido para adaptar señal a dispositivos de 3.3 V.
* La línea `MICBIAS` no está conectada explícitamente, lo que podría afectar la polarización si el micrófono requiere alimentación activa. Se recomienda confirmar la necesidad según el modelo exacto.

---

#### 4. Recomendaciones

* Verificar si el micrófono necesita polarización desde `MICBIAS`; si es así, conectar ese pin a través de una resistencia (ej. 2.2 kΩ).
* Considerar un filtro pasabanda (hardware o software) si se desea reducir ruido fuera del rango vocal.
* Documentar valores de GAIN, A/R en diseño final si se fijan con resistencias o puenteos.
* Añadir etiquetas para facilitar el trazado de señales `MIC_ANALOG` y `SPI_MICROPHONE`.

---

#### 5. Conclusión

El diseño de este módulo es robusto y bien planteado para captación de audio en sistemas embebidos. Incorpora amplificación, filtrado, conversión y adaptación de niveles adecuadamente. La única revisión necesaria es confirmar la gestión de `MICBIAS` en relación al micrófono utilizado.
