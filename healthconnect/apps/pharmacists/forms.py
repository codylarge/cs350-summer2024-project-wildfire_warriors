from django import forms
from .models import Prescription

class PrescriptionFillForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['is_approved']
        widgets = {
            'is_approved': forms.CheckboxInput(),
        }