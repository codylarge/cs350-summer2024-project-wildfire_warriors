from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, PatientProfile, StaffProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'is_patient', 'is_doctor', 'is_nurse', 'is_pharmacist')

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('medical_history',)

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ('role',)
