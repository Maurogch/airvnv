from django.contrib import admin
from .models import City, Host, Property, Reservation, RentDate


class HostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')


# Register your models here.
admin.site.register(City)
admin.site.register(Host)
admin.site.register(Property)
admin.site.register(RentDate)
admin.site.register(Reservation)




