from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomRegistrationForm, MedicalRecordForm
from .models import CustomUser, StaffProfile, MedicalRecord
from apps.patients.models import PatientProfile
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegistrationForm()

    return render(request, 'register.html', {'form': form})

def forgot_password_view(request):
    # Logic for forgot password
    return render(request, 'forgot-password.html')


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
    }

    if user.role == 'patient':
        try:
            patient_profile = PatientProfile.objects.get(user=user)
            user_info['medical_history'] = patient_profile.medical_history
        except PatientProfile.DoesNotExist:
            user_info['medical_history'] = 'No medical history available.'

    else:
        try:
            staff_profile = StaffProfile.objects.get(user=user)
            user_info['role'] = staff_profile.role
        except StaffProfile.DoesNotExist:
            user_info['role'] = 'No role available.'

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
    return render(request, 'services.html')

def pharmacy(request):
    return render(request, 'pharmacy.html')

@login_required
def view_medical_records(request):
    records = MedicalRecord.objects.filter(user=request.user)
    return render(request, 'view_medical_records.html', {'records': records})

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