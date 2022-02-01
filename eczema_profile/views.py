from django.shortcuts import render, redirect
from .utils import poem_calc_score, poem_calc_db, process_image, encode_image
from django.contrib.auth.models import User
from .models import PoemScore, EczeImage
from .models import Activity, Food, Allergies, ContactAllergens, HealthEvent, Product, Trigger
from PIL import Image
import numpy as np
# Create your views here.

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
            trigger.save()
            request.POST = dict(request.POST)
            for val in trigger_list:
                if val in request.POST:
                    if val == 'food':
                        for food in request.POST[val]:
                            print(food)
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
            return render("triggers")
    else:
        return redirect("login")

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
        return render(request, 'pages/add_element.html')
    else:
        return redirect("login")