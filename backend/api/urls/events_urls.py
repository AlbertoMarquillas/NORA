"""
events_urls.py

Rutas HTTP del subdominio de eventos externos del sistema.
Este módulo contiene endpoints de entrada de eventos procedentes
de audio, visión u otras fuentes externas al core FSM.
"""

from django.urls import path

from api.views.events_views import (
    recibir_evento_audio,
    recibir_evento_video,
)

app_name = "events"

urlpatterns = [
    # Ingesta de eventos procedentes del subsistema de audio.
    path("ingest/audio/", recibir_evento_audio, name="ingest_audio"),

    # Ingesta de eventos procedentes del subsistema de visión.
    path("ingest/video/", recibir_evento_video, name="ingest_video"),

    # Compatibilidad temporal con clientes legacy.
    path("audio/", recibir_evento_audio, name="audio_legacy"),
    path("video/", recibir_evento_video, name="video_legacy"),

    # Futuros endpoints razonables:
    # path("ingest/nfc/", recibir_evento_nfc, name="ingest_nfc"),
    # path("ingest/manual/", recibir_evento_manual, name="ingest_manual"),
    # path("ingest/system/", recibir_evento_sistema, name="ingest_system"),
]