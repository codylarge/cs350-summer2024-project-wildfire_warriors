from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('medical-record/', views.medical_record, name='medical_record'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('medical-records/', views.medical_record, name='view_medical_records'),
    path('medical-records/modify/<int:record_id>/', views.modify_medical_record, name='modify_medical_record'),
    path('select-doctor/', views.select_doctor, name='select_doctor'),
    path('patient_services/', views.patient_services, name='patient_services'),
]