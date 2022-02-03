from django.shortcuts import redirect, render
from eczema_profile.utils import poem_calc_db
from Insights.views import find_count_trigger_items
import json
from django.contrib.auth.models import User
from .models import RequestAppointment, Appointment

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

def patient_profile(request, patient_username):
    print(patient_username)
    if request.user.is_authenticated:
        if 'doctor' in request.user.username.lower():
            user = User.objects.get(username = patient_username)
            poemscore = list(user.poemscore_set.all())
            p = []
            sleepscore = []
            for score in poemscore:
            
                sleepscore.append(abs(getattr(score,'q2')-4))
                p.append(poem_calc_db(score))
            
            triggers = list(user.trigger_set.all())
            
            triggers_x,triggers_y = find_count_trigger_items(triggers)
            print(triggers_x,triggers_y)
            #Image fetch from db
            images, masks = [], []
            ecze_set = list(user.eczeimage_set.all())
            for e in ecze_set:
                images.append(e.image.url)
                masks.append(e.processed_image.url)
            a = {
                "trigger_x":json.dumps(triggers_x),
                "trigger_y":triggers_y,
                "poem_score":p,
                "sleep_score":sleepscore,
                "labels":[i+1 for i in range(len(p))],
                "images": images,
                "masks": masks,
            }
            return render(request, 'doctor/patient_profile.html', context=a)
        else:
            return redirect("home")
    else:
        return redirect('login')

def request_appointment_page(request):
    if request.user.is_authenticated:
        scheduled_appointments = request.user.appointment_set.all()
        requested_appointments = request.user.requestappointment_set.all()
        req_app_flag = False
        scheduled_app_flag = False
        if len(scheduled_appointments) == 0 or list(scheduled_appointments)[-1].appointment_status == False:
            message = "Doctor yet to accept the appointment"
        elif len(scheduled_appointments) != 0 and list(scheduled_appointments)[-1].appointment_status == True:
            message = "Your Appointment has already been Scheduled, Join the meeting below"
            scheduled_app_flag = True
        
        if len(requested_appointments) == 0 or list(requested_appointments)[-1].request_status == True:
            request_appointment_message = "You Haven't requested for an appointment Yet"
            req_app_flag = True
        elif (len(requested_appointments)!=0) and list(requested_appointments)[-1].request_status == False:
            request_appointment_message = "You have already requested for an appointment"

        c = {
            "message": message,
            'request_appointment_message': request_appointment_message,
            'req_app_flag': req_app_flag,
            'sd_flag': scheduled_app_flag
        }
        return render(request, 'doctor/request_appointment.html', context=c)
    else:
        return redirect('login')

def send_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            obj = RequestAppointment(patient=request.user)
            obj.save()
            return redirect('appointment')
        else:
            return redirect('home')
    else:
        return redirect('login')

def appointments_page(request):
    if request.user.is_authenticated:
        if 'doctor' in request.user.username.lower():
            patients = list(request.user.doctorprofile_set.all()[0].patients.all())
            requested_appointments = []
            for patient in patients:
                if len(list(patient.requestappointment_set.all())):
                    if list(patient.requestappointment_set.all())[-1].request_status == False:
                        requested_appointments.append(list(patient.requestappointment_set.all())[-1])
            c = {
                'requested_appointments' : requested_appointments
            }
            return render(request, 'doctor/appointments.html', context=c)
    else:
        return redirect('login')

def accept_appointment(request, patient_id, requested_appointment_id):
    if request.user.is_authenticated:
        patient = User.objects.get(id=patient_id)
        req = RequestAppointment.objects.get(id=requested_appointment_id)
        req.request_status = True
        req.save()
        app = Appointment(patient=patient)
        app.save()
        return redirect('doctor_appointments')
    else:
        return redirect('login')
    