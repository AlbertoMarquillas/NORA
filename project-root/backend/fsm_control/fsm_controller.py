"""
fsm_controller.py

Controlador principal de la máquina de estados finita (FSM) del sistema NORA.
Gestiona transiciones entre estados, aplica reglas de prioridad entre eventos,
evalúa condiciones contextuales y cláusulas de guarda antes de ejecutar cambios
de estado.

Permite una integración centralizada y extensible con el resto del sistema.
"""

import time
import heapq
from typing import List, Callable, Tuple, Optional

from fsm_control.definitions.fsm_definitions import FSMState, FSMEvent
from fsm_control.definitions.fsm_transitions import FSM_TRANSITIONS
from fsm_control.definitions.fsm_priority import FSM_EVENT_PRIORITY, DEFAULT_EVENT_PRIORITY
from fsm_control.definitions.fsm_conditions import FSMContext, condicion_siempre
from fsm_control.definitions.fsm_guard_clauses import guardia_siempre_permitido
from fsm_control.definitions.fsm_emotional_states import EmotionalStatus

class PendingEvent:
    """Representa un evento pendiente ordenado por prioridad y timestamp."""
    def __init__(self, event: FSMEvent, timestamp: float):
        self.event = event
        self.priority = FSM_EVENT_PRIORITY.get(event, DEFAULT_EVENT_PRIORITY)
        self.timestamp = timestamp

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.timestamp < other.timestamp

class FSMController:
    """
    Implementación del controlador FSM del sistema NORA.
    Gestiona el ciclo completo de recepción, evaluación y transición de estados.
    """
    def __init__(self):
        self.estado_actual: FSMState = FSMState.REPOSO
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
        """Añade un evento a la cola de eventos pendientes."""
        t = timestamp or time.time()
        heapq.heappush(self.event_queue, PendingEvent(evento, t))

    def procesar_siguiente_evento(self):
        """Evalúa y aplica la transición correspondiente al siguiente evento válido."""
        if not self.event_queue:
            return

        evento_pendiente = heapq.heappop(self.event_queue)
        clave = (self.estado_actual, evento_pendiente.event)

        if clave not in FSM_TRANSITIONS:
            return  # Transición no definida

        estado_destino = FSM_TRANSITIONS[clave]

        # Evaluar condiciones globales
        if not all(cond(self.contexto) for cond in self.condiciones):
            return

        # Evaluar guardias asociadas a la transición
        for guardia in self.guardias:
            if not guardia(self.estado_actual, evento_pendiente.event, estado_destino, self.contexto):
                return

        # Aplicar transición
        self._transicionar(estado_destino, evento_pendiente.event)

    def _transicionar(self, nuevo_estado: FSMState, evento: FSMEvent):
        """Ejecuta el cambio de estado y registra el evento."""
        print(f"[FSM] Transición: {self.estado_actual.name} --({evento.name})--> {nuevo_estado.name}")
        self.estado_actual = nuevo_estado
        # Aquí se podrían emitir señales, actualizar GUI o registrar logs estructurados

    def actualizar_contexto(self, nuevo_contexto: FSMContext):
        """Permite actualizar el contexto evaluable de forma externa."""
        self.contexto = nuevo_contexto

    def actualizar_estado_emocional(self, nuevo_estado: str, intensidad: float):
        """Permite modificar el estado emocional del sistema."""
        self.estado_emocional.actualizar(nuevo_estado, intensidad)
