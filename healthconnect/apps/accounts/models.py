from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20)
    birthdate = models.DateField(null=True, blank=True)

class StaffProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class MedicalRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=255)
    remedy = models.CharField(max_length=255)
    prescription = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.condition}"