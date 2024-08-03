from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, PatientProfile, StaffProfile
from django.core.exceptions import ValidationError

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

    # Remove the default help text for username & confirmation password 
    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''

    # Remove password security requirements (only checks for matching passwords)
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        
        return password2

    def save(self, commit=True): # Called on form submission
        user = super().save(commit=False) # Create instance of new CustomUser
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
