from django.shortcuts import render

# Create your views here.
def doctor_services(request):
    return render(request, 'doctors/doctor_services.html')