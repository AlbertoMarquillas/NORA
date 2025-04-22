"""
Módulo: sistema/manejadores.py

Define funciones manejadoras externas para eventos del sistema, 
como el controlador principal de eventos FSM, desacoplado de main.py.
"""

from src.sistema.event_manager import Evento


def manejar_evento_fsm(evento: Evento, fsm, em):
    """
    Maneja eventos relacionados con la lógica FSM.
    Emite respuestas habladas cuando el evento contiene texto reconocido.
    """
    nuevo_estado = fsm.transicion(evento.tipo)
    print(f"[FSM] ← Estado actualizado: {nuevo_estado.name}\n")

    if evento.tipo == "EVT_COMMAND_RECOGNIZED":
        texto = evento.datos.get("texto")
        if texto:
            respuesta = f"He entendido: {texto}"
            em.emitir(Evento("EVT_DECIR_TEXTO", origen="fsm", datos={"texto": respuesta}))
        else:
            print("[FSM] Advertencia: comando sin texto reconocido — no se emite respuesta")