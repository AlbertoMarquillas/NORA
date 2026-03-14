"""
intents.py

Definición de intenciones de alto nivel que la capa de aplicación
puede enviar a la capa action.

Notas de diseño
---------------
- Un ActionIntent representa una intención ejecutable, no una decisión FSM.
- Los intents deben ser estables y suficientemente genéricos para desacoplar
  la capa application de la implementación física concreta del robot.
- La implementación real se resuelve en action_executor.py y en la capa action.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any


class ActionIntentType(Enum):
    """
    Tipos de intención ejecutable por la capa action.

    Los intents están agrupados por dominio funcional para facilitar
    mantenibilidad, trazabilidad y crecimiento del sistema.
    """

    # =========================================================
    # CORE / CONTROL GENERAL
    # =========================================================

    NO_OP = auto()
    """
    No ejecutar ninguna acción. Útil como placeholder o salida neutra.
    """

    RESET_INTERACTION = auto()
    """
    Reiniciar recursos asociados a una interacción activa.
    """

    CANCEL_CURRENT_ACTION = auto()
    """
    Cancelar la acción actual en curso.
    """

    # =========================================================
    # AUDIO OUTPUT / VOZ / SONIDO
    # =========================================================

    SPEAK_TEXT = auto()
    """
    Sintetizar y reproducir texto por voz.
    """

    SPEAK_SSML = auto()
    """
    Sintetizar y reproducir contenido SSML.
    """

    PLAY_SOUND = auto()
    """
    Reproducir un sonido corto o efecto.
    """

    PLAY_MUSIC = auto()
    """
    Reproducir música o audio largo.
    """

    PAUSE_AUDIO = auto()
    """
    Pausar reproducción de audio.
    """

    RESUME_AUDIO = auto()
    """
    Reanudar reproducción de audio.
    """

    STOP_AUDIO = auto()
    """
    Detener toda reproducción de audio.
    """

    SET_VOLUME = auto()
    """
    Ajustar el volumen del subsistema de audio.
    """

    MUTE_AUDIO = auto()
    """
    Silenciar salida de audio.
    """

    UNMUTE_AUDIO = auto()
    """
    Reactivar salida de audio silenciada.
    """

    # =========================================================
    # AUDIO INPUT / ESCUCHA / MICRO
    # =========================================================

    START_LISTENING = auto()
    """
    Iniciar captura o escucha activa del micrófono.
    """

    STOP_LISTENING = auto()
    """
    Detener captura o escucha activa.
    """

    PAUSE_LISTENING = auto()
    """
    Pausar temporalmente la escucha.
    """

    RESUME_LISTENING = auto()
    """
    Reanudar la escucha pausada.
    """

    ENABLE_WAKEWORD = auto()
    """
    Activar escucha de wake word.
    """

    DISABLE_WAKEWORD = auto()
    """
    Desactivar escucha de wake word.
    """

    # =========================================================
    # VISIÓN / CÁMARA / CAPTURA
    # =========================================================

    CAPTURE_IMAGE = auto()
    """
    Capturar una imagen puntual.
    """

    CAPTURE_VIDEO = auto()
    """
    Capturar un vídeo o secuencia.
    """

    START_VIDEO_STREAM = auto()
    """
    Iniciar streaming de vídeo.
    """

    STOP_VIDEO_STREAM = auto()
    """
    Detener streaming de vídeo.
    """

    SCAN_ENVIRONMENT = auto()
    """
    Realizar escaneo visual del entorno.
    """

    FOCUS_CAMERA = auto()
    """
    Ajustar el foco o apuntar cámara a un objetivo.
    """

    # =========================================================
    # SCREEN / UI / DISPLAY
    # =========================================================

    DISPLAY_TEXT = auto()
    """
    Mostrar texto en pantalla.
    """

    DISPLAY_IMAGE = auto()
    """
    Mostrar imagen en pantalla.
    """

    DISPLAY_VIDEO = auto()
    """
    Mostrar vídeo en pantalla.
    """

    DISPLAY_ANIMATION = auto()
    """
    Mostrar animación en pantalla.
    """

    DISPLAY_EMOTION = auto()
    """
    Mostrar una emoción o cara emocional en pantalla.
    """

    SHOW_NOTIFICATION = auto()
    """
    Mostrar notificación visual.
    """

    SHOW_MENU = auto()
    """
    Mostrar menú o interfaz de selección.
    """

    CLEAR_SCREEN = auto()
    """
    Limpiar contenido de pantalla.
    """

    # =========================================================
    # LEDS / LUZ / SEÑALIZACIÓN
    # =========================================================

    SET_LED_COLOR = auto()
    """
    Fijar color LED.
    """

    SET_LED_PATTERN = auto()
    """
    Aplicar patrón de iluminación.
    """

    BLINK_LED = auto()
    """
    Hacer parpadear LEDs.
    """

    TURN_OFF_LEDS = auto()
    """
    Apagar todos los LEDs.
    """

    # =========================================================
    # MOVIMIENTO / SERVOS / CUERPO
    # =========================================================

    MOVE_HEAD = auto()
    """
    Mover cabeza o conjunto equivalente.
    """

    MOVE_EYES = auto()
    """
    Mover ojos, cámaras o equivalente direccional.
    """

    MOVE_ARM = auto()
    """
    Mover brazo o actuador equivalente.
    """

    MOVE_BODY = auto()
    """
    Mover cuerpo o base.
    """

    SET_POSTURE = auto()
    """
    Configurar postura global.
    """

    RESET_POSTURE = auto()
    """
    Volver a postura neutra o base.
    """

    LOOK_AT_TARGET = auto()
    """
    Orientarse hacia un objetivo concreto.
    """

    TRACK_TARGET = auto()
    """
    Seguir dinámicamente a un objetivo.
    """

    # =========================================================
    # EXPRESIÓN / ESTADO AFECTIVO
    # =========================================================

    SET_EMOTION = auto()
    """
    Ajustar estado emocional interno o expresivo.
    """

    CLEAR_EMOTION = auto()
    """
    Limpiar o neutralizar expresión emocional activa.
    """

    PLAY_EMOTION_ANIMATION = auto()
    """
    Reproducir animación emocional.
    """

    # =========================================================
    # COGNICIÓN / INFORMACIÓN / CONTENIDO
    # =========================================================

    READ_CONTENT = auto()
    """
    Leer o extraer contenido de una fuente.
    """

    SEARCH_INFORMATION = auto()
    """
    Buscar información relevante.
    """

    SUMMARIZE_CONTENT = auto()
    """
    Resumir contenido.
    """

    TRANSLATE_CONTENT = auto()
    """
    Traducir contenido.
    """

    STORE_MEMORY = auto()
    """
    Guardar información en memoria o contexto persistente.
    """

    RECALL_MEMORY = auto()
    """
    Recuperar información de memoria.
    """

    # =========================================================
    # SISTEMA / INTEGRACIÓN / NOTIFICACIONES
    # =========================================================

    SEND_NOTIFICATION = auto()
    """
    Enviar notificación a sistema externo o usuario.
    """

    LOG_EVENT = auto()
    """
    Registrar evento o acción en sistema de logs.
    """

    TRIGGER_WORKFLOW = auto()
    """
    Lanzar flujo interno o pipeline externo.
    """


@dataclass(slots=True)
class ActionIntent:
    """
    Intención ejecutable por la capa action.

    Attributes
    ----------
    intent_type : ActionIntentType
        Tipo de intención.
    payload : dict[str, Any]
        Parámetros asociados a la intención.
    description : str
        Descripción legible de la intención.
    source : str
        Fuente lógica que origina la intención.
    correlation_id : str | None
        Identificador de correlación para trazabilidad.
    priority : int
        Prioridad local de ejecución de la intención.
    """

    intent_type: ActionIntentType
    payload: dict[str, Any] = field(default_factory=dict)
    description: str = ""
    source: str = "application"
    correlation_id: str | None = None
    priority: int = 0