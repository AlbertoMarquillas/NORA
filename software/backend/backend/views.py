from rest_framework.views import APIView
from rest_framework.response import Response

class CorsTestView(APIView):
    def get(self, request):
        return Response({"message": "CORS ok"})