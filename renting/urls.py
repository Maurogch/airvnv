from django.urls import path
from . import views


app_name = 'renting'
urlpatterns = [
    path('', views.index, name='index'),
    path('property/<int:property_id>', views.single_property, name='single_property'),
    path('properties/city/<int:city_id>', views.props_by_city_id, name='props_by_city_id'),
    path('city/<int:city_id>', views.city, name='city'),
    path('city/', views.citys, name='city')

]
