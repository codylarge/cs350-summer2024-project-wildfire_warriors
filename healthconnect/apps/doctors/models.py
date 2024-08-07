from django.db import models
from apps.accounts.models import CustomUser

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username