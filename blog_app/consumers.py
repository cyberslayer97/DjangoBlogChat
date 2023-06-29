from channels.generic.websocket import AsyncJsonWebsocketConsumer
from time import sleep
import asyncio
from author_profile.models import Author_Profile
from .models import Chat, tags
from channels.auth import get_user
# from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.groupname = self.scope['url_route']['kwargs']['groupname']
        print(self.groupname)
        self.user =await get_user(self.scope)
        print(self.user)
        print("User ID: ", self.user.id)
        print("Username: ", self.user.username)
        print("Email: ", self.user.email)

        await (self.channel_layer.group_add)(
            self.groupname,
            self.channel_name
        )

        await self.accept()
    async def receive_json(self, content, **kwargs):
        profile = await self.get_user_profile(self.user)
        await self.chat_save(content)


        await (self.channel_layer.group_send)(
            self.groupname,
            {
                'type':'chat.message',
                'message': content,
                'sender': profile
            }
        )
    
  

    async def chat_message(self, event):
        await self.send_json({'message':event['message'],'sender':event['sender']})

    
    async def disconnect(self, code):
        print('Disconnected', code)
    
    @database_sync_to_async
    def get_user_profile(self, user):
        user_profile = Author_Profile.objects.get(user=user)
        return user_profile.Profile_image.url
    
    @database_sync_to_async
    def chat_save(self, message):
        tag = tags.objects.get(tagname=self.groupname)
        chat_message = Chat(group=tag, content=message, sender=self.user.author_profile)
        chat_message.save()
      