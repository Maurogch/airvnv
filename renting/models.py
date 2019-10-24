from django.db import models


class City(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.fields.CharField(unique=True, max_length=40)
    email = models.fields.EmailField(max_length=60)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.fields.CharField(blank=False, max_length=255)
    description = models.fields.TextField(blank=False)
    max_guests = models.fields.IntegerField(blank=False)
    # How to set imagefiled: https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
    img = models.ImageField(upload_to='imgs/properties/', height_field=400, width_field=400)
    price = models.fields.DecimalField(max_digits=8, decimal_places=2)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # RentDate list? If yes, should I elimiate the foreignkey in RentDate?

    def __str__(self):
        return self.title


class Reservation(models.Model):
    number = models.fields.IntegerField(unique=True)
    guest = models.fields.CharField(max_length=120)  # Ask for name, last name and email, should we make an object?
    property = models.ForeignKey(Property, on_delete=models.PROTECT)  # Dont delete a property if there are reservations

    def __str__(self):
        return self.number


class RentDate(models.Model):
    date = models.fields.DateField(blank=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT, null=True, blank=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False)

    def __str__(self):
        return self.date