# NORA – Neural Observant Responsive Assistant

**NORA** (Neural Observant Responsive Assistant) es un asistente físico inteligente diseñado como proyecto personal, técnico y académico. Su desarrollo combina visión por computador, reconocimiento y síntesis de voz, control físico mediante servomecanismos, expresión facial digital y una lógica modular orientada a la interacción multimodal y personalizada.

A diferencia de los asistentes virtuales convencionales, NORA tiene **presencia física**. Su diseño incorpora una **cabeza robótica metálica** equipada con cámara, micrófono, altavoz, pantalla facial animada, iluminación emocional y sistemas de movimiento simbólico. El asistente es completamente controlado por el usuario, sin conexión a la nube, y funciona mediante procesamiento local en una **Raspberry Pi**.

## 🎯 Objetivo

El proyecto busca:

- Integrar múltiples tecnologías (IA, visión artificial, voz, robótica, UX, electrónica) en un solo sistema físico autónomo.
- Desarrollar un asistente **transparente, extensible y expresivo**, capaz de comunicarse de forma natural.
- Ofrecer una alternativa más humana y consciente a los asistentes comerciales: sin vigilancia constante, sin dependencia de servicios externos, y con control total por parte del usuario.
- Servir como plataforma de experimentación, aprendizaje y demostración profesional multidisciplinar.

## 🧠 Funcionalidades clave

- Reconocimiento de voz offline (ASR) y síntesis hablada (TTS)
- Detección facial, seguimiento visual, estimación postural
- Pantalla facial animada con expresividad emocional digital
- Iluminación RGB dinámica para señalización de estado
- Movimiento físico básico (asentir, mirar, reaccionar)
- Activación y apagado mediante NFC (presencia consciente)
- Registro local de hábitos, notas y rutinas personales
- Interacción completamente **local y privada**
- Arquitectura **modular y ampliable**

## 📁 Estructura del repositorio
```bash
NORA/
├── docs/                          # Documentación técnica general
│   ├── 00.index_documental.md
│   ├── 01.plan_implementacion_software.md
│   ├── 02.arquitectura_logica.md
│   ├── 03.protocolo_interaccion.md
│   ├── 04.estados_y_emociones.md
│   ├── 05.simulacion_sin_hardware.md
│   ├── 06.documento_eventos.md
│   ├── 07.tests_modulares.md
│   ├── 08.entorno_virtual.md
│   ├── xx.ejecucion.md
│   └── Nora_Introduccion.docx
│
├── software/                      # Código fuente del sistema y archivo principal
│   ├── main.py                   # Punto de entrada del sistema NORA
│   └── src/                      # Módulos funcionales del asistente
│       ├── vision/              # Percepción visual (detección facial, postural)
│       ├── voz/                 # Entrada y salida de voz
│       │   ├── reconocedor.py   # Simulación de reconocimiento de voz (ASR)
│       │   └── sintetizador.py  # Síntesis de texto a voz (TTS)
│       ├── interfaz/            # Control del rostro, LEDs RGB, expresividad
│       ├── control/             # Coordinación de servos, gestos físicos
│       ├── sistema/             # FSM, EventManager y manejadores de eventos
│       │   ├── fsm.py
│       │   ├── event_manager.py
│       │   └── manejadores.py
│       └── datos/               # Base de datos, hábitos, rutinas y perfil
│
├── utils/                         # Scripts de inicialización y herramientas
│   └── estructura_src.py
│
├── software_tests/                         # Scripts de prueba y validación
│   ├── test_event_manager_fsm.py
│
├── config/                        # Archivos de configuración
│   ├── perfiles_usuario/
│   └── parametros_sistema.json
│
├── hardware/                      # Diseño físico y electrónico
│   ├── esquemas/
│   ├── modelos_3d/
│   ├── diseño_mecanico/
│   └── proveedores/
│
├── assets/                        # Recursos gráficos y multimedia
│   ├── imagenes/
│   └── videos/
│
├── README.md                      # Descripción general del proyecto
├── requirements.txt              # Dependencias Python
└── .gitignore                    # Exclusiones para Git
```

## 🛠️ Tecnologías utilizadas

- **Python** como lenguaje principal
- **OpenCV** y **MediaPipe** para visión artificial
- **Vosk**, **Whisper** u otras soluciones ASR locales
- **pyttsx3**, **Google TTS**, o motores TTS personalizados
- **Raspberry Pi 4B** como centro de procesamiento
- **I2C**, **GPIO**, **PWM**, **NFC**, **LED RGB**, **Servos SG90**
- **SQLite** para almacenamiento local de datos

## 📌 Estado actual

> En fase de diseño y documentación técnica.  
> Desarrollo progresivo por bloques: funcionalidades previstas, componentes físicos, arquitectura modular y prototipado funcional.

## 📚 Licencia

Este proyecto se publica con fines formativos y de demostración técnica. La propiedad intelectual del diseño, arquitectura y documentación pertenece al autor.  
Para usos comerciales o difusión externa, contactar previamente.

---
 
**Repositorio activo:** [github.com/AlbertoMarquillas/NORA]
