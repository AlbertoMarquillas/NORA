"""
backend_urls.py

Router raíz HTTP del backend de NORA.

Este módulo define el enrutado principal del servidor Django y delega
la gestión de rutas específicas a los submódulos de cada dominio
(`auth`, `events`, `fsm`).
"""

from django.contrib import admin
from django.urls import include, path

from api.views.backend_views import CorsTestView


urlpatterns = [

    # Panel de administración de Django
    path("admin/", admin.site.urls),

    # Endpoint simple para testear CORS durante desarrollo
    path("api/test-cors/", CorsTestView.as_view(), name="cors_test"),

    # Rutas de autenticación
    path("api/auth/", include("api.urls.auth_urls")),

    # Rutas de eventos externos
    path("api/events/", include("api.urls.events_urls")),

    # Rutas de control y observación de la FSM
    path("api/fsm/", include("api.urls.fsm_urls")),
]