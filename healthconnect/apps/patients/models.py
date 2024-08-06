from django.db import models
from apps.accounts.models import CustomUser

# Create your models here.


class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.user.username