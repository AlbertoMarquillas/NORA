from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EventoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("eventos", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("eventos", self.channel_name)

    async def enviar_evento(self, event):
        await self.send(text_data=json.dumps(event["data"]))
