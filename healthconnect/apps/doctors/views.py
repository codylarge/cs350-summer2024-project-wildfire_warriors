from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import CustomUser
from apps.patients.models import MedicalRecord
from datetime import datetime
from apps.patients.models import Patient
from apps.accounts.models import Appointment
from .forms import PrescriptionForm

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
def list_patients_prescription(request):
    doctor = request.user.doctor
    patients = Patient.objects.filter(primary_doctor=doctor)
    for patient in patients:
        print(f"Patient: {patient}, Username: {patient.username}")
    return render(request, 'list_patients_prescription.html', {'patients': patients})

@login_required
def manage_appointments(request):
    doctor = request.user.doctor  # Assumes user has a related Doctor profile
    appointments = Appointment.objects.filter(doctor=doctor, date__gte=datetime.now()).order_by('date')

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = get_object_or_404(Appointment, id=appointment_id, doctor=doctor)
        appointment.delete()
        messages.success(request, 'Appointment canceled successfully!')
        return redirect('manage_appointments')

    return render(request, 'manage_appointments.html', {'appointments': appointments})

@login_required
def request_prescription(request, patient_username):
    patient = get_object_or_404(Patient, user__username=patient_username)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            try:
                prescription.doctor = patient.primary_doctor
                prescription.patient = patient  # Ensure the patient field is set
                prescription.save()
            except Patient.DoesNotExist:
                print("Patient does not exist")
                pass
            prescription.save()
            return redirect('list_patients_prescription')
    else:
        form = PrescriptionForm()

    return render(request, 'request_prescription.html', {
        'patient': patient,
        'form': form,
    })


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