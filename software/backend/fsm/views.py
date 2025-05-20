from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from fsm.fsm_controller.fsm_controller import fsm
from fsm.definitions.fsm_definitions import FSMEvent
from fsm.dispatcher import emitir_evento_desde_backend

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

    nuevo_estado_nombre = emitir_evento_desde_backend(evento)

    return Response({
        "estado_actual": nuevo_estado_nombre,
    })

@api_view(["POST"])
def recibir_sensor_backend(request):
    sensor = request.data.get("sensor")
    valor = request.data.get("value")
    estado_actual = request.data.get("current_state")

    try:
        valor = float(valor)
    except (TypeError, ValueError):
        return Response({"error": "Valor numérico inválido"}, status=400)


    if sensor == "temperatura":
        if valor > 45:
            evento = FSMEvent.EVT_MODULE_FAILURE
        elif valor < 0:
            evento = FSMEvent.CMD_INHIBIR_ACTIVACION
        else:
            return Response({"estado_actual": estado_actual})  # no hay transición

        nuevo_estado = emitir_evento_desde_backend(evento)
        return Response({"estado_actual": nuevo_estado})

    return Response({"error": "sensor no reconocido"}, status=400)
