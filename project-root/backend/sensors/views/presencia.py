from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from sensors.modules.presencia import detectar_presencia
from fsm_control.evaluadores import evaluar_evento_presencia

@csrf_exempt
def sensor_presencia(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        valor_simulado = data.get('value')
        estado_actual = data.get('current_state')

        presencia = detectar_presencia(valor_simulado)
        evento_futuro = evaluar_evento_presencia(presencia, estado_actual)

        return JsonResponse({'evento_futuro': evento_futuro})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
