from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from eczema_profile.utils import poem_calc_db

# Create your views here.
def insights_page(request):
    if request.user.is_authenticated:
        poemscore = list(request.user.poemscore_set.all())
        p = []
        sleepscore = []
        for score in poemscore:
           
            sleepscore.append(getattr(score,'q2'))
            p.append(poem_calc_db(score))
        

        
        #Image fetch from db
        images, masks = [], []
        ecze_set = list(request.user.eczeimage_set.all())
        for e in ecze_set:
            images.append(e.image.url)
            masks.append(e.processed_image.url)
        a = {
            "poem_score":p,
            "sleep_score":sleepscore,
            "labels":[i+1 for i in range(len(p))],
            "images": images,
            "masks": masks,
            "test_image": images[0]
        } 


        return render(request,'pages/insights.html',context = a)
    else:
        return redirect("login")