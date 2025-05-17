# backend/api/views.py (o evento/views.py)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from fsm_control.fsm_controller import FSMController
from evento.models import EventoRecibido
from fsm_control.definitions.fsm_definitions import FSMEvent
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Instancia global del controlador FSM
fsm_controller = FSMController()

def listar_eventos(request):
    eventos = EventoRecibido.objects.order_by('-timestamp')[:50]
    datos = [
        {
            "evento": e.evento,
            "descripcion": e.descripcion,
            "tipo": e.tipo,
            "origen": e.origen,
            "timestamp": e.timestamp.isoformat(),
        }
        for e in eventos
    ]
    return JsonResponse(datos, safe=False)


@api_view(["POST"])
def recibir_evento_fsm(request):
    try:
        print("Petición recibida:", request.data)

        if request.data.get("type") != "fsm_event":
            print("Tipo de evento no válido:", request.data.get("type"))
            return Response({"error": "Tipo de evento no válido"}, status=status.HTTP_400_BAD_REQUEST)

        evento_nombre = request.data.get("evento")
        descripcion = request.data.get("descripcion", "")
        print("Evento recibido:", evento_nombre)

        evento = FSMEvent[evento_nombre]  # <- Aquí es donde puede fallar

        fsm_controller.recibir_evento(evento)
        fsm_controller.procesar_siguiente_evento()

        print("Evento procesado correctamente. Estado actual:", fsm_controller.estado_actual.name)

        return Response({
            "status": "ok",
            "evento": evento.name,
            "descripcion": descripcion,
            "estado_actual": fsm_controller.estado_actual.name,
        })

    except KeyError as e:
        print("Evento no reconocido:", e)
        return Response({"error": f"Evento desconocido: {evento_nombre}"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

def estado_fsm_actual(request):
    return JsonResponse({
        "estado": fsm_controller.estado_actual.name
    })

