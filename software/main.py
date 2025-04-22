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
import time

from src.sistema.fsm import FSM

# Simulación de eventos controlados
EVENTOS_SIMULADOS = [
    "EVT_NFC_ACTIVATE",
    "EVT_FACE_DETECTED",
    "EVT_COMMAND_RECOGNIZED",
    "EVT_IDLE_TIMEOUT",
    "EVT_SHUTDOWN_REQUEST"
]

def iniciar_sistema(simulacion: bool):
    modo = "SIMULACIÓN" if simulacion else "PRODUCCIÓN"
    print(f"[main.py] Iniciando NORA en modo {modo}...\n")

    # Inicialización de la FSM
    fsm = FSM()
    print(f"[main.py] Estado inicial: {fsm.estado_actual.name}\n")

    # Simulación de eventos en secuencia
    for evento in EVENTOS_SIMULADOS:
        time.sleep(1.2)
        print(f"[main.py] → Enviando evento: {evento}")
        nuevo_estado = fsm.transicion(evento)
        print(f"[main.py] ← Nuevo estado: {nuevo_estado.name}\n")

    print("[main.py] Secuencia de simulación finalizada.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arranque del asistente físico NORA")
    parser.add_argument("--simulacion", action="store_true", help="Ejecutar en modo simulación (sin hardware)")
    args = parser.parse_args()

    iniciar_sistema(simulacion=args.simulacion)