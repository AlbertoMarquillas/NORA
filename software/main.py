"""
Archivo principal: main.py

Punto de entrada del sistema NORA.
Permite lanzar el sistema en modo simulación (--simulacion) o en modo GUI (--gui).
"""

import argparse
from src.sistema.sistema import Sistema

def main():
    parser = argparse.ArgumentParser(description="Arranque del asistente físico NORA")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--simulacion", action="store_true", help="Ejecutar en modo simulación (sin hardware)")
    group.add_argument("--gui", action="store_true", help="Ejecutar interfaz gráfica de control (GUI)")
    args = parser.parse_args()

    sistema = Sistema(simulacion=args.simulacion)

    if args.simulacion:
        sistema.ejecutar_simulacion()
    elif args.gui:
        sistema.ejecutar_gui()

if __name__ == "__main__":
    main()
