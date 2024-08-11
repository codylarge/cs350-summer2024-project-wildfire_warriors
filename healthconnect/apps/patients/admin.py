from django.contrib import admin
from .models import Patient, MedicalRecord

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalRecord)