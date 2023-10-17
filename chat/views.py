from django.shortcuts import render

# Create your views here.

def chatpage(request):
    username = request.user.username
    return render(request,"chat/chatpage.html", context={"msg":"ChatPageRoom!", 'username':username})

def chatroom(request, room):
    return render(request, "chat/chatpage2.html", context={"msg":room})