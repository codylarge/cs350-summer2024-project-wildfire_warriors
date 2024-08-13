from django.shortcuts import render

# Create your views here.
def nurse_services(request):
    return render(request, 'nurse_services.html')