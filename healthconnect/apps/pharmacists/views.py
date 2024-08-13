from django.shortcuts import render, redirect
from .models import Prescription

# Create your views here.

def pharmacist_services(request):
    return render(request, 'pharmacist_services.html')

def review_prescriptions(request):
    # Fetch all prescriptions that have not been approved yet
    prescriptions = Prescription.objects.filter(is_approved=False)
    
    if request.method == 'POST':
        # Get the prescription ID from the POST request
        prescription_id = request.POST.get('prescription_id')
        # Fetch the prescription and update the approval status
        prescription = Prescription.objects.get(id=prescription_id)
        prescription.is_approved = True
        prescription.save()
        # Redirect back to the review page after approval
        return redirect('review_prescriptions')
    
    return render(request, 'review_prescriptions.html', {'prescriptions': prescriptions})