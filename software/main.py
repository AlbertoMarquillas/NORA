"""
Archivo principal: main.py

Punto de entrada del sistema NORA en modo de desarrollo o simulación.
Inicializa el entorno, carga el sistema de eventos, y lanza los módulos configurados
según el modo de ejecución especificado.

Este archivo se mantiene mínimo; su única función es orquestar el sistema
activando los componentes definidos en `src/` y controlando el bucle principal.
"""

import os
import sys
import argparse

# Simulación de la activación de módulos (reales o mocks)

def iniciar_sistema(simulacion: bool):
    modo = "SIMULACIÓN" if simulacion else "PRODUCCIÓN"
    print(f"[main.py] Iniciando NORA en modo {modo}...\n")

    # Inicialización del gestor de eventos
    print("[main.py] Cargando EventManager... (pendiente de implementación)")

    # Arranque de módulos simulados
    print("[main.py] Cargando módulos del sistema:")
    print("  - visión")
    print("  - voz")
    print("  - interfaz gráfica / facial")
    print("  - control físico")
    print("  - sistema central (FSM)")
    print("  - base de datos y rutinas")

    print("\n[main.py] Sistema en marcha. Esperando eventos...\n")
    
    # Bucle principal simulado
    try:
        while True:
            pass  # A reemplazar por detección de eventos
    except KeyboardInterrupt:
        print("\n[main.py] Interrupción detectada. Cerrando NORA...")
        # Procedimientos de apagado ordenado


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arranque del asistente físico NORA")
    parser.add_argument("--simulacion", action="store_true", help="Ejecutar en modo simulación (sin hardware)")
    args = parser.parse_args()

    iniciar_sistema(simulacion=args.simulacion)
