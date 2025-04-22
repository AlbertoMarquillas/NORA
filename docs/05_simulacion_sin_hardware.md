## 05. Simulación del Sistema NORA sin Hardware Físico

### Propósito del documento

Este documento detalla cómo ejecutar y probar el sistema NORA en un entorno de desarrollo sin requerir hardware físico real (Raspberry Pi, servos, LEDs, sensores). Permite simular la lógica, interacción y comportamiento multimodal de NORA en una estación de trabajo estándar.

---

### Objetivos de la simulación

- Verificar la lógica de estados y emociones
- Probar la interacción por voz y visión artificial
- Visualizar la salida facial y lumínica mediante GUI
- Simular la activación por NFC o evento físico
- Ejecutar pruebas de comportamiento sin montaje físico

---

### Requisitos del entorno

- **Sistema operativo:** Windows, Linux o macOS
- **Python:** versión 3.10 o superior
- **Dependencias:**
  - `opencv-python`
  - `mediapipe`
  - `pyttsx3`
  - `vosk` o `whisper` (según elección)
  - `tkinter` o `pygame` (GUI facial)
  - `sqlite3`
  - `keyboard` o similar para eventos simulados

---

### Simulación de componentes físicos

#### GPIO y PWM
- Reemplazo por clases `MockGPIO`, `MockPWM`
- Interfaz con funciones `set_pin_state()`, `simulate_servo()`
- Logs por consola para visualizar acciones físicas

#### LEDs RGB
- Representación gráfica en ventana (círculo o barra de color)
- Cambios de color basados en eventos de estado o emoción

#### Servomotores
- Texto animado o representación con flechas/cabeza virtual
- Logs: "Servo A: Inclinación +15°", "Servo B: posición centro"

#### NFC
- Simulación por pulsación de tecla (`F2` para activar, `F3` para desactivar)
- Evento interno: `EVT_NFC_ACTIVATE`, `EVT_NFC_DEACTIVATE`

#### Pantalla facial
- Ventana con rostro animado (ojos, boca, cejas)
- Cambios de expresión ligados al sistema de emociones

---

### Pruebas disponibles en entorno simulado

- **test_voz.py:** comando hablado → texto → respuesta por voz + animación facial
- **test_vision.py:** detección de rostro → reacción visual + expresión
- **test_leds.py:** eventos internos → cambio de color visual
- **test_nfc.py:** pulsación de tecla → encendido y apagado lógico
- **test_dialogo.py:** conversación guiada → seguimiento FSM y voz

---

### Recomendaciones para desarrollo sin hardware

- Utilizar logs enriquecidos con timestamp y nivel (INFO, EVENT, WARN)
- Crear scripts de prueba por módulo con escenarios básicos
- Documentar cada evento interno generado (en consola o archivo)
- Controlar tiempo y secuencia de ejecución con `asyncio` o `threading`
- Añadir opción `--simulacion` al ejecutar el sistema para usar mocks

---

### Ejemplo de ejecución

```bash
$ python main.py --simulacion
[NORA] Iniciado en modo simulación.
[NFC] Activación simulada recibida.
[ESTADO] Transición: REPOSO → PASIVO
[INTERFAZ] Luz: azul tenue | Rostro: atención suave
[VOZ] Usuario: "recuérdame beber agua"
[ASR] Interpretado: "recuérdame beber agua"
[ESTADO] ESCUCHA → ACTIVO → PASIVO
```

---

### Conclusión

La simulación sin hardware permite avanzar en el desarrollo de NORA, depurar su lógica y validar su comportamiento expresivo antes de disponer del prototipo físico. Este entorno es compatible con pruebas automatizadas y favorece la iteración ágil en las primeras fases del proyecto.