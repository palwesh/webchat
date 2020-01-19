import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
# from .models import Thread, ChastMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("conected". event)
        await self.send({
            "type":"websocket.accept"
        })
        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
  
        thread_obj = await self.get_thread(me, other_user)
        self.thread_obj = await self.get_thread(me, other_user)
        chat_room = f"thread_{thread_obj.id}"
        self.chat_room = chat_room

        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
       



    async def websocket_receive(self, event):
        print("recive". event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dist_data = json.loads(front_text)
            msg = loaded_dist_data.get('message')
            print(msg)
             
            user = self.scope['user']
            username = 'default'
            if user.is_authenticated:
                username = user.username
            myResponse = {
                'message': msg,
                'username': username
            }

            await self.create_chat_thread(user, msg)
           

            await self.channel_layer.group_send(
                self.chat_room,
                {
                    'type':'chat_message',
                    'text': json.dumps(myResponse)
                }
            )

            # await self.send({
            #     "type": "websocket.send",
            #     "text": json.dumps(myResponse)
            # })

    async def chat_message(self, event):
        print('messafe', event)
        await self.send({
            "type": "websocket.send",
            "text": event['text']

        })

    async def websocket_disconnected(self, event):
        print("disconnected". event)


    @database_sync_to_async
    def get_thread(self, user, other_user):
        return Thread.objects.get_or_new(user, other_user)[0]



    @database_sync_to_async
    def create_chat_thread(self, me, msg):
        thread_obj = self.thread_obj
        me  =  self.scope['user']
        return ChatMessage.objects.create(thread=thread_obj, user=me, message=msg)


    