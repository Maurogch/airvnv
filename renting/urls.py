from django.urls import path
from . import views


app_name = 'renting'
urlpatterns = [
    path('', views.index, name='index'),
    path('property/<int:property_id>', views.single_property, name='single_property'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')

]
