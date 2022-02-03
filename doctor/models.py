from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_status = models.BooleanField(default=True)

class RequestAppointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    request_status = models.BooleanField(default = False)

class DoctorProfile(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patients = models.ManyToManyField(User, related_name = 'patients')
    appointments = models.ManyToManyField(Appointment)

    def __str__(self):
        return str(self.doctor.username)