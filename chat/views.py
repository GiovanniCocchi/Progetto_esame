from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def chatpage(request):
    username = request.user.username
    return render(request,"chat/chatpage.html", context={"msg":"ChatPageRoom!", 'username':username})

@login_required
def chatroom(request, room):
    username= request.user.username
    return render(request, "chat/chatpage2.html", context={"msg":room,'username':username})