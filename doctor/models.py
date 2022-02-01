from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DoctorProfile(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patients = models.ManyToManyField(User, related_name = 'patients')

    def __str__(self):
        return str(self.doctor.username)