from django.db import models
from apps.accounts.models import CustomUser
from apps.doctors.models import Doctor

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    medical_history = models.TextField(blank=True)
    primary_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='patients')


    def __str__(self):
        return self.user.username