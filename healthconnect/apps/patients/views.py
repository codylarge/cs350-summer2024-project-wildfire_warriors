from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicalRecord   
from apps.doctors.models import Doctor
from .models import Patient
from apps.accounts.models import CustomUser


# NOT @login required, this will be allowed by all and a request to login will be made when user selects a service
def patient_services(request):
    custom_user = get_object_or_404(CustomUser, username=request.user.username)
    patient = get_object_or_404(Patient, user=custom_user)
    print("testing patient_services")
    print(f"Patient Username: {patient.user.username}")
    
    return render(request, 'select_doctor.html', {'patient': patient})
    
# Create your views here.
@login_required
def book_appointment(request):
    return render(request, 'book-appointment.html')

@login_required
def medical_history(request):
    current_user = request.user
    patient = get_object_or_404(Patient, user=current_user)
    records = MedicalRecord.objects.filter(patient=patient)
    print(f"Patient Username: {patient.user.username}")
    return render(request, 'medical-history.html', {'records': records})

@login_required
def select_doctor(request):
    doctors = Doctor.objects.filter(accepting_new_patients=True)
    
    if request.method == 'POST':
        selected_doctor_user_id = request.POST.get('doctor_id')
        selected_doctor = Doctor.objects.get(user_id=selected_doctor_user_id)
        
        # Assign the selected doctor to the patient's profile
        patient_profile = Patient.objects.get(user=request.user)
        patient_profile.primary_doctor = selected_doctor
        patient_profile.save()
        
        # Redirect to a success page or patient's profile page
        return redirect('profile')
    
    return render(request, 'select_doctor.html', {'doctors': doctors})

