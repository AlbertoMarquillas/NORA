"""
fsm_consumers.py

Consumer WebSocket encargado de transmitir al frontend las actualizaciones
de la máquina de estados finita (FSM) del sistema NORA.

Este consumer debe utilizarse para cambios de estado, transiciones,
eventos internos de la FSM, errores del núcleo de control y otra
información asociada al runtime interno del sistema.
"""

import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer


logger = logging.getLogger(__name__)


class FSMConsumer(AsyncWebsocketConsumer):
    """
    Consumer WebSocket para actualizaciones internas de la FSM.

    Este consumer se suscribe al grupo de actualizaciones FSM y reenvía
    al frontend los mensajes publicados por el backend mediante
    Django Channels.
    """

    GROUP_NAME = "fsm_updates"

    async def connect(self) -> None:
        """
        Acepta la conexión WebSocket y suscribe el cliente al grupo
        de actualizaciones FSM.

        Returns
        -------
        None
        """
        try:
            logger.info("Intentando conectar WebSocket de FSM.")

            if self.channel_layer is None:
                logger.error("channel_layer no disponible en FSMConsumer.connect().")
                await self.close(code=1011)
                return

            await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
            await self.accept()

            logger.info(
                "Conexión WebSocket FSM aceptada: channel=%s group=%s",
                self.channel_name,
                self.GROUP_NAME,
            )

        except Exception as exc:
            logger.exception("Error en FSMConsumer.connect(): %s", exc)
            await self.close(code=1011)

    async def disconnect(self, close_code: int) -> None:
        """
        Elimina al cliente del grupo FSM al cerrarse la conexión.

        Parameters
        ----------
        close_code : int
            Código de cierre de la conexión.

        Returns
        -------
        None
        """
        try:
            if self.channel_layer is not None:
                await self.channel_layer.group_discard(
                    self.GROUP_NAME,
                    self.channel_name,
                )

            logger.info(
                "Conexión WebSocket FSM cerrada: channel=%s group=%s code=%s",
                self.channel_name,
                self.GROUP_NAME,
                close_code,
            )

        except Exception as exc:
            logger.exception("Error en FSMConsumer.disconnect(): %s", exc)

    async def receive(self, text_data: str) -> None:
        """
        Gestiona mensajes recibidos desde el frontend.

        En la versión actual este canal está diseñado como canal
        de observación del estado FSM, por lo que los mensajes del
        cliente no modifican directamente la máquina de estados.

        Parameters
        ----------
        text_data : str
            Mensaje textual recibido desde el cliente.

        Returns
        -------
        None
        """
        try:
            logger.info("Mensaje recibido en canal FSM: %s", text_data)

            await self.send(
                text_data=json.dumps(
                    {
                        "type": "info",
                        "message": "Canal WebSocket FSM en modo solo lectura.",
                    }
                )
            )

        except Exception as exc:
            logger.exception("Error en FSMConsumer.receive(): %s", exc)

    async def enviar_evento_fsm(self, event: dict) -> None:
        """
        Reenvía al frontend una actualización FSM recibida desde el channel layer.

        Este método será invocado automáticamente por Django Channels cuando
        se publique un `group_send` con `type="enviar_evento_fsm"`.

        Parameters
        ----------
        event : dict
            Evento recibido desde el grupo de Channels. Se espera que
            contenga una clave `data` con un diccionario serializable a JSON.

        Returns
        -------
        None
        """
        try:
            data = event.get("data", {})

            if not isinstance(data, dict):
                logger.warning(
                    "Payload inválido en FSMConsumer.enviar_evento_fsm(): %s",
                    event,
                )
                return

            await self.send(text_data=json.dumps(data))

            logger.info("Evento FSM enviado al frontend: %s", data)

        except Exception as exc:
            logger.exception(
                "Error en FSMConsumer.enviar_evento_fsm(): %s",
                exc,
            )