from django.db import models
from apps.accounts.models import CustomUser

# Create your models here.

class Nurse (models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username