from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, StaffProfile
from apps.patients.models import Patient 

admin.site.register(CustomUser)
admin.site.register(StaffProfile)
#admin