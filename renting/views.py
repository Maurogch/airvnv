from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from .models import *


def index(request):
    return HttpResponse("Hello world, from default view index")


def city1(request, city_id):
    try:
        response = "You are looking at city: {0} id: {1}".format(City.objects.get(pk=city_id), city_id)
    except City.DoesNotExist:
        raise Http404("La ciudad no existe")
    return HttpResponse(response)


def city(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, 'renting/detail.html', {'city': city})


def citys(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'renting/index.html', context)


def register_property(request):
    cities = City.objects.all()
    return render(request, 'renting/register-property.html', {'cities': cities})


# def saveProperty(request):