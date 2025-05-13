# backend/main_backend.py

import multiprocessing
import os
import time
from subprocess import Popen

def lanzar_backend():
    os.system("python manage.py runserver 0.0.0.0:8000")

def lanzar_voz():
    os.system("python voz/main.py")

if __name__ == "__main__":
    backend_proc = multiprocessing.Process(target=lanzar_backend)
    voz_proc = multiprocessing.Process(target=lanzar_voz)

    backend_proc.start()
    time.sleep(2)  # espera breve para asegurar que el backend arranque
    voz_proc.start()

    backend_proc.join()
    voz_proc.join()
