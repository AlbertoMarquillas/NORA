### Módulo: Botón físico de activación (Pull-down)

Este módulo representa un botón físico conectado a una entrada digital del sistema NORA, utilizado como uno de los mecanismos de activación local. Es una forma directa, sencilla y robusta de interacción humana con el sistema.

---

#### 1. Descripción funcional del conjunto

Cuando el usuario presiona el botón, la línea `Btn` se pone a nivel alto (3.3 V). En reposo (sin presionar), el nodo `Btn` es forzado a nivel bajo mediante una resistencia pull-down de 10 kΩ.

Este botón puede ser interpretado como un evento `EVT_BTN_PRESSED` dentro del sistema y procesado por el módulo `activacion/`.

---

#### 2. Componentes principales

**a) Botón normalmente abierto (NA)**

* Conectado entre Vcc (3.3 V) y la línea de señal `Btn`.
* Presionado: cierra el circuito y pone `Btn` en 3.3 V.

**b) R1-PD\_BTN – Resistencia de pull-down (10 kΩ)**

* Conectada entre `Btn` y GND.
* Garantiza que la línea esté en 0 V cuando el botón no está siendo pulsado.

---

#### 3. Observaciones técnicas

* El uso de una resistencia de 10 kΩ es estándar para este tipo de configuraciones y proporciona un equilibrio entre consumo y velocidad de respuesta.
* La lógica es activa en alto (HIGH activa), lo cual es común pero debe estar correctamente gestionado a nivel de software para evitar rebotes.
* La señal `Btn` se conecta presumiblemente a un pin GPIO digital, que deberá estar configurado con interrupción o lectura periódica.

---

#### 4. Recomendaciones

* Añadir un condensador de desacoplo de \~100 nF entre `Btn` y GND para filtrar rebotes mecánicos si no se implementa un debounce por software.
* Incluir una etiqueta clara en la PCB para mantenimiento e identificación.
* Si se desea mayor robustez frente a ruido electromagnético, se puede implementar una red RC pasiva (ej. 10 kΩ y 100 nF) o filtrar digitalmente.

---

#### 5. Conclusión

El módulo está correctamente diseñado y sigue buenas prácticas para detección digital de entradas mediante botón. Se recomienda implementar debounce (por hardware o so
