from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('medical-record/', views.medical_record, name='medical_record'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('medical-records/', views.view_medical_records, name='view_medical_records'),
    path('medical-records/modify/<int:record_id>/', views.modify_medical_record, name='modify_medical_record'),
    path('medical-records/modify/', views.modify_medical_record, name='add_medical_record'),
]