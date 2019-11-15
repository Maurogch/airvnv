from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from datetime import datetime
from .models import *
import random
import re


def index(request):
    message = ''
    properties = Property.objects.all()
    cities = City.objects.all()

    if request.method == 'POST':
        city_id = request.POST['city_id']
        checkin_date = request.POST['checkin_date']
        checkout_date = request.POST['checkout_date']
        cant_guests = request.POST['cant_guests']

        # city filter
        if city_id != '0':
            properties = Property.objects.filter(city_id=city_id)

        # pax filter
        if cant_guests != '':
            for prop in properties:
                if prop.max_guests < int(cant_guests):
                    properties = properties.exclude(pk=prop.id)

        # date filter
        if checkin_date != '' and checkout_date != '':
            # Convert date format in a format that the orm understands
            checkin_date = datetime.strptime(request.POST['checkin_date'], "%m/%d/%Y").strftime("%Y-%m-%d")
            checkout_date = datetime.strptime(request.POST['checkout_date'], "%m/%d/%Y").strftime("%Y-%m-%d")
            checkin_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
            checkout_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()

            if checkin_date >= datetime.now().date() and checkout_date >= datetime.now().date():
                for prop in properties:
                    rent_dates = RentDate.objects.filter(property=prop.id, date__gte=checkin_date, date__lte=checkout_date)
                    rent_dates = rent_dates.exclude(reservation__isnull=False)

                    if not rent_dates.exists():
                        properties = properties.exclude(pk=prop.id)
            else:
                message = "No se ha podido filtrar las propiedades. Fechas ingresadas invalidas"

        if properties.count() == 0:
            message = "No se han encontrado propiedades vacantes que cumplan con el filtro"

    return render(request, 'renting/index.html', {'properties': properties, 'cities': cities, 'message': message})


def single_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    message = ''
    comission = property.price * 8 / 100
    total_day = property.price + comission
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
                total = total_day * len(rent_dates_id)
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

    rent_dates = RentDate.objects.filter(property=property, reservation=None)  # Return only dates without reservation
    max_guests = range(1, property.max_guests + 1)  # imitate a 'while loop' in template
    return render(request, 'renting/property.html', {
        'property': property,
        'rent_dates': rent_dates,
        'message': message,
        'max_guests': max_guests,
        'post': post,
        'total': total,
        'comission': comission,
        'total_day': total_day
    })


def about(request):
    return render(request, 'renting/about.html', {})


def contact(request):
    return render(request, 'renting/contact.html', {})


def check_email(email):
    match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I)
    if match is None:
        return False
    else:
        return True
