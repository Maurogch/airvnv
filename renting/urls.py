from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'renting'
urlpatterns = [
    path('', views.index, name='index'),
    path('city/<int:city_id>', views.city, name='city'),
    path('city/', views.citys, name='city'),
    path('properties/<int:city_id>', views.props_by_city_id, name='properties')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

