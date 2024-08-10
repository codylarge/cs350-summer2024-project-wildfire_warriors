from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('medical-record/', views.medical_record, name='medical-record'),
    path('book-appointment/', views.book_appointment, name='book-appointment'),
]