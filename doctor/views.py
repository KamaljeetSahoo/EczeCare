from tkinter import E
from django.shortcuts import redirect, render
from .models import DoctorProfile
from eczema_profile.utils import poem_calc_db
from Insights.views import find_count_trigger_items

Blood_group = ['A+','A-','B+','B-','O+','O-','AB+','AB-']
age_group = [25,15,18,20,35,45,16,27]
def give_age_Bg(n):
    age = []
    Bg = []
    for i in range(0,n):
        if i>7:
            Bg.append(Blood_group[i-8])
            age.append(age[i-8])
        else:
           Bg.append(Blood_group[i]) 
           age.append(age_group[i])
    return Bg,age

# Create your views here.
def doctor_homepage(request):
    if request.user.is_authenticated:
        if 'doctor' in request.user.username.lower():
            patients = list(request.user.doctorprofile_set.all()[0].patients.all())
            #peom_score, age, blood_group, most_common_trigger
            bg, age = give_age_Bg(len(patients))
            patient_details = {}
            for i in range(len(patients)):
                triggers = find_count_trigger_items(patients[i].trigger_set.all())
                if len(triggers[0]) != 0:
                    trigger = triggers[0][0]
                else:
                    trigger = "No Triggers Found"
                if len(list(patients[i].poemscore_set.all())) != 0:
                    poem_score = poem_calc_db(list(patients[i].poemscore_set.all())[-1])
                else:
                    poem_score = 'None'
                patient_details[i] = {
                    'patient': patients[i],
                    'poem_score': poem_score,
                    'age' : age[i],
                    'blood_group': bg[i],
                    'most_common_trigger': trigger
                }
            c = {
                'patient_details': patient_details
            }
            return render(request, 'doctor/doctor_homepage.html', context=c)
        else:
            return redirect("home")
    else:
        return redirect('login')