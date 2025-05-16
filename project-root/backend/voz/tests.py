"""
main.py

Script autónomo para lanzar solo el sistema de voz de NORA.
Útil para pruebas, depuración o integración parcial sin iniciar el backend completo.
"""

from voz.motor_voz import iniciar_motor_voz


if __name__ == "__main__":
    try:
        iniciar_motor_voz()
    except Exception as e:
        print(f"❌ Error crítico al iniciar el motor de voz: {e}")
