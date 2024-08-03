# When a CustomUser instance is saved, the post_save signal is triggered. The create_user_profile function checks if the user was newly created (created is True) 
# and then creates the appropriate profile based on the user's role.

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, PatientProfile, StaffProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_patient:
            PatientProfile.objects.create(user=instance)
        elif instance.is_doctor or instance.is_nurse or instance.is_pharmacist:
            # Determine the role
            role = None
            if instance.is_doctor:
                role = 'Doctor'
            elif instance.is_nurse:
                role = 'Nurse'
            elif instance.is_pharmacist:
                role = 'Pharmacist'
                
            # Create the StaffProfile with the determined role
            StaffProfile.objects.create(user=instance, role=role)
