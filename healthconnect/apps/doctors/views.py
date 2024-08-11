from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from apps.patients.models import MedicalRecord
from apps.patients.models import Patient

# Create your views here.
def doctor_services(request):
    return render(request, 'doctor_services.html')

@login_required
def list_patients(request):
    doctor = request.user.doctor
    patients = Patient.objects.filter(primary_doctor=doctor)
    for patient in patients:
        print(f"Patient: {patient}, Username: {patient.username}")
    return render(request, 'list_patients.html', {'patients': patients})

@login_required
def update_medical_record(request, username):
    custom_user = get_object_or_404(CustomUser, username=username)
    patient = get_object_or_404(Patient, user=custom_user)

    if request.method == 'POST':
        condition = request.POST.get('condition')
        date = request.POST.get('date')
        prescription = request.POST.get('prescription')
        remedy = request.POST.get('remedy')

        # Create and save the new MedicalRecord
        new_record = MedicalRecord(
            patient=patient,
            condition=condition,
            date=date,
            prescription=prescription,
            remedy=remedy
        )
        new_record.save()

        # Optionally, you can also add it to the patient's medical_history if you use ManyToManyField
        patient.medical_history.add(new_record)

        return redirect('update_medical_record', username=username)

    medical_records = MedicalRecord.objects.filter(patient=patient)
    return render(request, 'update_records.html', {'patient': patient, 'medical_records': medical_records})