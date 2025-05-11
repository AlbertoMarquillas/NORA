from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def sensor_temperatura(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        temperatura = data.get('value')
        estado_actual = data.get('current_state')

        # Aquí decides qué evento generar
        evento_futuro = None
        if temperatura is not None and temperatura > 30:
            evento_futuro = "EVT_SPEECH_START"  # o cualquier otro

        return JsonResponse({'evento_futuro': evento_futuro})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
