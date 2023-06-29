from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/aj/<str:groupname>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]