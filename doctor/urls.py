from django.urls import path
from .views import doctor_homepage, patient_profile, request_appointment_page, send_request, appointments_page, accept_appointment

urlpatterns = [
    path('doctor_homepage/', doctor_homepage, name="doctor_homepage"),
    path('visit_profile/<slug:patient_username>/',patient_profile),
    path('request_appointment/', request_appointment_page, name="appointment"),
    path('send_request/', send_request),
    path('appointments/', appointments_page, name="doctor_appointments"),
    path('accept_appointment/<int:patient_id>/<int:requested_appointment_id>/', accept_appointment)
]