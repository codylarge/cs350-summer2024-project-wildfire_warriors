from django.db import models
from django.utils import timezone
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    scheduled_date = models.DateTimeField(default=timezone.now)
    reason = models.TextField(blank=True)
    room_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.username} for {self.patient.user.username} on {self.scheduled_date}"
