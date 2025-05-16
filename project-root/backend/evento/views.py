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
    if request.method != "POST":
        return JsonResponse({"error": "Solo se aceptan peticiones POST"}, status=405)

    try:
        datos = json.loads(request.body)
        if datos.get("type") != "fsm_event":
            return JsonResponse({"error": "Tipo de evento no válido"}, status=400)

        evento_nombre = datos.get("evento")
        descripcion = datos.get("descripcion", "")

        # Convertir string a FSMEvent
        evento = FSMEvent[evento_nombre]

        # Enviar evento a la FSM y procesarlo
        fsm_controller.recibir_evento(evento)
        fsm_controller.procesar_siguiente_evento()

        return JsonResponse({
            "status": "ok",
            "evento": evento.name,
            "descripcion": descripcion
        })

    except KeyError:
        return JsonResponse({"error": f"Evento desconocido: {evento_nombre}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def estado_fsm_actual(request):
    return JsonResponse({
        "estado": fsm_controller.estado_actual.name
    })

