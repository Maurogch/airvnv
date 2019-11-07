from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ciuadad'
        verbose_name_plural = 'Ciudades'


class Host(User):
    pass

    class Meta:
        verbose_name = 'Anfitrion'
        verbose_name_plural = 'Anfitriones'


class Property(models.Model):
    title = models.fields.CharField(blank=False, max_length=255)
    description = models.fields.TextField(blank=False)
    max_guests = models.fields.IntegerField(blank=False)
    # How to set imagefiled: https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
    img = models.ImageField(upload_to='static/reting/images')
    price = models.fields.DecimalField(max_digits=8, decimal_places=2)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    host = models.ForeignKey(Host, on_delete=models.PROTECT)
    # There is an implicit list of RentDate here, accessed with rentdate_set

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    def __str__(self):
        return self.title


class Reservation(models.Model):
    number = models.fields.IntegerField(unique=True)
    guestName = models.fields.CharField(max_length=120)
    guestEmail = models.fields.EmailField(max_length=80)
    total = models.fields.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return self.number

    # Get price of property by getting property from first property in array of rentdate
    # Then multiply that price by the lenght of the array of rentdate
    def calc_total(self):
        self.total = self.rentdate_set[0].property.price * self.rentdate_set.count()
        return self.total


class RentDate(models.Model):
    date = models.fields.DateField(blank=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT, null=True, blank=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False)

    def __str__(self):
        return self.date
