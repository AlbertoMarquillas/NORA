from src.sistema.fsm import FSM
from src.sistema.event_manager import EventManager, Evento

em = EventManager()
fsm = FSM()

def manejador_fsm(evento):
    fsm.transicion(evento.tipo)

# Registrar eventos relevantes
em.suscribir("EVT_NFC_ACTIVATE", manejador_fsm)
em.suscribir("EVT_FACE_DETECTED", manejador_fsm)
em.suscribir("EVT_COMMAND_RECOGNIZED", manejador_fsm)
em.suscribir("EVT_IDLE_TIMEOUT", manejador_fsm)

# Emitir eventos simulados
em.emitir(Evento("EVT_NFC_ACTIVATE", origen="main"))
em.emitir(Evento("EVT_FACE_DETECTED", origen="main"))
em.emitir(Evento("EVT_COMMAND_RECOGNIZED", origen="voz"))
em.emitir(Evento("EVT_IDLE_TIMEOUT", origen="sistema"))

# Procesar la cola
em.procesar()
