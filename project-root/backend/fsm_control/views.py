from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from evento.models import EventoRecibido
from fsm_control.fsm_instance import fsm
from fsm_control.definitions.fsm_definitions import FSMEvent

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@csrf_exempt
def recibir_evento_fsm(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        tipo = data.get('type')
        evento_str = data.get('evento')
        descripcion = data.get('descripcion', '')

        if tipo != 'fsm_event' or not evento_str:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)

        try:
            evento = FSMEvent[evento_str]
        except KeyError:
            return JsonResponse({'error': f'Evento desconocido: {evento_str}'}, status=400)

        EventoRecibido.objects.create(
            tipo=tipo,
            evento=evento.name,
            descripcion=descripcion,
            origen='frontend'
        )

        fsm.recibir_evento(evento)
        fsm.procesar_siguiente_evento()

        # WebSocket: notificación al frontend
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "eventos",
            {
                "type": "enviar_evento",
                "data": {
                    "evento": evento.name,
                    "descripcion": descripcion,
                    "nuevo_estado": fsm.estado_actual.name,
                }
            }
        )

        return JsonResponse({
            'status': 'ok',
            'evento': evento.name,
            'nuevo_estado': fsm.estado_actual.name
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)


def estado_fsm_actual(request):
    return JsonResponse({
        "estado": fsm_controller.estado_actual.name
    })
