from django.shortcuts import render, redirect
from .models import ConferenceRoom

# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'base.html')


class AddRoomView(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        name = request.POST.get('room-name')
        capacity = request.POST.get('capacity')
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get('projector') == 'on'

        if not name:
            return render(request, 'add_room.html', context={'error': 'Room name not added'})
        if capacity <= 0:
            return render(request, 'add_room.html', context={'error': 'Capacity number need to be positive'})
        if ConferenceRoom.objects.filter(name=name).first():
            return render(request, 'add_room.html', context={'error': "This room name already exists"})

        ConferenceRoom.objects.create(name=name, capacity=capacity, projector_availability=projector)
        return redirect('room-list')
