from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
# authsystem/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("username")  # username puede ser email aquí
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
            attrs["username"] = user.username  # Redirigimos al username real
        except User.DoesNotExist:
            raise serializers.ValidationError("No user with this email.")

        return super().validate(attrs)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username_or_email = request.data.get("username_or_email")
        password = request.data.get("password")

        user = authenticate(username=username_or_email, password=password)
        if not user:
            # intentamos con email
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass

        if not user:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "username": user.username,
            "email": user.email,
            "avatar": None,
            "is_admin": user.is_staff,
            "is_guest": False  # esto se puede ajustar si hay modelo extendido
        })


class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    print(request.headers)  # Verifica si el token está presente
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
        "avatar": None,  # Si en el futuro se añade
        "is_admin": user.is_staff,
        "is_guest": False  # Puedes implementar esto como desees
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    try:
        # Opcionalmente revoca el token si usas token blacklisting
        return Response({"detail": "Successfully logged out."})
    except Exception as e:
        return Response({"detail": str(e)}, status=400)
