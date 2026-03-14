"""
WSGI configuration for the NORA backend project.

This module exposes the WSGI callable used by WSGI-compatible
servers (e.g., Gunicorn, uWSGI).

Reference:
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
from pathlib import Path


# --------------------------------------------------
# Load environment variables from .env
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")


# --------------------------------------------------
# Django settings module
# --------------------------------------------------

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "backend.server.settings.dev"
)


# --------------------------------------------------
# WSGI application
# --------------------------------------------------

application = get_wsgi_application()