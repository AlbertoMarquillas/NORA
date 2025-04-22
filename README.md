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

/docs/                        → Documentación técnica general
│   ├── Nora_Introduccion.docx     ← Documento principal (introducción, motivación, objetivos)
│   ├── funcionalidades.md         ← Detalle de funcionalidades previstas
│   ├── componentes_fisicos.md     ← Descripción completa de hardware
│   ├── arquitectura_sistema.md    ← Diseño de arquitectura hardware/software
│   └── anexos/                    ← Diagramas, tablas, referencias, etc.

/src/                         → Código fuente del sistema (Python)
│   ├── vision/                   ← Módulo de cámara y análisis de imagen
│   ├── voz/                      ← Reconocimiento de voz y TTS
│   ├── interfaz/                 ← Gestión de pantalla facial, LEDs y expresividad
│   ├── control/                  ← Coordinación de servos, movimientos simbólicos
│   ├── sistema/                  ← Activación NFC, lógica de estado, inicialización
│   └── datos/                    ← Base de datos local, gestión de hábitos y rutinas

/hardware/                   → Componentes físicos y diseño
│   ├── esquemas/                ← Esquemas electrónicos y conexiones GPIO
│   ├── modelos_3d/              ← Piezas en STL o CAD para impresión 3D
│   ├── diseño_mecanico/         ← Bocetos, mediciones, planos estructurales
│   └── proveedores/             ← Referencias de componentes y enlaces de compra

/assets/                     → Recursos visuales y gráficos
│   ├── imagenes/                ← Fotos del prototipo, renders, bocetos
│   └── videos/                  ← Demos de funcionamiento o animaciones

/tests/                      → Scripts de prueba y validación de módulos
│   ├── test_vision.py
│   ├── test_voz.py
│   ├── test_leds.py
│   └── test_nfc.py

/config/                     → Archivos de configuración y calibración
│   ├── perfiles_usuario/        ← Perfiles y rutinas personalizadas
│   └── parametros_sistema.json  ← Configuraciones iniciales y ajustes de sistema

README.md                   → Descripción general del proyecto (GitHub)
requirements.txt            → Librerías Python necesarias
.gitignore                  → Archivos y carpetas excluidos del control de versiones

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
 
**Repositorio activo:** [github.com/tuusuario/NORA]
