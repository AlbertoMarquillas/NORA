from fsm.fsm_controller.fsm_controller import fsm
from fsm.definitions.fsm_definitions import FSMEvent
from typing import Optional

def emitir_evento_desde_backend(evento: FSMEvent, descripcion: Optional[str] = "") -> str:
    """
    Recibe un evento generado desde cualquier módulo del backend,
    lo inyecta en la FSM y devuelve el nuevo estado.
    """
    fsm.recibir_evento(evento)
    nuevo_estado = fsm.procesar_siguiente_evento()
    return nuevo_estado.name if nuevo_estado else fsm.obtener_estado_actual().name
