"""
fsm_validation_test.py

Script de validación estructural de la FSM:
- Verifica que todos los eventos y estados usados en la tabla de transiciones
  estén definidos en los enums FSMEvent y FSMState.

Se utiliza para evitar errores por referencias inválidas o definiciones incompletas.
"""

from fsm_control.definitions.fsm_definitions import FSMEvent, FSMState
from fsm_control.definitions.fsm_transitions import FSM_TRANSITIONS

def validar_transiciones():
    errores = []
    eventos_definidos = set(item for item in FSMEvent)
    estados_definidos = set(item for item in FSMState)

    for (estado_origen, evento), estado_destino in FSM_TRANSITIONS.items():
        if estado_origen not in estados_definidos:
            errores.append(f"Estado origen no definido: {estado_origen}")
        if evento not in eventos_definidos:
            errores.append(f"Evento no definido: {evento}")
        if estado_destino not in estados_definidos:
            errores.append(f"Estado destino no definido: {estado_destino}")

    if errores:
        print("Errores encontrados en FSM_TRANSITIONS:")
        for error in errores:
            print("   -", error)
    else:
        print("Todas las transiciones están correctamente definidas.")

if __name__ == "__main__":
    validar_transiciones()
