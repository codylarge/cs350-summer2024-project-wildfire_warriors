from django import forms
from apps.pharmacists.models import Prescription, Drug

class PrescriptionForm(forms.ModelForm):
    drug = forms.ModelChoiceField(queryset=Drug.objects.all(), label="Select Drug")
    amount = forms.IntegerField(min_value=1, label="Amount")

    class Meta:
        model = Prescription
        fields = ['drug', 'amount']
