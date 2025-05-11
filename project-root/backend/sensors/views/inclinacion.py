from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def sensor_inclinacion(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        inclinacion = data.get('value')
        estado_actual = data.get('current_state')

        evento_futuro = "EVT_ATTENTION_GAINED" if inclinacion else None
        return JsonResponse({'evento_futuro': evento_futuro})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
