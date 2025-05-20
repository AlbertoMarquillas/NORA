from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("fsm_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("fsm_updates", self.channel_name)

    async def receive(self, text_data):
        # Si quieres permitir que el frontend envíe datos también, lo puedes procesar aquí
        pass

    async def send_fsm_event(self, event):
        await self.send(text_data=json.dumps(event["content"]))