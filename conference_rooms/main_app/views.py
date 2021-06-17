from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class AddRoom(View):
    def get(self, request):
        return render(request, 'main_app/addroom.html')

    def post(self, request):
        pass
