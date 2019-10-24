from django.urls import path
from . import views


app_name = 'renting'
urlpatterns = [
    path('', views.index, name='index'),
    path('city/<int:city_id>', views.city, name='city'),
    path('city/', views.citys, name='city'),
    path('registerProperty/', views.register_property, name='registerProperty'),
]