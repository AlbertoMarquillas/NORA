@echo off
call env\Scripts\activate.bat
echo Activando entorno...
pip install -r requirements.txt
echo Aplicando migraciones...
python backend\manage.py makemigrations
python backend\manage.py migrate
echo Iniciando servidor...
python backend\manage.py runserver
pause
