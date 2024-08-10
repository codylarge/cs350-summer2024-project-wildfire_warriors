from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicalRecord   
from apps.doctors.models import Doctor
from .models import Patient
from .forms import MedicalRecordForm

# Create your views here.
@login_required
def book_appointment(request):
    return render(request, 'book-appointment.html')

@login_required
def medical_record(request):
    return render(request, 'medical-record.html')

@login_required
def modify_medical_record(request, record_id=None):
    if not request.user.is_doctor and not request.user.is_nurse:
        return redirect('home')

    if record_id:
        record = get_object_or_404(MedicalRecord, id=record_id)
    else:
        record = MedicalRecord(user=request.user)

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('view_medical_records')
    else:
        form = MedicalRecordForm(instance=record)

    return render(request, 'modify_medical_record.html', {'form': form})

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

