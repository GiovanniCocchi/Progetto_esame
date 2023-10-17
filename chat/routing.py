from django.urls import path

from chat.consumers import WSConsumerChatChannels

ws_urlpatterns =[
    #path("ws/chatws/", WSConsumerChat.as_asgi()),
    path("ws/chatws/<str:room>/", WSConsumerChatChannels.as_asgi())
]
"""


websocket_urlpatterns=[
                    re_path(
                        r"ws/chat/(?P<chat_box_name>\w+)/$", consumers.ChatRoomConsumer.as_asgi()
                    ),
                ]

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)
"""