from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from eczema_profile.utils import poem_calc_db

# Create your views here.
def insights_page(request):
    if request.user.is_authenticated:
        poemscore = list(request.user.poemscore_set.all())
        l = []
        i = 1

        p = []
        for score in poemscore:
            p.append(poem_calc_db(score))
            l.append(i)
            i+=1
        a = {
            "poem_score":p,
            "labels":l
        } 

        return render(request,'pages/insights.html',context = a)
    else:
        return redirect("login")