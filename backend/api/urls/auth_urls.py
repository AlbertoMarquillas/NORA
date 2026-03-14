"""
auth_urls.py

Rutas HTTP del subdominio de autenticación y perfil básico del usuario.
Este módulo agrupa exclusivamente endpoints relacionados con login,
refresh de tokens, logout, registro y consulta del usuario autenticado.
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api.views.auth_views import (
    CustomTokenObtainPairView,
    RegisterView,
    LogoutView,
    MeView,
)

# Namespace de URLs para poder referenciar rutas como:
# reverse("auth:login"), reverse("auth:me"), etc.
app_name = "auth"

urlpatterns = [
    # Inicio de sesión mediante username o email.
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),

    # Renovación del access token a partir del refresh token.
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),

    # Cierre de sesión del usuario autenticado.
    # Si usas blacklist de refresh tokens, esta vista puede invalidarlos.
    path("logout/", LogoutView.as_view(), name="logout"),

    # Registro de nuevos usuarios.
    path("register/", RegisterView.as_view(), name="register"),

    # Perfil del usuario autenticado actualmente.
    path("me/", MeView.as_view(), name="me"),
]