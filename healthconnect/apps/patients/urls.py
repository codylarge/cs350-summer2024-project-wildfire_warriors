from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('medical-history/', views.medical_history, name='medical_history'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('select-doctor/', views.select_doctor, name='select_doctor'),
    path('patient_services/', views.patient_services, name='patient_services'),
]