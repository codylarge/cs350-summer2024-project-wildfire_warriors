from django.db import models
from apps.accounts.models import CustomUser
from apps.doctors.models import Doctor
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    medical_history = models.TextField(blank=True)
    primary_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='patients')


    def __str__(self):
        return self.user.username
    
class MedicalRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    condition = models.CharField(max_length=255)
    remedy = models.CharField(max_length=255)
    prescription = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.condition}"