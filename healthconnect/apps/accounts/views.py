from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomRegistrationForm
from .models import CustomUser, StaffProfile
from apps.patients.models import Patient
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from apps.pharmacists.models import Prescription
from apps.pharmacists.forms import PrescriptionFillForm


def register_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user using the form's save method
            role = form.cleaned_data['role']

            auth_login(request, user)
            
            # Redirect based on user role
            if role == 'patient':
                return redirect('select_doctor')
            else:
                return redirect('home')
    else:
        form = CustomRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def forgot_password_view(request):
    # Logic for forgot password
    return render(request, 'forgot-password.html')

def appointment_success(request):
    return render(request, 'appointment_success.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            role = request.GET.get('role', '')
            if role == 'doctor':
                return redirect('doctor_dashboard')  # Replace with actual dashboard URL
            elif role == 'patient':
                return redirect('patient_dashboard')  # Replace with actual dashboard URL
            elif role == 'nurse':
                return redirect('nurse_dashboard')  # Replace with actual dashboard URL
            elif role == 'pharmacist':
                return redirect('pharmacist_dashboard')  # Replace with actual dashboard URL
            return redirect('profile')  # Default redirect if no role is specified
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    user_info = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'birthdate': user.birthdate,
        'role': user.role,
    }

    if user.role == 'patient':
        try:
            patient_profile = Patient.objects.get(user=user)
            user_info['medical_history'] = patient_profile.medical_records.all()
            user_info['primary_doctor'] = patient_profile.primary_doctor
        except Patient.DoesNotExist:
            user_info['medical_history'] = 'No medical history available.'
            user_info['primary_doctor'] = 'No primary doctor assigned.'

    else:
        user_info['role'] = user.role

    return render(request, 'profile.html', {'user_info': user_info})

def get_staff_role(user):
    if user.is_doctor:
        return 'Doctor'
    elif user.is_nurse:
        return 'Nurse'
    elif user.is_pharmacist:
        return 'Pharmacist'
    return ''

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    user = request.user
    if hasattr(user, 'doctor'):
        return render(request, 'doctor_services.html')
    elif hasattr(user, 'patient'):
        return render(request, 'patient_services.html')
    elif hasattr(user, 'nurse'):
        return render(request, 'nurse_services.html')
    elif hasattr(user, 'pharmacist'):
        return render(request, 'pharmacist_services.html')
    else:
        return render(request, 'patient_services.html')

from django.utils import timezone

def pharmacy(request):
    user = request.user
    if hasattr(user, 'pharmacist'):
        prescriptions = Prescription.objects.all()
        if request.method == 'POST':
            prescription_id = request.POST.get('prescription_id')
            prescription = Prescription.objects.get(id=prescription_id)
            prescription.filled = 'filled' in request.POST
            if prescription.filled:
                prescription.last_filled = timezone.now()
            else:
                prescription.last_filled = None
            prescription.save()
        return render(request, 'pharmacist_pharmacy.html', {'prescriptions': prescriptions})
    elif hasattr(user, 'patient'):
        prescriptions = Prescription.objects.filter(patient=user.patient)
        if request.method == 'POST' and 'request_refill' in request.POST:
            prescription_id = request.POST.get('prescription_id')
            prescription = Prescription.objects.get(id=prescription_id)
            prescription.filled = False
            prescription.save()
        return render(request, 'patient_pharmacy.html', {'prescriptions': prescriptions})
    elif hasattr(user, 'doctor'):
        prescriptions = Prescription.objects.select_related('patient', 'drug').all()
        return render(request, 'doctor_pharmacy.html', {'prescriptions': prescriptions})
    elif hasattr(user, 'nurse'):
        prescriptions = Prescription.objects.select_related('patient', 'drug').all()
        return render(request, 'nurse_pharmacy.html', {'prescriptions': prescriptions})
    else:
        return render(request, 'patient_pharmacy.html')