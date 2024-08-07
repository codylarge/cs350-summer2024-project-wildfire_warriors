# When a CustomUser instance is saved, the post_save signal is triggered. The create_user_profile function checks if the user was newly created (created is True) 
# and then creates the appropriate profile based on the user's role.

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, StaffProfile
from apps.patients.models import Patient
from apps.doctors.models import Doctor
from apps.nurses.models import Nurse
from apps.pharmacists.models import Pharmacist



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        role = instance.role
        if role == 'patient':
            Patient.objects.create(user=instance)
        elif role == 'doctor':
            Doctor.objects.create(user=instance)
        elif role == 'nurse':
            Nurse.objects.create(user=instance)
        elif role == 'pharmacist':
            role = 'Pharmacist'
            Pharmacist.objects.create(user=instance)
        else:
            role = 'Unknown'
                
        #StaffProfile.objects.create(user=instance, role=role)
