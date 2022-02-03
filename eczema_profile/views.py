from django.shortcuts import render, redirect 
from .utils import poem_calc_score, poem_calc_db, process_image, encode_image, last_severe,weather,find_cor
from django.contrib.auth.models import User
from .models import PoemScore, EczeImage
from .models import Activity, Food, Allergies, ContactAllergens, HealthEvent, Product, Trigger
from PIL import Image
import numpy as np
# Create your views here.
msgs ={-1:"Your progress has been good, We are happy for you!",0:"Take the questionaire to help us track your progress",1:"Aloevera helps cure itchiness and gives some relief",2:"Listen to soothing music for better sleep",3:"You have to remember not to scratch your skin",4:"Remember to take you medicines on time and keep clean",5:"stay hydrated and moisturised!",6:"Apply lotions and shower some love on your skin",7:"Coconut Oil is the best home remedy for dry skin!"}
def landing_page(request):
    return render(request, 'pages/landing_page.html')

def triggers(request):
    if request.user.is_authenticated:
        c = {
            'foods': list(Food.objects.all()),
            'activities': list(Activity.objects.all()),
            'allergies': list(Allergies.objects.all()),
            'contactAllergens': list(ContactAllergens.objects.all()),
            'healthEvents': list(HealthEvent.objects.all()),
            'products': list(Product.objects.all())
        }
        return render(request,'pages/triggers.html', context=c)
    else:
        return redirect('login')

def add_trigger(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            trigger_list = ['food', 'allergy', 'activities', 'healthEvents', 'products', 'contactAllergens']
            trigger = Trigger(user=request.user)
            if len(request.POST) > 1:
                trigger.save()
                request.POST = dict(request.POST)
                for val in trigger_list:
                    if val in request.POST:
                        if val == 'food':
                            for food in request.POST[val]:
                                trigger.food.add(Food.objects.get(food_name=food))
                        if val == 'allergy':
                            for allergy in request.POST[val]:
                                trigger.allergy.add(Allergies.objects.get(allergy_name=allergy))
                        if val == 'activities':
                            for activity in request.POST[val]:
                                trigger.activity.add(Activity.objects.get(activity_name=activity))
                        if val == 'healthEvents':
                            for h_event in request.POST[val]:
                                trigger.health_event.add(HealthEvent.objects.get(health_event_name=h_event))
                        if val == 'products':
                            for prod in request.POST[val]:
                                trigger.product.add(Product.objects.get(product=prod))
                        if val == 'contactAllergens':
                            for c_allergen in request.POST[val]:
                                trigger.contact.add(ContactAllergens.objects.get(c_allergy_name=c_allergen))
                trigger.save()
                return redirect("home")
            else:
                return redirect("triggers")
        else:
            return render("triggers")
    else:
        return redirect("login")

def homepage(request):
    if request.user.is_authenticated:
        if len(list(request.user.poemscore_set.all())) != 0:
            last_poem_entry = list(request.user.poemscore_set.all())[-1]
            lastsevere = last_severe(list(request.user.poemscore_set.all())[-1])
            last_poem_score = poem_calc_db(last_poem_entry)
        else:
            lastsevere = 0
            last_poem_score = 'None'
        poemscore = list(request.user.poemscore_set.all())
        p = []
        sleepscore = []
        temp =[]
        hum=[]
        poem_score_sum=0 
        temp_sum = 0
        humidity_sum=0
        for score in poemscore:
            temp.append(int(getattr(score,'temp')))
            hum.append(getattr(score,'hum'))
            sleepscore.append(abs(getattr(score,'q2')-4))
            p.append(poem_calc_db(score))
            poem_score_sum += poem_calc_db(score)
            temp_sum += int(getattr(score,'temp'))
            humidity_sum += int(getattr(score,'hum'))
        if p!=[]:
            cor_temp,cor_humidity = find_cor(temp,hum,p,poem_score_sum,temp_sum,humidity_sum)
        else:
            t="Track to know dependency"
            h="Track to know dependency"
            cor_temp,cor_humidity=0,0

        if cor_temp>0:
            cor_temp = cor_temp*100
            t = "High Temperature causes you discomfort"
        elif cor_temp<0:
            cor_temp = abs(cor_temp*100)
            t = "Low Temperature cause you discomfort"
        elif cor_temp==0:
            cor_humidity = cor_humidity*100
            t= "Your eczema is Temperature indepedent"


        if cor_humidity>0:
            cor_humidity = cor_humidity*100
            h = "High Humidity causes you discomfort"
        elif cor_humidity<0:
            cor_humidity = abs(cor_humidity*100)
            h = "Low Humidity cause you discomfort"
        if cor_humidity==0:
            cor_humidity = cor_humidity*100
            h = "Your eczema is Humidity indepedent"


        if 0<cor_humidity<=30:
            cor_humidity = 25
        elif 30<cor_humidity<=60:
            cor_humidity = 50
        elif 60<cor_humidity<=80:
            cor_humidity = 75
        elif 80<cor_humidity<=100:
            cor_humidity = 100
        else:
            cor_humidity = 0

        if 0<cor_temp<=30:
            cor_temp = 25   
        elif 30<cor_temp<=60:
            cor_temp = 50
        elif 60<cor_temp <=80:
            cor_temp = 75
        elif 80<cor_temp<=100:
            cor_temp = 100
        else:
            cor_temp = 0
        
        c = {
            "lastsevere":  msgs[lastsevere],
            "last_poem_score": last_poem_score,
            "humidity_cor": int(cor_humidity),
            "temp_cor":int(cor_temp),
            "t":t,
            "h":h
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
            h,t = weather()
            obj = PoemScore(q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,temp=t,hum=h,user=user)
            obj.save()
            return redirect("home")
        else:
            return redirect('analyse_page')

def eczeImagePage(request):
    if request.user.is_authenticated:
        return render(request, 'pages/eczeImage.html')
    else:
        return redirect("login")

def eczeImageUpload(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            image = request.FILES['ecze_image']
            image_name = str(image)
            np_image = np.array(Image.open(image))
            processed_image = process_image(np_image)
            encoded_image = encode_image(processed_image)

            obj = EczeImage(image = image, user = request.user)
            obj.processed_image.save(image_name, encoded_image)
            obj.save()
            
            return redirect("home")

        else:
            return redirect("ecze_image")
    else:
        return redirect("login")


def add_element_page(request, element):
    print(element)
    if request.user.is_authenticated:
        return render(request, 'pages/add_element.html',context={'element':element})
    else:
        return redirect("login")

def add_element(request, element):
    
    if request.user.is_authenticated:
        if request.method=="POST":
            added_val=request.POST['element']
            if(element == "food"):
                obj=Food(food_name=added_val)
                obj.save()
            if(element == "contact_allergen"):
                obj=ContactAllergens(c_allergy_name=added_val)
                obj.save()
            if(element == "health_events"):
                obj=HealthEvent(health_event_name=added_val)
                obj.save()
            if(element == "products"):
                obj=Product(product=added_val)
                obj.save()
            if(element == "allergy"):
                obj=Allergies(allergy_name=added_val)
                obj.save()
            if(element == "activities"):
                obj=Activity(activity_name=added_val)
                obj.save()
            return redirect("triggers")																							
        else:
            return redirect("home")    
    else:
        return redirect("login")



