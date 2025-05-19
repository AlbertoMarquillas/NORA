from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TransicionFSM

@api_view(['GET'])
def lista_transiciones(request):
    transiciones = TransicionFSM.objects.order_by('-timestamp')[:10]
    data = [
        {
            "timestamp": t.timestamp,
            "estado_anterior": t.estado_anterior,
            "evento": t.evento,
            "estado_nuevo": t.estado_nuevo
        }
        for t in transiciones
    ]
    return Response(data)
