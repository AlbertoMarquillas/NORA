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
from functools import partial

from src.sistema.fsm import FSM
from src.sistema.event_manager import EventManager, Evento
from src.voz.reconocedor import ReconocedorVoz
from src.voz.sintetizador import SintetizadorVoz
from src.sistema.manejadores import manejar_evento_fsm

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

    # Inicialización de componentes
    fsm = FSM()
    em = EventManager()
    voz = ReconocedorVoz(em)
    tts = SintetizadorVoz(em)

    # Registro de manejador FSM
    manejador = partial(manejar_evento_fsm, fsm=fsm, em=em)
    
    for tipo in [
        "EVT_NFC_ACTIVATE",
        "EVT_FACE_DETECTED",
        "EVT_COMMAND_RECOGNIZED",
        "EVT_COMMAND_UNKNOWN",
        "EVT_IDLE_TIMEOUT",
        "EVT_SHUTDOWN_REQUEST"
    ]:
        em.suscribir(tipo, manejador)

    print(f"[main.py] Estado inicial: {fsm.estado_actual.name}\n")

    # Emisión de eventos simulados + voz
    for tipo in EVENTOS_SIMULADOS:
        time.sleep(1.0)
        print(f"[main.py] → Emitiendo evento: {tipo}")
        em.emitir(Evento(tipo, origen="main"))
        em.procesar()

        if fsm.estado_actual.name == "ESCUCHA":
            print("[main.py] → FSM en estado ESCUCHA: activando reconocimiento de voz")
            voz.escuchar_simulado()
            em.procesar()


    print("[main.py] Secuencia de simulación finalizada.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arranque del asistente físico NORA")
    parser.add_argument("--simulacion", action="store_true", help="Ejecutar en modo simulación (sin hardware)")
    args = parser.parse_args()

    iniciar_sistema(simulacion=args.simulacion)