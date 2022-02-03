from pydoc import Doc
from django.contrib import admin
from .models import DoctorProfile, Appointment, RequestAppointment
# Register your models here.

admin.site.register(DoctorProfile)
admin.site.register(Appointment)
admin.site.register(RequestAppointment)