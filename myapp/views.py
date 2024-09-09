from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def room(request, roomName):
    return render(request, 'room.html', {'roomName': roomName})