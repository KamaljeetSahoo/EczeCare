from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DoctorProfile(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)