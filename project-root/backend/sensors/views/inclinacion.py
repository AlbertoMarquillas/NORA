from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from sensors.modules.inclinacion import detectar_inclinacion
from fsm_control.evaluadores import evaluar_evento_inclinacion

@csrf_exempt
def sensor_inclinacion(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        valor_simulado = data.get('value')
        estado_actual = data.get('current_state')

        inclinada = detectar_inclinacion(valor_simulado)
        evento_futuro = evaluar_evento_inclinacion(inclinada, estado_actual)

        return JsonResponse({'evento_futuro': evento_futuro})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
