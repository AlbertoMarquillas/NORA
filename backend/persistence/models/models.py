"""
models.py

Punto de entrada de modelos del app `backend`.

Django solo registra automáticamente los modelos que se importan
desde `backend.models`. Este archivo reexporta los modelos definidos
en los módulos internos de persistencia.
"""

from backend.persistence.models.auth_models import CustomUser
from backend.persistence.models.events_models import TransicionFSM

__all__ = [
    "CustomUser",
    "TransicionFSM",
]