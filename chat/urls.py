from django.urls import path

from chat.views import chatpage, chatroom
app_name = "chat"

urlpatterns=[
    path("", chatpage, name="chatpage"),
    path("<str:room>/", chatroom, name="chatroom")
]