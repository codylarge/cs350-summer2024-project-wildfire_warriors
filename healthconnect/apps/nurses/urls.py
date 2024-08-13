from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('nurse_services/', views.nurse_services, name='nurse_services'),
]