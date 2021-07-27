from django.contrib import admin
from django.urls import path, re_path

from main_app.views import HomePage, AddRoom, ShowRooms, DeleteRoom, EditRoom, BookTheRoom, RoomDetails, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^home/?$', HomePage.as_view()),
    re_path(r'^room/new/?$', AddRoom.as_view(), name="add_room"),
    re_path(r'^room/?$', ShowRooms.as_view(), name="show_rooms"),
    re_path(r'^room/delete/(?P<id_room>\d+)/?$', DeleteRoom.as_view(), name="delete_room"),
    re_path(r'^room/modify/(?P<id_room>\d+)/?$', EditRoom.as_view(), name="edit_room"),
    re_path(r'^room/reserve/(?P<id_room>\d+)/?$', BookTheRoom.as_view(), name="book_room"),
    re_path(r'^room/(?P<id_room>\d+)/?$', RoomDetails.as_view(), name="room_details"),
    re_path(r'^room/search/?$', SearchView.as_view(), name="room-list"),
]
