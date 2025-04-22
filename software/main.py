"""
Archivo principal: main.py

Punto de entrada del sistema NORA en modo de desarrollo o simulación.
Inicializa el entorno, instancia la clase Sistema y lanza la ejecución.
"""

import argparse
from src.sistema.sistema import Sistema

def main():
    parser = argparse.ArgumentParser(description="Arranque del asistente físico NORA")
    parser.add_argument("--simulacion", action="store_true", help="Ejecutar en modo simulación (sin hardware)")
    args = parser.parse_args()

    sistema = Sistema(simulacion=args.simulacion)
    sistema.ejecutar_simulacion()

if __name__ == "__main__":
    main()
