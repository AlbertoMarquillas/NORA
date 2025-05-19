from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from fsm.fsm_controller.fsm_controller import fsm
from fsm.definitions.fsm_definitions import FSMEvent

@api_view(['POST'])
def recibir_evento_fsm(request):
    """
    Recibe un evento del frontend, lo inyecta en la FSM y devuelve el estado actual.
    """
    nombre_evento = request.data.get("evento")

    if not nombre_evento:
        return Response({"error": "No se ha especificado un evento"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        evento = FSMEvent[nombre_evento]
    except KeyError:
        return Response({"error": f"Evento no reconocido: {nombre_evento}"}, status=status.HTTP_400_BAD_REQUEST)

    fsm.recibir_evento(evento)
    nuevo_estado = fsm.procesar_siguiente_evento()

    return Response({
        "estado_actual": (nuevo_estado.name if nuevo_estado else fsm.obtener_estado_actual().name)
    })
