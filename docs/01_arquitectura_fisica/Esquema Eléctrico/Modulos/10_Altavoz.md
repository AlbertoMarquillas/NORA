### Módulo: Reproducción de Sonido – Altavoz con Transistor de Conmutación

Este módulo permite la generación de sonido mediante un altavoz de baja impedancia controlado por una señal PWM. Se emplea un transistor NPN (2N2222) como interruptor para manejar la corriente necesaria del altavoz, activado desde el sistema NORA mediante una señal `PWM_AUDIO` generada por el módulo `voz/`.

---

#### 1. Descripción funcional del conjunto

Una señal PWM es enviada a la base de un transistor que conmuta la corriente del altavoz. El sistema actúa como un convertidor digital-analógico rudimentario para generar sonidos, tonos o voz sintetizada.

---

#### 2. Componentes principales

**a) Q2 – Transistor NPN 2N2222**

* Actúa como interruptor controlado por `PWM_AUDIO`.
* El pin base está polarizado con una resistencia de 1 kΩ (`R-BASE-SPKR`).

**b) LS1 – Altavoz**

* Recibe corriente a través del colector del transistor.
* Alimentación: 5 V compartida (`5V_Modules`).
* Impedancia típica: 8 Ω (debe confirmarse en la implementación final).

**c) D4 – Diodo de protección (1N5819)**

* Protege contra corriente inversa inducida por la bobina del altavoz (flyback).
* Tipo Schottky, baja caída de tensión, respuesta rápida.

**d) C-FILTRO-SPKR – Condensador de 100 nF**

* Filtra picos de alta frecuencia para proteger el transistor.
* Mejora la integridad de señal y reduce EMI.

**e) R-BASE-SPKR – Resistencia de base (1 kΩ)**

* Limita corriente hacia la base de Q2 para evitar saturación excesiva o daños.

---

#### 3. Observaciones técnicas

* El transistor 2N2222 puede manejar hasta 600 mA, adecuado para pequeños altavoces.
* La resistencia de base es adecuada para niveles lógicos de 3.3 V o 5 V.
* El diodo Schottky está correctamente orientado y protege al transistor durante apagado rápido.
* El filtrado capacitivo es limitado pero útil en esta configuración básica.

---

#### 4. Recomendaciones

* Si el altavoz es de 8 Ω y se alimenta a 5 V, la corriente esperada puede ser de hasta 600 mA. Confirmar que Q2 tiene disipación térmica adecuada.
* Si se desea mejorar la calidad de audio, considerar el uso de un filtro pasabajo y un amplificador clase D dedicado.
* Añadir resistencia de carga (pull-down) en el nodo del colector si se producen zumbidos en reposo.

---

#### 5. Conclusión

El módulo permite la activación eficiente de un altavoz mediante control PWM. El diseño es funcional para generar tonos o señales simples, con protección y filtrado básico. Para salida de audio más compleja o calidad vocal, se recomienda rediseñar usando un DAC y etapa de audio dedicada.
