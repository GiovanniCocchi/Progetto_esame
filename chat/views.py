from django.shortcuts import render

# Create your views here.

def chatpage(request):
    return render(request,"chat/chatpage.html", context={"msg":"ChatPageRoom!"})

def chatroom(request, room):
    return render(request, "chat/chatpage2.html", context={"msg":room})