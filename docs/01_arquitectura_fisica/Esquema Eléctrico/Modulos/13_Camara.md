## 14. Módulo de Cámara

### 14.1. Descripción General

El módulo de cámara constituye el subsistema de visión de NORA. Está basado en un sensor digital IMX219 conectado directamente a la Raspberry Pi 4 mediante la interfaz CSI (Camera Serial Interface). Este módulo permite la adquisición de vídeo en tiempo real, siendo utilizado por el subsistema `vision/` para tareas de percepción visual, análisis postural, reconocimiento facial y seguimiento del entorno.

### 14.2. Especificaciones Técnicas

* **Sensor:** Sony IMX219
* **Resolución:** 8 MP (3280×2464)
* **Vídeo:** Hasta 1080p @30 fps o 720p @60 fps
* **Interfaz:** MIPI CSI-2 (conector FFC de 15 pines)
* **Alimentación:** 3.3 V/1.8 V suministrada internamente por la RPi4
* **Conexión:** Mediante cable plano directamente al conector CSI de la Raspberry Pi
* **Compatibilidad:** Total con `libcamera`, `OpenCV`, `GStreamer`

### 14.3. Conexión Física

El módulo se conecta al conector CSI de la Raspberry Pi 4, situado junto al puerto HDMI más cercano al USB-C. No se representa en el esquema de Proteus debido a que:

* No requiere conexión externa de alimentación.
* El bus CSI es un canal digital diferencial de alta velocidad que no forma parte del sistema GPIO.
* Proteus no modela buses CSI ni la interacción con módulos de imagen.

### 14.4. Recomendaciones de Montaje

* Instalar la cámara en un soporte fijo y orientada hacia el usuario.
* Usar buena iluminación ambiental o LEDs difusos si se requiere compensar condiciones de luz.
* Evitar contraluces directos o reflejos en la lente.

### 14.5. Configuración por Software

* Control mediante `libcamera-vid` o `libcamera-still` en RPi OS moderno:

  ```bash
  libcamera-vid -t 0 --width 1280 --height 720 --framerate 30
  ```
* Alternativamente, capturar con OpenCV:

  ```python
  import cv2
  cap = cv2.VideoCapture(0)
  ret, frame = cap.read()
  ```

### 14.6. Funcionalidad en NORA

La cámara se gestiona desde el módulo `vision/`, que se encarga de:

* Inicialización y configuración del sensor.
* Captura en tiempo real de imágenes o secuencias.
* Preprocesado (filtro, normalización, corrección geométrica).
* Transmisión interna de eventos visuales (presencia, gesto, rostro, posición).

### 14.7. Conclusión

El IMX219 proporciona una solución visual estable, eficiente y de bajo consumo para sistemas embebidos. Su integración mediante CSI elimina la necesidad de cableado auxiliar, y su compatibilidad con librerías estándar permite una rápida explotación funcional. Este módulo constituye una de las fuentes sensoriales principales de NORA.
