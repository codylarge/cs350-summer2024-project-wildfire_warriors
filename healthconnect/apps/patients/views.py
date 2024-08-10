from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicalRecord   
from .forms import MedicalRecordForm

# Create your views here.
@login_required
def book_appointment(request):
    return render(request, 'book-appointment.html')

@login_required
def medical_record(request):
    return render(request, 'medical-record.html')

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
