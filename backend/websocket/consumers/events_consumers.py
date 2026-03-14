"""
events_consumers.py

Consumer WebSocket encargado de transmitir al frontend los eventos
externos o de ingesta del sistema NORA.

Este consumer debe usarse para eventos procedentes de subsistemas como
audio, visión, NFC, sensores o triggers externos, antes o al margen
de su efecto sobre la FSM.
"""

import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer


logger = logging.getLogger(__name__)


class EventConsumer(AsyncWebsocketConsumer):
    """
    Consumer WebSocket para eventos externos del sistema.

    Este consumer se suscribe al grupo de eventos externos y reenvía
    al frontend los mensajes publicados por el backend mediante
    Django Channels.
    """

    GROUP_NAME = "eventos"

    async def connect(self) -> None:
        """
        Acepta la conexión WebSocket y suscribe el cliente al grupo
        de eventos externos.

        Returns
        -------
        None
        """
        try:
            logger.info("Intentando conectar WebSocket de eventos.")

            if self.channel_layer is None:
                logger.error("channel_layer no disponible en EventConsumer.connect().")
                await self.close(code=1011)
                return

            await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
            await self.accept()

            logger.info(
                "Conexión WebSocket de eventos aceptada: channel=%s group=%s",
                self.channel_name,
                self.GROUP_NAME,
            )

        except Exception as exc:
            logger.exception("Error en EventConsumer.connect(): %s", exc)
            await self.close(code=1011)

    async def disconnect(self, close_code: int) -> None:
        """
        Elimina al cliente del grupo al cerrarse la conexión.

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
                "Conexión WebSocket de eventos cerrada: channel=%s group=%s code=%s",
                self.channel_name,
                self.GROUP_NAME,
                close_code,
            )

        except Exception as exc:
            logger.exception("Error en EventConsumer.disconnect(): %s", exc)

    async def receive(self, text_data: str) -> None:
        """
        Gestiona mensajes recibidos desde el frontend.

        Este canal está pensado principalmente como canal de salida
        desde backend hacia frontend. Los mensajes entrantes se aceptan,
        pero no alteran el estado del sistema.

        Parameters
        ----------
        text_data : str
            Mensaje textual recibido desde el cliente.

        Returns
        -------
        None
        """
        try:
            logger.info("Mensaje recibido en canal de eventos: %s", text_data)

            await self.send(
                text_data=json.dumps(
                    {
                        "type": "info",
                        "message": "Canal WebSocket de eventos en modo solo lectura.",
                    }
                )
            )

        except Exception as exc:
            logger.exception("Error en EventConsumer.receive(): %s", exc)

    async def enviar_evento_externo(self, event: dict) -> None:
        """
        Reenvía al frontend un evento externo recibido desde el channel layer.

        Este método será invocado automáticamente por Django Channels cuando
        se publique un `group_send` con `type="enviar_evento_externo"`.

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
                    "Payload inválido en EventConsumer.enviar_evento_externo(): %s",
                    event,
                )
                return

            await self.send(text_data=json.dumps(data))

            logger.info("Evento externo enviado al frontend: %s", data)

        except Exception as exc:
            logger.exception(
                "Error en EventConsumer.enviar_evento_externo(): %s",
                exc,
            )