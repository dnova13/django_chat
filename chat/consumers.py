from channels.generic.websocket import AsyncWebsocketConsumer
import json

""" 
비동기식으로 변경

사실, 기존의 동기방식은 비동기 방식에 비해, I/O가 끝날때까지 
계속 기다려야 하므로 비효율 적이라는 단점이 존재한다.

하지만, 비동기로 작성하는 경우 I/O가 끝나지 않아도 즉시 결과값이 리턴된다.
따라서, I/O과 완료되면 완료된거에 따른 콜백함수가 호출되는 방식으로 진행된다.
때문에, 계속 다른일을 할 수 있어서 더 효율적이게 된다.

"""


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
