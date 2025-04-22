"""
Módulo: interfaz/interfaz.py

Este módulo define la clase InterfazSimulada, responsable de mostrar
representaciones visuales simbólicas del estado o emoción del asistente
NORA, en modo consola.

Este módulo escucha eventos mediante el EventManager y reacciona visualmente.
"""

from src.sistema.event_manager import Evento

class InterfazSimulada:
    def __init__(self, event_manager):
        self.em = event_manager

        self.iconos = {
            "REPOSO": "💤",
            "PASIVO": "😐",
            "ESCUCHA": "👂",
            "ACTIVO": "🟢",
            "ERROR": "❌",
            "UNKNOWN": "❓"
        }

        for tipo in [
            "EVT_COMMAND_RECOGNIZED",
            "EVT_COMMAND_UNKNOWN",
            "EVT_IDLE_TIMEOUT",
            "EVT_FACE_DETECTED",
            "EVT_NFC_ACTIVATE",
            "EVT_SHUTDOWN_REQUEST",
            "EVT_MOSTRAR_ESTADO"
        ]:
            self.em.suscribir(tipo, self.mostrar_estado)

        print("[InterfazSimulada] Subscrita a eventos visuales.")

    def mostrar_estado(self, evento: Evento):
        tipo = evento.tipo
        simbolo = ""
        mensaje = ""

        if tipo == "EVT_COMMAND_RECOGNIZED":
            simbolo = self.iconos.get("ACTIVO")
            mensaje = "Comando reconocido y ejecutado."

        elif tipo == "EVT_COMMAND_UNKNOWN":
            simbolo = self.iconos.get("UNKNOWN")
            mensaje = "No se ha entendido el comando."

        elif tipo == "EVT_IDLE_TIMEOUT":
            simbolo = self.iconos.get("REPOSO")
            mensaje = "Tiempo de inactividad."

        elif tipo == "EVT_FACE_DETECTED":
            simbolo = self.iconos.get("ESCUCHA")
            mensaje = "Presencia detectada."

        elif tipo == "EVT_NFC_ACTIVATE":
            simbolo = self.iconos.get("PASIVO")
            mensaje = "Activación por NFC."

        elif tipo == "EVT_SHUTDOWN_REQUEST":
            simbolo = self.iconos.get("REPOSO")
            mensaje = "Solicitud de apagado."

        elif tipo == "EVT_MOSTRAR_ESTADO":
            estado = evento.datos.get("estado", "")
            simbolo = self.iconos.get(estado.upper(), "⬜")
            mensaje = f"Estado actualizado → {estado}"

        print(f"[InterfazSimulada] {simbolo} {mensaje}")
