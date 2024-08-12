from django.contrib import admin
from .models import Pharmacist, Drug, Prescription

admin.site.register(Pharmacist)
admin.site.register(Drug)
admin.site.register(Prescription)