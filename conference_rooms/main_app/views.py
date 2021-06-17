from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from main_app.models import Room, Reservation
from datetime import date, datetime


class HomePage(View):
    def get(self, request):
        return render(request, 'main_app/base_template.html')


class AddRoom(View):
    def get(self, request):
        return render(request, 'main_app/add_room.html')

    def post(self, request):
        name = request.POST.get('room_name')
        try:
            room_capacity = int(request.POST.get('room_capacity'))
        except ValueError:
            return render(request, 'main_app/edit_room.html',
                          context={'errors': "Capacity of the room can not be empty!"})
        projector_room = request.POST.get('projector_room')
        rooms = Room.objects.all()
        if name == "":
            return render(request, 'main_app/add_room.html', context={'errors': "Name can not be empty!"})
        elif room_capacity < 0:
            return render(request, 'main_app/add_room.html',
                          context={'errors': "Capacity of the room can not be negative!"})
        try:
            new_room = Room.objects.create(name=name, capacity=room_capacity, projector_available=projector_room)
        except IntegrityError:
            return render(request, 'main_app/add_room.html',
                          context={'errors': "Room with this name is already exists!"})
        return HttpResponseRedirect('http://127.0.0.1:8000/home')


class ShowRooms(View):
    def get(self, request):
        rooms = Room.objects.all()
        if not rooms.first():
            return HttpResponse("No rooms available ")
        return render(request, 'main_app/show_rooms.html', context={'rooms': rooms})


class DeleteRoom(View):
    def get(self, request, id_room):
        try:
            room = Room.objects.get(id=id_room)
            room.delete()
        except ObjectDoesNotExist:
            return HttpResponse("This room is not exists!")
        return HttpResponseRedirect('http://127.0.0.1:8000/room')


class EditRoom(View):
    def get(self, request, id_room):
        try:
            room = Room.objects.get(id=id_room)
        except ObjectDoesNotExist:
            return render(request, 'main_app/edit_room.html',
                          context={'errors': "This room is not exists!"})
        return render(request, 'main_app/edit_room.html')

    def post(self, request, id_room):
        name = request.POST.get('room_name')
        try:
            room_capacity = int(request.POST.get('room_capacity'))
        except ValueError:
            return render(request, 'main_app/edit_room.html',
                          context={'errors': "Capacity of the room can not be empty!"})
        projector_room = request.POST.get('projector_room')
        if name == "":
            return render(request, 'main_app/edit_room.html', context={'errors': "Name can not be empty!"})
        elif room_capacity < 0:
            return render(request, 'main_app/edit_room.html',
                          context={'errors': "Capacity of the room can not be negative!"})
        try:
            room = Room.objects.get(id=id_room)
            room.name = name
            room.capacity = room_capacity
            room.projector_available = projector_room
            try:
                room.save()
            except IntegrityError:
                return render(request, 'main_app/edit_room.html',
                              context={'errors': "Room with this name is already exists!"})
        except ObjectDoesNotExist:
            return render(request, 'main_app/edit_room.html',
                          context={'errors': "This room is not exists!"})
        return HttpResponseRedirect(reverse('show_rooms'))


class BookTheRoom(View):
    def get(self, request, id_room):
        return render(request, 'main_app/book_the_room.html')

    def post(self, request, id_room):
        comment = request.POST.get('comment')
        date = request.POST.get('book_date')
        date = datetime.strptime(date, '%Y-%m-%d')
        try:
            test_get = Reservation.objects.get(date=date, room_id=id_room)
            return render(request, 'main_app/book_the_room.html',
                          context={'errors': "This room is already booked on this date!"})
        except ObjectDoesNotExist:
            if date < datetime.now():
                print("xxxxxx")
