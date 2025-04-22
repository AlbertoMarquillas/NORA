"""
Archivo: utils/estructura_src.py

Este script genera la estructura de carpetas lógica para el directorio src/ del proyecto NORA.
Debe ejecutarse una sola vez al iniciar el repositorio.

Crea las siguientes carpetas dentro de src/:
- vision/     → percepción visual (detección facial, postural, atención)
- voz/        → reconocimiento y síntesis de voz (ASR + TTS)
- interfaz/   → control de rostro animado, LEDs, expresividad simbólica
- control/    → coordinación de servos y gestos físicos
- sistema/    → lógica central, activación NFC, FSM general
- datos/      → gestión local de rutinas, notas, eventos y perfil de usuario

Cada carpeta contiene un __init__.py para ser usada como paquete Python.
"""

import os

def crear_estructura_src():
    folders = [
        "vision",
        "voz",
        "interfaz",
        "control",
        "sistema",
        "datos"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        init_file = os.path.join(folder, "__init__.py")
        with open(init_file, "w") as f:
            f.write(f"# Módulo {folder} - inicializado\n")

    print("[estructura_src.py] Estructura de src/ creada con éxito.")


if __name__ == "__main__":
    crear_estructura_src()