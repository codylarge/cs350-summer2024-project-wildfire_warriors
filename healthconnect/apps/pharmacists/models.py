from django.db import models
from apps.accounts.models import CustomUser
from django.conf import settings
from apps.doctors.models import Doctor
from apps.patients.models import Patient
# Create your models here.
class Pharmacist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
class Drug(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date_prescribed = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.full_name} - {self.drug.name} ({self.amount})"
