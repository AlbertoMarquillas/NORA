## 📁 Documentación de Arquitectura – Proyecto NORA

Este directorio contiene una descripción detallada de cada archivo fuente del sistema NORA. Cada documento explica el propósito, funcionalidades, dependencias y relación con el resto del sistema de uno de los módulos clave.

---

### Índice de módulos documentados

| Nº  | Archivo              | Descripción resumida                                  |
|-----|----------------------|--------------------------------------------------------|
| 01  | `01_main.md`         | Lanzador principal del sistema (`main.py`)            |
| 02  | `02_sistema.md`      | Núcleo de coordinación global (`sistema.py`)          |
| 03  | `03_interfaz.md`     | Representación visual del estado (`interfaz.py`)      |
| 04  | `04_sintetizador.md` | Salida de voz con TTS (`sintetizador.py`)             |
| 05  | `05_reconocedor.md`  | Simulación de entrada de voz (`reconocedor.py`)       |
| 06  | `06_event_manager.md`| Bus de eventos desacoplado (`event_manager.py`)       |
| 07  | `07_fsm.md`          | Máquina de estados del sistema (`fsm.py`)             |
| 08  | `08_manejadores.md`  | Lógica externa de reacción a eventos (`manejadores.py`)|

---

Todos los módulos están diseñados con un enfoque modular, escalable y desacoplado, siguiendo principios de arquitectura reactiva basada en eventos.

Esta documentación es útil para desarrolladores que deseen entender, mantener o extender el sistema.

---

**Ubicación:** `docs/arquitectura/`

