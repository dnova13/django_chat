from django.urls import re_path

from . import consumers

# update 로 인한 수정
# consumers.ChatConsumer => consumers.ChatConsumer.as_asgi() 로
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
