"""
Módulo: sistema/sistema.py

Define la clase Sistema, encargada de inicializar y coordinar los módulos
funcionales del asistente NORA. Centraliza la FSM, EventManager, interfaz,
voz y respuesta simbólica, con soporte para ejecución en modo simulación.
"""

from functools import partial
from time import sleep

from src.sistema.fsm import FSM
from src.sistema.event_manager import EventManager, Evento
from src.voz.reconocedor import ReconocedorVoz
from src.voz.sintetizador import SintetizadorVoz
from src.interfaz.interfaz import InterfazSimulada
from src.sistema.manejadores import manejar_evento_fsm

class Sistema:
    def __init__(self, simulacion=True):
        self.simulacion = simulacion
        self.fsm = FSM()
        self.eventos = EventManager()
        self.reconocedor = ReconocedorVoz(self.eventos)
        self.sintetizador = SintetizadorVoz(self.eventos)
        self.interfaz = InterfazSimulada(self.eventos)

        # Registro del manejador FSM a los eventos relevantes
        handler = partial(manejar_evento_fsm, fsm=self.fsm, em=self.eventos)
        for tipo in [
            "EVT_NFC_ACTIVATE",
            "EVT_FACE_DETECTED",
            "EVT_COMMAND_RECOGNIZED",
            "EVT_COMMAND_UNKNOWN",
            "EVT_IDLE_TIMEOUT",
            "EVT_SHUTDOWN_REQUEST"
        ]:
            self.eventos.suscribir(tipo, handler)

    def ejecutar_simulacion(self):
        """
        Ejecuta una secuencia de eventos simulados, verificando el flujo FSM,
        respuesta de voz y representación visual.
        """
        secuencia = [
            "EVT_NFC_ACTIVATE",
            "EVT_FACE_DETECTED",
            "EVT_COMMAND_RECOGNIZED",
            "EVT_IDLE_TIMEOUT",
            "EVT_SHUTDOWN_REQUEST"
        ]

        print(f"[Sistema] Iniciando simulación en modo {'SIMULACIÓN' if self.simulacion else 'PRODUCCIÓN'}\n")
        print(f"[Sistema] Estado inicial: {self.fsm.estado_actual.name}\n")

        for tipo in secuencia:
            sleep(1.0)
            print(f"[Sistema] → Emitiendo evento: {tipo}")
            self.eventos.emitir(Evento(tipo, origen="sistema"))
            self.eventos.procesar()

            if self.fsm.estado_actual.name == "ESCUCHA":
                print("[Sistema] → FSM en ESCUCHA: activando reconocimiento de voz")
                self.reconocedor.escuchar_simulado()
                self.eventos.procesar()

        print("[Sistema] Simulación completada.\n")