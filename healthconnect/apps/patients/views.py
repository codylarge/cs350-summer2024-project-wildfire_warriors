from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def book_appointment(request):
    return render(request, 'book-appointment.html')

@login_required
def medical_record(request):
    return render(request, 'medical-record.html')

