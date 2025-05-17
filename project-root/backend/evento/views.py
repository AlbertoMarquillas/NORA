# backend/api/views.py (o evento/views.py)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from fsm_control.fsm_controller import FSMController
from evento.models import EventoRecibido
from fsm_control.definitions.fsm_definitions import FSMEvent

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


@csrf_exempt
def recibir_evento_fsm(request):
    """
    Procesa un evento de tipo FSM enviado desde el frontend.
    El evento debe venir con tipo 'fsm_event' y el nombre del evento.
    """
    try:
        if request.data.get("type") != "fsm_event":
            return JsonResponse({"error": "Tipo de evento no válido"}, status=400)

        evento_nombre = request.data.get("evento")
        descripcion = request.data.get("descripcion", "")

        # Convertir a Enum
        evento = FSMEvent[evento_nombre]

        fsm_controller.recibir_evento(evento)
        fsm_controller.procesar_siguiente_evento()

        return JsonResponse({
            "status": "ok",
            "evento": evento.name,
            "descripcion": descripcion,
            "estado_actual": fsm_controller.estado_actual.name,
        }, status=200)

    except KeyError:
        return JsonResponse({"error": f"Evento desconocido: {evento_nombre}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

def estado_fsm_actual(request):
    return JsonResponse({
        "estado": fsm_controller.estado_actual.name
    })

