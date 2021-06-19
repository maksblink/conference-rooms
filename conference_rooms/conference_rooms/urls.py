"""conference_rooms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from main_app.views import HomePage, AddRoom, ShowRooms, DeleteRoom, EditRoom, BookTheRoom, RoomDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^home/?$', HomePage.as_view()),
    re_path(r'^room/new/?$', AddRoom.as_view(), name="add_room"),
    re_path(r'^room/?$', ShowRooms.as_view(), name="show_rooms"),
    re_path(r'^room/delete/(?P<id_room>\d+)/?$', DeleteRoom.as_view(), name="delete_room"),
    re_path(r'^room/modify/(?P<id_room>\d+)/?$', EditRoom.as_view(), name="edit_room"),
    re_path(r'^room/reserve/(?P<id_room>\d+)/?$', BookTheRoom.as_view(), name="book_room"),
    re_path(r'^room/(?P<id_room>\d+)/?$', RoomDetails.as_view(), name="room_details"),
]
