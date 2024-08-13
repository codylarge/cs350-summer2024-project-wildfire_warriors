from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('pharmacist_services/', views.pharmacist_services, name='pharmacist_services'),
    path('prescriptions/', views.review_prescriptions, name='review_prescriptions'),
]