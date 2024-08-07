from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, StaffProfile, MedicalRecord
from apps.patients.models import PatientProfile
from django.core.exceptions import ValidationError
from django.utils import timezone

from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birthdate = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=[('patient', 'Patient'), ('doctor', 'Doctor'), ('nurse', 'Nurse'), ('pharmacist', 'Pharmacist')],
        required=True,
        label="Role"
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birthdate', 'username', 'email', 'password1', 'password2', 'role']

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
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthdate = self.cleaned_data['birthdate']
        user.is_active = True  # Default field from the AbstractUser class
        user.date_joined = timezone.now()  # Default field from the AbstractUser class

        role = self.cleaned_data['role']
        
        if role == 'patient':
            user.is_staff = False # Default field from the AbstractUser class
        elif role in ['doctor', 'nurse', 'pharmacist']:
            user.is_staff = True
        else:
            raise ValidationError("Invalid role.")
    
        if commit:
            user.save()
        
        return user

'''
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('medical_history',)

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ('role',)
'''

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['date', 'condition', 'remedy', 'prescription']