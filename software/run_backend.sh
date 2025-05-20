#!/bin/bash
cd backend
source ../venv/bin/activate
pip install -r ../requirements.txt
python manage.py makemigrations
python manage.py migrate
daphne backend.asgi:application
