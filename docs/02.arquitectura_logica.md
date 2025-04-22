## 02. Arquitectura Lógica del Software de NORA

### Propósito del documento

Este documento describe la arquitectura lógica del software que conforma el sistema operativo de NORA. Se detallan los módulos funcionales principales, sus responsabilidades, interfaces internas, relaciones entre componentes y principios de diseño modular adoptados.

El objetivo es proporcionar una visión clara y estructurada de cómo se organiza el código fuente dentro de la carpeta `/src/`, estableciendo una referencia técnica para el desarrollo, depuración, extensión y mantenimiento del sistema.

---

### Estructura general de carpetas

```
/src/
|-- vision/        -> Módulo de percepción visual (detección facial, postural, atención)
|-- voz/           -> Reconocimiento de voz offline y síntesis hablada (ASR + TTS)
|-- interfaz/      -> Control del rostro animado, iluminación RGB y expresividad
|-- control/       -> Coordinación de servos y movimientos simbólicos
|-- sistema/       -> Lógica central, estados internos, activación NFC, transiciones
|-- datos/         -> Gestor de base de datos, perfil de usuario, rutinas, eventos
```

Cada carpeta representa un **módulo funcional independiente**, organizado en torno a una responsabilidad concreta. Los módulos están diseñados para comunicarse entre sí mediante un sistema de eventos o mensajes locales.

---

### Descripción de módulos

#### 1. `vision/`
- **Responsabilidades:** detección y seguimiento facial, estimación de postura, percepción de presencia, análisis de expresiones.
- **Entradas:** flujo de imagen desde webcam.
- **Salidas:** coordenadas de rostro, atención estimada, alerta postural.
- **Tecnologías:** OpenCV, MediaPipe, threading o procesamiento asincrónico.

#### 2. `voz/`
- **Responsabilidades:** conversión de voz a texto (ASR) y generación de voz desde texto (TTS).
- **Entradas:** flujo de audio desde micrófono.
- **Salidas:** texto interpretado, audio sintetizado.
- **Tecnologías:** Vosk/Whisper, pyttsx3, control FSM para diálogos.

#### 3. `interfaz/`
- **Responsabilidades:** visualización de emociones, gestión de rostro animado, control de iluminación simbólica.
- **Entradas:** comandos de estado y emociones.
- **Salidas:** cambios visuales en GUI (o pantalla física), color de LEDs virtuales o reales.
- **Tecnologías:** Tkinter / PyGame / PyQt + drivers para LEDs (virtuales en desarrollo).

#### 4. `control/`
- **Responsabilidades:** ejecución de gestos físicos (cabeceo, orientación), control de servos.
- **Entradas:** eventos internos de atención o expresión.
- **Salidas:** órdenes a GPIOs simuladas o reales.
- **Tecnologías:** mock de GPIO, planificación por estado.

#### 5. `sistema/`
- **Responsabilidades:** definición de estados globales, gestión de activación NFC, inicialización y apagado.
- **Entradas:** eventos de sistema, entrada NFC, inactividad prolongada.
- **Salidas:** transiciones de modo, comandos a otros módulos.
- **Tecnologías:** máquina de estados global, EventManager.

#### 6. `datos/`
- **Responsabilidades:** almacenamiento estructurado de notas, rutinas, eventos y perfil del usuario.
- **Entradas:** comandos internos, interacciones habladas.
- **Salidas:** respuestas personalizadas, datos de contexto.
- **Tecnologías:** SQLite3, acceso directo o ORM simple.

---

### Principios de diseño modular

- **Separación de responsabilidades:** cada módulo debe encargarse de una tarea concreta y tener una interfaz clara.
- **Desacoplamiento funcional:** los módulos no se llaman entre sí directamente; se comunican por eventos.
- **Escalabilidad:** cada carpeta admite nuevos submódulos o extensiones sin afectar la estructura general.
- **Testabilidad:** todos los módulos incluyen pruebas individuales en `/tests/` que validan su comportamiento aislado.

---

### Flujo de ejecución general (resumen)

1. **Encendido:** el sistema se activa por NFC o evento manual.
2. **Inicialización:** se cargan los estados, perfiles y configuraciones.
3. **Bucle principal:** los módulos vision, voz e interfaz quedan en escucha o espera de eventos.
4. **Eventos:** al detectar presencia, voz o acción programada, se generan eventos internos.
5. **Reacción coordinada:** el sistema emite respuestas multimodales en función del contexto.
6. **Reposo:** tras inactividad o petición explícita, el sistema se apaga ordenadamente.