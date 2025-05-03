### Módulo: Comunicación NFC – PN532 (I2C)

Este módulo proporciona la capacidad de lectura y escritura de tarjetas o tags NFC mediante el circuito integrado PN532, operando en modo I2C. Permite implementar identificación de usuario, control de acceso o interacciones por proximidad en el sistema NORA, en conjunto con el módulo `sensores/` o `activacion/`.

---

#### 1. Descripción funcional del conjunto

El PN532 es un controlador de comunicaciones NFC que puede trabajar en distintos modos (I2C, SPI, UART). En este diseño se encuentra configurado en modo I2C, con las líneas SDA y SCL conectadas a resistencias de pull-up. Incluye línea de interrupción (`P32_INT0`) y reinicio (`RSTPD_N`) para control desde el microcontrolador principal.

---

#### 2. Componentes principales

**a) PN532 (U4)**

* Controlador NFC compatible con ISO/IEC 14443 A/B, FeliCa, MIFARE.
* Configurado en modo I2C.
* Pines relevantes:

  * `SDA`, `SCL`: líneas I2C con pull-ups de 4.7 kΩ (`R4`, `R5`).
  * `RSTPD_N`: reset activo en bajo, controlado por `R6` (10 kΩ).
  * `P32_INT0`: línea de interrupción NFC.
* Alimentación: 3.3 V desde `3V3_Modules`.

**b) Condensador de desacoplo (C10 – 100 nF)**

* Filtro entre alimentación y tierra, cerca del chip PN532.

**c) Pull-ups para I2C (R4, R5 – 4.7 kΩ)**

* Mantienen las líneas SDA y SCL en nivel alto cuando están inactivas.

**d) R6 – Pull-up en `RSTPD_N` (10 kΩ)**

* Permite mantener el PN532 fuera de estado de reset.

---

#### 3. Observaciones técnicas

* El modo I2C es adecuado para integración simple con Raspberry Pi o microcontroladores.
* Se recomienda confirmar que las líneas `RSTPD_N` y `P32_INT0` están correctamente gestionadas por el software, ya que son claves para reinicio y eventos.
* Las resistencias de pull-up tienen valores estándar correctos.
* Se emplea correctamente alimentación a 3.3 V, conforme a las especificaciones del PN532.

---

#### 4. Recomendaciones

* Asegurar que el microcontrolador lee correctamente `P32_INT0` para detectar eventos NFC sin necesidad de sondeo constante.
* Documentar si se emplean librerías específicas como `Adafruit_PN532` u otras que gestionen el modo I2C.
* Incluir puntos de test en SDA/SCL para facilitar diagnóstico en caso de fallos de comunicación.
* Si se requiere cambiar de modo (SPI/UART), es necesario reconfigurar pines `MODE` (no visibles en este esquema).

---

#### 5. Conclusión

El módulo está correctamente implementado para comunicaciones NFC vía I2C. La disposición de alimentación, filtrado, interrupciones y reinicio es adecuada. Solo se recomienda asegurar la gestión software de `INT` y `RST` para robustez funcional.
