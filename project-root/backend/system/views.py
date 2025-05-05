from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from psutil import cpu_percent, virtual_memory  # Usamos psutil para obtener el estado del sistema

class SystemStatusView(APIView):
    permission_classes = [IsAuthenticated]  # Aseguramos que el usuario esté autenticado

    def get(self, request):
        # Obtenemos el estado del sistema
        cpu_usage = cpu_percent(interval=1)  # Obtiene el porcentaje de uso de la CPU
        memory = virtual_memory()
        system_status = {
            'systemStatus': 'Todo funciona correctamente',  # Puedes cambiarlo según el estado real
            'cpuUsage': cpu_usage,
            'memoryUsage': memory.percent,
            'dbConnection': True  # Aquí deberías verificar si la conexión a la base de datos está activa
        }
        return Response(system_status)
