## 08. Configuración del Entorno Virtual para NORA

### Propósito del documento

Este documento define cómo configurar correctamente el entorno virtual del proyecto NORA, asegurando un espacio aislado y reproducible para el desarrollo. También describe el uso del archivo `requirements.txt` y la estructura de carpetas esperada.

---

### 📁 Ubicación del entorno virtual

El entorno virtual se crea en la **raíz del proyecto**, es decir, en la carpeta `NORA/`, no dentro de `src/`, para mantener una separación clara entre la lógica del sistema y la configuración del entorno.

```
NORA/
├── env/                   # Entorno virtual (creado por venv)
├── src/                  # Código fuente
├── docs/                 # Documentación técnica
├── utils/                # Scripts de soporte
├── requirements.txt      # Dependencias instaladas
└── .gitignore            # Exclusiones de control de versiones
```

---

### ✅ Creación del entorno virtual

```bash
cd NORA
python -m venv env
```

### ▶️ Activación del entorno

- **Windows:**
  ```bash
  .\env\Scripts\activate
  ```
- **Linux / macOS:**
  ```bash
  source env/bin/activate
  ```

---

### 📦 Archivo `requirements.txt`

El proyecto ya cuenta con un archivo `requirements.txt` inicial con las siguientes dependencias:

```txt
absl-py==2.2.2
attrs==25.3.0
certifi==2025.1.31
cffi==1.17.1
charset-normalizer==3.4.1
colorama==0.4.6
comtypes==1.4.10
contourpy==1.3.2
cycler==0.12.1
flatbuffers==25.2.10
fonttools==4.57.0
idna==3.10
jax==0.6.0
jaxlib==0.6.0
kiwisolver==1.4.8
matplotlib==3.10.1
mediapipe==0.10.21
ml_dtypes==0.5.1
networkx==3.4.2
numpy==1.26.4
opencv-contrib-python==4.11.0.86
opencv-python==4.11.0.86
opt_einsum==3.4.0
packaging==25.0
pillow==11.2.1
protobuf==4.25.6
pycparser==2.22
pyparsing==3.2.3
pypiwin32==223
python-dateutil==2.9.0.post0
pyttsx3==2.98
pywin32==310
requests==2.32.3
scipy==1.15.2
sentencepiece==0.2.0
six==1.17.0
sounddevice==0.5.1
srt==3.5.3
tqdm==4.67.1
urllib3==2.4.0
vosk==0.3.45
websockets==15.0.1
```

Puedes regenerar este archivo tras instalar nuevos paquetes con:
```bash
pip freeze > requirements.txt
```

---

### 🧪 Verificación del entorno

Para comprobar que todo funciona correctamente:

```bash
python -m pip list
python -c "import cv2; import mediapipe; import pyttsx3; print('Entorno OK')"
```
---

Este entorno virtual es la base para ejecutar el sistema NORA en modo desarrollo o simulación, manteniendo el aislamiento de librerías y garantizando reproducibilidad.

