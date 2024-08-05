from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PatientProfile, StaffProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_patient', 'is_doctor', 'is_nurse', 'is_pharmacist')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PatientProfile)
admin.site.register(StaffProfile)
#admin