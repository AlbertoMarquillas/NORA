"""
motor_voz.py

Motor principal del sistema de voz de NORA.
Orquesta el bucle de escucha, reconocimiento y procesamiento de frases.
Diseñado para ejecutarse como proceso independiente o dentro del lanzador general.
"""

import time
from voz.recognizer import escuchar_frase
from voz.procesador import procesar_frase
from voz.definiciones import DEBUG_VOZ


def iniciar_motor_voz():
    """
    Bucle principal del sistema de voz.
    Escucha frases, las procesa, y ejecuta acciones o respuestas.
    """
    print("🎙️ Motor de voz iniciado. Esperando comandos...\n")

    while True:
        try:
            frase = escuchar_frase()
            if not frase:
                if DEBUG_VOZ:
                    print("🔁 No se obtuvo frase válida. Esperando nueva entrada...\n")
                continue

            procesar_frase(frase)

        except KeyboardInterrupt:
            print("\n🛑 Motor de voz detenido manualmente.")
            break

        except Exception as e:
            print(f"❌ Error inesperado en el motor de voz: {e}")
            time.sleep(1)  # espera mínima para evitar bucle incontrolado

    print("🟢 Finalización del motor de voz.")

if __name__ == "__main__":
    # Si se ejecuta directamente, inicia el motor de voz
    iniciar_motor_voz()
    
    