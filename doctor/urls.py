from django.urls import path
from .views import doctor_homepage

urlpatterns = [
    path('doctor_homepage/', doctor_homepage, name="doctor_homepage"),
]