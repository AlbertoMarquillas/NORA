"""
Controlador principal de la máquina de estados finita (FSM) del sistema NORA.
Gestiona transiciones, evalúa condiciones y guarda eventos. Integra eventos desde
el frontend y sensores externos, y reenvía el resultado a ambos canales.
"""

import time
import heapq
import logging
import os
from typing import List, Callable, Optional
from evento.models import TransicionFSM
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from fsm.definitions.fsm_definitions import FSMState, FSMEvent
from fsm.definitions.fsm_transitions import FSM_TRANSITIONS
from fsm.definitions.fsm_priority import FSM_EVENT_PRIORITY, DEFAULT_EVENT_PRIORITY
from fsm.definitions.fsm_conditions import FSMContext, condicion_siempre
from fsm.definitions.fsm_guard_clauses import guardia_siempre_permitido
from fsm.definitions.fsm_emotional_states import EmotionalStatus

# Logger configurado
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'backend', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_PATH = os.path.join(LOG_DIR, 'fsm.log')
logger = logging.getLogger("fsm")
logger.setLevel(logging.INFO)
if not logger.handlers:
    fh = logging.FileHandler(LOG_PATH)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)


class PendingEvent:
    def __init__(self, event: FSMEvent, timestamp: float):
        self.event = event
        self.priority = FSM_EVENT_PRIORITY.get(event, DEFAULT_EVENT_PRIORITY)
        self.timestamp = timestamp

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.timestamp < other.timestamp


class FSMController:
    def __init__(self):
        self.estado_actual: FSMState = FSMState.INACTIVO
        self.contexto: FSMContext = FSMContext()
        self.estado_emocional: EmotionalStatus = EmotionalStatus()
        self.event_queue: List[PendingEvent] = []
        self.guardias: List[Callable[[FSMState, FSMEvent, FSMState, FSMContext], bool]] = [
            guardia_siempre_permitido
        ]
        self.condiciones: List[Callable[[FSMContext], bool]] = [
            condicion_siempre
        ]

    def recibir_evento(self, evento: FSMEvent, timestamp: Optional[float] = None):
        t = timestamp or time.time()
        heapq.heappush(self.event_queue, PendingEvent(evento, t))

    def procesar_siguiente_evento(self) -> Optional[FSMState]:
        if not self.event_queue:
            return None

        evento_pendiente = heapq.heappop(self.event_queue)
        clave = (self.estado_actual, evento_pendiente.event)

        if clave not in FSM_TRANSITIONS:
            return None

        destino = FSM_TRANSITIONS[clave]

        if not all(cond(self.contexto) for cond in self.condiciones):
            return None

        for guardia in self.guardias:
            if not guardia(self.estado_actual, evento_pendiente.event, destino, self.contexto):
                return None

        self._transicionar(destino, evento_pendiente.event)
        return destino

    def _transicionar(self, nuevo_estado: FSMState, evento: FSMEvent):
        estado_anterior = self.estado_actual.name
        self.estado_actual = nuevo_estado

        log_msg = f"[FSM] {estado_anterior} --({evento.name})--> {nuevo_estado.name}"
        print(log_msg)
        logger.info(log_msg)

        TransicionFSM.objects.create(
            estado_anterior=estado_anterior,
            evento=evento.name,
            estado_nuevo=nuevo_estado.name
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "fsm_updates",
            {
                "type": "send_fsm_event",
                "content": {
                    "evento": evento.name,
                    "nuevo_estado": nuevo_estado.name,
                },
            }
        )

        # Aquí deberías emitir señales (ej. WebSocket) para frontend y agentes externos

    def actualizar_contexto(self, nuevo_contexto: FSMContext):
        self.contexto = nuevo_contexto

    def actualizar_estado_emocional(self, nuevo_estado: str, intensidad: float):
        self.estado_emocional.actualizar(nuevo_estado, intensidad)

    def obtener_estado_actual(self) -> FSMState:
        return self.estado_actual

# Al final del archivo
fsm = FSMController()
