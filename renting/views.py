from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from .models import *
import random
import re


def index(request):
    properties = Property.objects.all()
    cities = City.objects.all()
    return render(request, 'renting/index.html', {'properties': properties}, {'cities': cities})


def single_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    message = ''
    total = 0
    post = False  # Set flag for loading modal window in template
    if request.method == 'POST':
        post = True

        name = request.POST['name']
        email = request.POST['email']
        guests = request.POST['guests']
        rent_dates_id = request.POST.getlist('rent_dates[]')  # get array from Form
        if not check_email(email):
            message = 'Email no válido'
        else:
            if name != '' and email != '' and guests != '0' and len(rent_dates_id) != 0:
                total = property.price * len(rent_dates_id)
                reservation = Reservation(
                    number=random.randint(1000, 10000),
                    guestName=name,
                    guestEmail=email,
                    guests=guests,
                    total=total
                )

                reservation.save()  # ORM save sets id in object

                for rent_date_id in rent_dates_id:  # Set this reservation to rent_dates selected
                    rent_date = RentDate.objects.get(pk=rent_date_id)
                    setattr(rent_date, 'reservation', reservation)  # sets attribute to object
                    rent_date.save()
                message = 'Reserva hecha con exito, Huespedes: %s, Días: ' \
                          '%d, Total: $%d' % (guests, len(rent_dates_id), total)
            else:
                message = 'Campos incompletos'

    rent_dates = RentDate.objects.filter(reservation=None)  # Return only dates without reservation
    max_guests = range(1, property.max_guests)  # imitate a 'while loop' in template
    return render(request, 'renting/property.html', {
        'property': property,
        'rent_dates': rent_dates,
        'message': message,
        'max_guests': max_guests,
        'post': post,
        'total': total
    })


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


def check_email(email):
    match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I)
    if match is None:
        return False
    else:
        return True


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
