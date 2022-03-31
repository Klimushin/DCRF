from django.urls import path

from chat.consumers import UserConsumer, RoomConsumer

websocket_urlpatterns = [
    path('ws/', UserConsumer.as_asgi()),
    path('ws/chat/', RoomConsumer.as_asgi()),
]
