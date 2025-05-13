from recognizer import escuchar_frase
from responder import responder_texto
import re

# Lista de frases que activan a NORA
FRASES_ACTIVACION = [
    "hola nora",
    "oye nora",
    "nora estás ahí",
    "despierta nora",
    "nora activa"
]

FRASES_DESACTIVACION = [
    "nora apágate",
    "nora cierra",
    "nora silencio",
    "nora no hables más",
    "nora cállate",
    "adiós nora",
    "nora vete",
    "apagate nora",
    "nora vete a dormir"
]

def normalizar_texto(frase):
    """
    Convierte a minúsculas y elimina caracteres no alfabéticos (salvo espacios).
    """
    frase = frase.lower()
    frase = re.sub(r'[^a-záéíóúñü\s]', '', frase)  # elimina signos y dígitos
    return frase.strip()


def contiene_frase_clave(frase, lista_claves):
    """
    Devuelve True si alguna frase clave está contenida en la frase detectada.
    """
    frase = frase.lower()
    return any(clave in frase for clave in lista_claves)

def main():
    while True:
        frase = escuchar_frase()
        frase = normalizar_texto(frase)
        if frase:
            if contiene_frase_clave(frase, FRASES_ACTIVACION):
                enviar_evento_fsm("EVT_WAKEWORD", "Frase de activación detectada por voz")
            elif contiene_frase_clave(frase, FRASES_DESACTIVACION):
                enviar_evento_fsm("EVT_SHUTDOWN", "Frase de desactivación detectada por voz")
                break
            else:
                responder_texto("No he entendido tu mensaje.")

if __name__ == "__main__":
    main()
