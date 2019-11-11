from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from .models import *


def index(request):
    properties = Property.objects.all()
    cities = City.objects.all()
    return render(request, 'renting/index.html', {'properties': properties}, {'cities': cities})


def single_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    return render(request, 'renting/property.html', {'property': property})


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
    return render(request, 'renting/city.html', context)


# problem: I can't send a string in urls (error). Search for a soultion
def props_by_cityname(request, city_name):
    # get city's id so I can search it in properties
    try:
        city = City.objects.get(name=city_name), city_name
    except City.DoesNotExist:
        raise Http404("La ciudad no existe")

    filtered_properties = Property.objects.filter(city_id=city.city_id)

    return render(request, 'renting/index.html', {filtered_properties: filtered_properties})


def props_by_city_id(request, city_id):
    filtered_properties = Property.objects.filter(city_id=city_id)

    return render(request, 'renting/index.html', {filtered_properties: filtered_properties})


def props_by_date_range(request, chekin, chekout):
    # not modified yet
    filtered_properties = Property.objects.filter()

    return render(request, 'renting/index.html', {filtered_properties: filtered_properties})
