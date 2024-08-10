from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('doctor_services/', views.doctor_services, name='doctor_services'),
]