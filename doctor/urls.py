from django.urls import path
from .views import doctor_homepage, patient_profile

urlpatterns = [
    path('doctor_homepage/', doctor_homepage, name="doctor_homepage"),
    path('visit_profile/<slug:patient_username>/',patient_profile)
]