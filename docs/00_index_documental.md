## 00. Índice Documental del Proyecto NORA

Este archivo actúa como índice maestro para la documentación técnica del asistente físico inteligente **NORA**. Recoge los documentos clave organizados por orden lógico y numeración, proporcionando una visión estructurada del sistema.

Cada entrada incluye una breve descripción de su contenido y propósito. Todos los documentos están alojados en la carpeta `/docs/` del repositorio.

---

### Índice de Procedimientos

**01.** `01.plan_implementacion_software.md`  
> Descripción completa de la estrategia de desarrollo software-first, fases por bloque funcional, herramientas necesarias y beneficios del enfoque modular inicial.

**02.** `02.arquitectura_logica.md`  
> Especificación de los módulos de `/src/`, su propósito, entradas/salidas y principios de diseño desacoplado mediante eventos.

**03.** `03.protocolo_interaccion.md`  
> Definición del ciclo de interacción humano-asistente, eventos reconocidos, flujos de comunicación y coordinación multimodal.

**04.** `04.estados_y_emociones.md`  
> Catálogo de estados operativos y emociones simuladas en NORA, con lógica de transición y su representación visual/lumínica/sonora.

**05.** `05.simulacion_sin_hardware.md`  
> Guía completa para ejecutar y validar el sistema sin necesidad de hardware físico, incluyendo mocks, GUI y scripts de prueba.

**06.** `06.documento_eventos.md`  
> Especificación del bus de eventos internos: formato, categorías, prioridades y mecanismo de distribución asincrónica.

**07.** `07.tests_modulares.md`  
> Plan de pruebas por módulo con estructura de `/tests/`, entradas esperadas, salidas observables y criterios de validación técnica.

---

### Notas
- Este índice se actualizará con nuevos documentos conforme se desarrollen otras capas del sistema (hardware, flujos de producción, interfaz final).
- Todos los documentos siguen un formato técnico-formal, con orientaciones directas a implementación, pruebas y mantenimiento.

---

**Documentación elaborada como parte del desarrollo progresivo de NORA.**

> Versión inicial: Abril 2025  
> Mantenedor: Alberto Marquillas