from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, PatientProfile, StaffProfile
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=[('patient', 'Patient'), ('doctor', 'Doctor'), ('nurse', 'Nurse'), ('pharmacist', 'Pharmacist')],
        required=True,
        label="Role"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']
        
        if role == 'patient':
            user.is_patient = True
        elif role == 'doctor':
            user.is_doctor = True
        elif role == 'nurse':
            user.is_nurse = True
        elif role == 'pharmacist':
            user.is_pharmacist = True
        
        if commit:
            user.save()
        
        return user

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('medical_history',)

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ('role',)
