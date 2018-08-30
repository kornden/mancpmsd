from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cpmsdblog'),
    path('doctors', views.doctors, name='doctors'),
    path('units', views.units, name='units'),
    path('freedrugs', views.freedrugs, name='freedrugs'),
    
]
