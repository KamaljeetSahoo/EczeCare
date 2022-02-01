from django.shortcuts import render, redirect
from .utils import poem_calc_score, poem_calc_db
from django.contrib.auth.models import User
from .models import PoemScore
# Create your views here.

def landing_page(request):
    return render(request, 'pages/landing_page.html')

def triggers(request):
    if request.user.is_authenticated:
        return render(request,'pages/triggers.html')
    else:
        return redirect('login')

def homepage(request):
    if request.user.is_authenticated:
        if len(list(request.user.poemscore_set.all())) != 0:
            last_poem_entry = list(request.user.poemscore_set.all())[-1]
            last_poem_score = poem_calc_db(last_poem_entry)
        else:
            last_poem_score = 'None'
        c = {
            "last_poem_score": last_poem_score,
        }
        return render(request, 'pages/homepage.html', context=c)
    else:
        return redirect("login")

def analyse_page(request):
    if request.user.is_authenticated:
        return render(request, 'pages/analyse.html')
    else:
        return redirect('login')

def analyse_poem(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            q1 = int(request.POST['q1'][0])
            q2 = int(request.POST['q2'][0])
            q3 = int(request.POST['q3'][0])
            q4 = int(request.POST['q4'][0])
            q5 = int(request.POST['q5'][0])
            q6 = int(request.POST['q6'][0])
            q7 = int(request.POST['q7'][0])
            user = User.objects.get(id = request.user.id)
            obj = PoemScore(q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,user=user)
            obj.save()
            return redirect("home")
        else:
            return redirect('analyse_page')
