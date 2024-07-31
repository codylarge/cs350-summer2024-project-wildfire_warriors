from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, PatientProfileForm, StaffProfileForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user.is_patient:
                PatientProfile.objects.create(user=user)
            else:
                StaffProfile.objects.create(user=user, role=get_staff_role(user))
            login(request, user)
            return redirect('profile')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})

def profile(request):
    user = request.user
    if user.is_patient:
        profile = user.patientprofile
    else:
        profile = user.staffprofile
    return render(request, 'accounts/profile.html', {'profile': profile})

def get_staff_role(user):
    if user.is_doctor:
        return 'Doctor'
    elif user.is_nurse:
        return 'Nurse'
    elif user.is_pharmacist:
        return 'Pharmacist'
    return ''
