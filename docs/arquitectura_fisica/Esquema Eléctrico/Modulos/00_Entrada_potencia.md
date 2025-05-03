### Módulo: Entrada y Distribución de Potencia (230V AC → 5V/3.3V DC)

Este módulo constituye la etapa primaria de alimentación del sistema NORA. Su función principal es transformar la tensión alterna de red (230 V AC) en tensiones continuas estables de 5 V y 3.3 V para el suministro de la Raspberry Pi y los periféricos conectados.

---

#### 1. Descripción funcional del conjunto

El bloque realiza tres funciones clave:

1. **Recepción de red eléctrica** mediante conector IEC 13 (tipo Schuko).
2. **Conmutación y protección** a través del módulo IEC 14.
3. **Conversión AC-DC** mediante fuente conmutada industrial (LRS-35-5).
4. **Regulación secundaria** a 3.3 V mediante LDO AMS1117-3.3.
5. **Distribución de voltaje** organizada a través del bloque POWER\_DISTR.

---

#### 2. Componentes principales

**a) IEC 13 (SCHUKO)**

* Entrada estándar de corriente alterna 230 V AC.
* Pines: Línea (L), Neutro (N) y Tierra (PE).

**b) IEC 14**

* Módulo de control conmutado, presumiblemente incluye interruptor, fusible y control remoto de encendido (`SWITCH_CTRL`).
* Aísla la red interna del sistema y facilita diagnósticos mediante `FUSE_STATUS`.

**c) Fuente LRS-35-5 (Mean Well)**

* Conversor AC-DC industrial de 230 V AC a 5 V DC (7 A máximo, 35 W).
* Proporciona potencia limpia y estable a todo el sistema.

**d) Regulador de tensión AMS1117-3.3 (U5)**

* Convierte 5 V a 3.3 V estabilizados.
* Acompañado de condensadores de filtrado:

  * **C11**: 10 µF entrada.
  * **C12**: 10 µF salida.
  * **C13**: 100 nF desacoplo.

**e) Bloque POWER\_DISTR**

* Distribuye las salidas de 5 V, 3.3 V y GND a los módulos:

  * `5V_RPI4` y `5V_Modules`
  * `3V3_RPI4` y `3V3_Modules`
  * `GND_RPI4` y `GND_Modules`

---

#### 3. Observaciones técnicas

* La elección del LRS-35-5 es adecuada por su robustez, bajo ruido y regulación precisa, ideal para alimentar una Raspberry Pi y múltiples sensores.
* El regulador AMS1117-3.3 permite obtener 3.3 V de forma local sin depender de la Raspberry Pi, útil si se busca aislar cargas sensibles o evitar sobrecarga del regulador interno de la Pi.
* El uso de un bloque de distribución (`POWER_DISTR`) mejora el orden y facilita futuras expansiones del sistema.

---

#### 4. Recomendaciones

* Confirmar que el disipador del LRS-35-5 tenga ventilación pasiva suficiente (≥ 20 mm libre por encima).
* Asegurar que el AMS1117 no disipe más de 0.5 W para evitar calentamiento excesivo (I < 200 mA recomendable).
* Incluir protección secundaria contra sobretensiones o picos transitorios si se expone a red inestable.
* Etiquetar externamente las salidas del bloque de distribución para mantenimiento.

---

#### 5. Posibles errores o mejoras detectadas

**1. Falta de fusible visible en la entrada IEC 13:**
Aunque el módulo IEC 14 parece tener `FUSE_STATUS`, no se representa de forma explícita un fusible físico en la entrada. Se recomienda añadir un fusible apropiado (ej. 250 V, 1–2 A) en la línea activa (`AC_L_IN`).

**2. Ausencia de condensador cerámico en la entrada de U5:**
Además del electrolítico de 10 µF (C11), se recomienda añadir un condensador cerámico de 100 nF en paralelo para mejorar la estabilidad del regulador AMS1117.

**3. Riesgo de sobrecalentamiento del AMS1117:**
Si se extraen corrientes superiores a 200 mA a 3.3 V, puede superar los límites térmicos sin disipador. Alternativamente, se sugiere sustituirlo por un step-down eficiente (como MP1584 o similar).

**4. POWER\_DISTR sin fusibles individuales:**
Se recomienda proteger las salidas individuales con fusibles PTC o resistencias limitadoras para evitar que un cortocircuito en un módulo afecte a toda la rama.

**5. GND del LRS-35-5 no representado claramente:**
La salida `GND` debe estar conectada inequívocamente a la masa común del sistema (`GND_RPI4`, `GND_Modules`). Aunque probablemente esté conectado, debe reflejarse con claridad en el esquema.

---

#### 6. Conclusión

Este módulo está correctamente planteado para las necesidades energéticas del sistema NORA. Su diseño combina seguridad (conmutación + tierra), fiabilidad (fuente conmutada certificada), y flexibilidad (regulación adicional y distribución separada), cumpliendo los criterios de un sistema embebido robusto. Las mejoras propuestas refuerzan la seguridad eléctrica y la fiabilidad a largo plazo.
