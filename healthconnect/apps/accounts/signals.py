# When a CustomUser instance is saved, the post_save signal is triggered. The create_user_profile function checks if the user was newly created (created is True) 
# and then creates the appropriate profile based on the user's role.

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, StaffProfile
from apps.patients.models import PatientProfile



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        role = instance.role
        if role == 'patient':
            PatientProfile.objects.create(user=instance)
        elif role == 'doctor':
            role = 'Doctor'
        elif role == 'nurse':
            role = 'Nurse'
        elif role == 'pharmacist':
            role = 'Pharmacist'
        else:
            role = 'Unknown'
                
        StaffProfile.objects.create(user=instance, role=role)
