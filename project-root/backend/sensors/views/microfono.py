from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from sensors.modules.microfono import detectar_voz
from fsm_control.evaluadores import evaluar_evento_microfono

@csrf_exempt
def sensor_microfono(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        valor_simulado = data.get('value')
        estado_actual = data.get('current_state')

        voz_detectada = detectar_voz(valor_simulado)
        evento_futuro = evaluar_evento_microfono(voz_detectada, estado_actual)

        return JsonResponse({'evento_futuro': evento_futuro})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
