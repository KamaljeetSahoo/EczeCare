from django.urls import path
from .views import doctor_homepage, patient_profile, request_appointment_page, send_request

urlpatterns = [
    path('doctor_homepage/', doctor_homepage, name="doctor_homepage"),
    path('visit_profile/<slug:patient_username>/',patient_profile),
    path('request_appointment/', request_appointment_page, name="appointment"),
    path('send_request/', send_request)
]