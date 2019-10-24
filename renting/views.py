from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return HttpResponse("Hello world, from default view index")


def city(request, city_id):
    response = "You are looking at city: {0} id: {1}".format(City.objects.get(pk=city_id), city_id)
    return HttpResponse(response)
