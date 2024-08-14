from django.db import models
from apps.accounts.models import CustomUser
from apps.doctors.models import Doctor
from django.utils import timezone

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    medical_history = models.ManyToManyField('MedicalRecord', blank=True, related_name='patients')
    primary_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='patients')
    prescriptions = models.ManyToManyField('pharmacists.Prescription', blank=True, related_name='patients')
    
    def __str__(self):
        return self.user.username
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    condition = models.CharField(max_length=255)
    date = models.DateField()
    prescription = models.TextField()
    remedy = models.TextField()

    def __str__(self):
        return f"{self.condition} on {self.date}"
