from django.shortcuts import render

# Create your views here.

def pharmacist_services(request):
    return render(request, 'pharmacists/pharmacist_services.html')