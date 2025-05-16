"""
main_backend.py

Lanzador principal del sistema NORA.
Inicia el servidor Django y el motor de voz en procesos independientes.
Diseñado para entorno Linux (compatible con Raspberry Pi).
"""

import multiprocessing
import os
import time
import sys
from voz.motor_voz import iniciar_motor_voz

# ─────────────────────────────────────────────────────────────
# 🎧 Variables de entorno para evitar errores de audio en Linux
# ─────────────────────────────────────────────────────────────
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
os.environ["ALSA_CARD"] = "default"
os.environ["SDL_AUDIODRIVER"] = "pulse"  # también puedes probar "dsp"

# ─────────────────────────────────────────────────────────────
# 🚀 Funciones de arranque
# ─────────────────────────────────────────────────────────────

def lanzar_backend():
    """
    Inicia el servidor de Django.
    """
    print("🚀 Iniciando backend Django...")
    os.system("python manage.py runserver 0.0.0.0:8000")


def lanzar_motor_voz():
    """
    Llama al motor de voz ya importado desde voz.motor_voz.
    """
    iniciar_motor_voz()

# ─────────────────────────────────────────────────────────────
# 🧠 Ejecución principal
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        backend_proc = multiprocessing.Process(target=lanzar_backend)
        voz_proc = multiprocessing.Process(target=lanzar_motor_voz)

        backend_proc.start()
        time.sleep(2)  # Espera para asegurar que el backend arranca
        voz_proc.start()

        print("✅ Sistema NORA en ejecución (backend + voz).")
        print("🛑 Pulsa Ctrl+C para detener.")

        backend_proc.join()
        voz_proc.join()

    except KeyboardInterrupt:
        print("\n🧹 Interrupción manual detectada. Cerrando procesos...")
        backend_proc.terminate()
        voz_proc.terminate()
        backend_proc.join()
        voz_proc.join()
        print("✅ Sistema NORA finalizado con éxito.")

    except Exception as e:
        print(f"❌ Error crítico al iniciar NORA: {e}")
        sys.exit(1)
