"""
fsm_urls.py

Rutas HTTP del subdominio de la máquina de estados finita (FSM).
Este módulo contiene endpoints relacionados con el control,
la observabilidad y la interacción directa con la FSM del sistema NORA.
"""

from django.urls import path

from api.views.fsm_views import (
    lista_transiciones,
    obtener_estado_actual,
    recibir_evento_fsm,
    recibir_sensor_backend,
)

app_name = "fsm"

urlpatterns = [
    # Inyección directa de un evento interno de la FSM.
    path("event/", recibir_evento_fsm, name="dispatch_event"),

    # Compatibilidad temporal con clientes legacy.
    path("evento/", recibir_evento_fsm, name="dispatch_event_legacy"),

    # Recepción de datos de sensores internos.
    path("sensor/", recibir_sensor_backend, name="ingest_sensor"),

    # Consulta del historial persistido de transiciones.
    path("transitions/", lista_transiciones, name="list_transitions"),

    # Consulta del estado actual de la FSM.
    path("state/", obtener_estado_actual, name="get_state"),

    # Futuros endpoints razonables:
    # path("snapshot/", obtener_snapshot_fsm, name="get_snapshot"),
    # path("queue/", listar_eventos_pendientes, name="list_pending_events"),
    # path("reset/", reiniciar_fsm, name="reset"),
]