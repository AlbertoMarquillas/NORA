from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EventoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "mensaje": "Conexión WebSocket establecida correctamente."
        }))
        await self.channel_layer.group_add("eventos", self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        print("Mensaje recibido desde el frontend:", text_data)
        await self.send(text_data=json.dumps({
            "respuesta": "Mensaje recibido."
        }))

    async def receive_json(self, content):
        # Puedes ampliar esta lógica si quieres recibir eventos desde el front por WebSocket
        print("Mensaje recibido por WebSocket:", content)

    async def enviar_evento_fsm(self, event):
        await self.send_json(event["data"])