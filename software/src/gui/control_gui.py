"""
Módulo: gui/control_gui.py

Clase ControlGUI – Interfaz gráfica de usuario (GUI) para control y simulación del sistema NORA.
Diseñada con Tkinter para ofrecer una vista más clara, estructurada y profesional del estado, respuesta
visual, control de eventos y espacio reservado para futuras visualizaciones.
"""

import tkinter as tk
from functools import partial
from src.sistema.event_manager import Evento

class ControlGUI:
    def __init__(self, sistema):
        self.sistema = sistema
        self.root = tk.Tk()
        self.root.title("NORA – Panel de Control")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # MARCO PRINCIPAL
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # COLUMNA IZQUIERDA (Estado, respuesta, control)
        left_frame = tk.Frame(main_frame, bg="#f0f0f0")
        left_frame.pack(side="left", fill="y", padx=(0, 20))

        # ESTADO
        tk.Label(left_frame, text="Estado actual:", font=("Segoe UI", 12), bg="#f0f0f0").pack(anchor="w")
        self.label_estado = tk.Label(left_frame, text="---", font=("Segoe UI", 20, "bold"), fg="#444", bg="#f0f0f0")
        self.label_estado.pack(anchor="w", pady=(0, 15))

        # RESPUESTA
        tk.Label(left_frame, text="Respuesta del sistema:", font=("Segoe UI", 12), bg="#f0f0f0").pack(anchor="w")
        self.label_respuesta = tk.Label(left_frame, text="---", font=("Segoe UI", 14), fg="#555", wraplength=300, justify="left", bg="#f0f0f0")
        self.label_respuesta.pack(anchor="w", pady=(0, 15))

        # SIMBOLO
        self.label_simbolo = tk.Label(left_frame, text="", font=("Segoe UI", 50), bg="#f0f0f0")
        self.label_simbolo.pack(pady=10)

        # BOTONES DE EVENTOS
        botones_frame = tk.LabelFrame(left_frame, text="Enviar evento", padx=10, pady=10, bg="#f0f0f0")
        botones_frame.pack(pady=10)

        eventos = [
            ("Presencia", "EVT_FACE_DETECTED"),
            ("NFC", "EVT_NFC_ACTIVATE"),
            ("Comando OK", "EVT_COMMAND_RECOGNIZED"),
            ("Comando ???", "EVT_COMMAND_UNKNOWN"),
            ("Timeout", "EVT_IDLE_TIMEOUT"),
            ("Apagar", "EVT_SHUTDOWN_REQUEST")
        ]

        for idx, (nombre, evento) in enumerate(eventos):
            b = tk.Button(botones_frame, text=nombre, width=20, height=1, font=("Segoe UI", 10),
                          command=partial(self.enviar_evento, evento))
            b.grid(row=idx, column=0, padx=6, pady=4, sticky="w")

        # COLUMNA DERECHA (Espacio para gráficos o visualizaciones futuras)
        right_frame = tk.LabelFrame(main_frame, text="Visualización futura", padx=10, pady=10, bg="#ffffff")
        right_frame.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(right_frame, bg="#ffffff")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_text(200, 100, text="X", fill="#888", font=("Segoe UI", 14))

        # SUSCRIPCIONES
        self.sistema.eventos.suscribir("EVT_MOSTRAR_ESTADO", self.actualizar_estado)
        self.sistema.eventos.suscribir("EVT_DECIR_TEXTO", self.mostrar_respuesta)

    def enviar_evento(self, tipo):
        self.sistema.eventos.emitir(Evento(tipo, origen="gui"))
        self.sistema.eventos.procesar()

    def actualizar_estado(self, evento):
        estado = evento.datos.get("estado", "---")
        simbolo = {
            "REPOSO": "💤",
            "PASIVO": "😐",
            "ESCUCHA": "👂",
            "ACTIVO": "🟢",
            "ERROR": "❌"
        }.get(estado.upper(), "⬜")

        self.label_estado.config(text=estado)
        self.label_simbolo.config(text=simbolo)

    def mostrar_respuesta(self, evento):
        texto = evento.datos.get("texto", "---")
        self.label_respuesta.config(text=texto)

    def lanzar(self):
        self.root.mainloop()
