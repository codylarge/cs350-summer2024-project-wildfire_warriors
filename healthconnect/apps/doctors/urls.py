from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('doctor_services/', views.doctor_services, name='doctor_services'),
    path('list_patients/', views.list_patients, name='list_patients'),
    path('update_records/<str:username>/', views.update_medical_record, name='update_medical_record'),
    path('request_prescription/<str:patient_username>/', views.request_prescription, name='request_prescription'),
    path('list_patients_prescription/', views.list_patients_prescription, name='list_patients_prescription'),
    path('manage-appointments/', views.manage_appointments, name='manage_appointments'),

]