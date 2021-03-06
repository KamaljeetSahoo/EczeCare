from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from eczema_profile.utils import poem_calc_db,find_cor
from collections import Counter
import json

def find_count_trigger_items(triggers):
    count = []
    for trigger in triggers:
        for food in trigger.food.all():
            count.append(str(food))
        for allergy in trigger.allergy.all():
            count.append(str(allergy))
        for contact in trigger.contact.all():
            count.append(str(contact))
        for activity in trigger.activity.all():
            count.append(str(activity))
        for health_event in trigger.health_event.all():
            count.append(str(health_event))
        for product in trigger.product.all():
            count.append(str(product))
    count = dict(Counter(count))
    count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    label_y=[]
    label_x = []
    for c in count:
        label_x.append(c)
        label_y.append(count[c])
    
    return label_x,label_y

# Create your views here.
def insights_page(request):
    if request.user.is_authenticated:
        poemscore = list(request.user.poemscore_set.all())
        p = []
        sleepscore = []
        temp =[]
        hum=[]
        poem_score_sum=0 
        temp_sum = 0
        humidity_sum=0
        roughness_score=[]
        for score in poemscore:
            temp.append(int(getattr(score,'temp')))
            hum.append(getattr(score,'hum'))
            sleepscore.append(abs(getattr(score,'q2')-4))
            roughness_score.append(int(getattr(score,'q5'))+int(getattr(score,'q6'))+int(getattr(score,'q7')))
            p.append(poem_calc_db(score))
            poem_score_sum += poem_calc_db(score)
            temp_sum += int(getattr(score,'temp'))
            humidity_sum += int(getattr(score,'hum'))
        cor_temp,cor_humidity = find_cor(temp,hum,p,poem_score_sum,temp_sum,humidity_sum)
        
        triggers = list(request.user.trigger_set.all())
        
        triggers_x,triggers_y = find_count_trigger_items(triggers)
        print(cor_temp,cor_humidity)
        #Image fetch from db
        images, masks= [], []
       
        ecze_set = list(request.user.eczeimage_set.all())
        for e in ecze_set:
            images.append(e.image.url)
            masks.append([e.processed_image.url, e.score])
        a = {
            "trigger_x":json.dumps(triggers_x),
            "trigger_y":triggers_y,
            "poem_score":p,
            "sleep_score":sleepscore,
            "labels":[i+1 for i in range(len(p))],
            "images": images,
            "masks": masks,
            "temp":json.dumps(temp),
            "hum":hum,
            "rough":json.dumps(roughness_score)
        } 


        return render(request,'pages/insights.html',context = a)
    else:
        return redirect("login")