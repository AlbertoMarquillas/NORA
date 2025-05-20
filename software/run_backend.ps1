# Navega a la carpeta del backend
cd backend

# Activa entorno virtual (ajusta la ruta si lo has movido)
& ../venv/Scripts/Activate.ps1

# Instala dependencias
pip install -r ../requirements.txt

# Aplica migraciones
python manage.py makemigrations
python manage.py migrate

# Ejecuta el servidor con Daphne
daphne backend.asgi:application
