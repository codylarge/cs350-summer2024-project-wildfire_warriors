from django.shortcuts import render

# Create your views here.
def nurse_services(request):
    return render(request, 'nurses/nurse_services.html')