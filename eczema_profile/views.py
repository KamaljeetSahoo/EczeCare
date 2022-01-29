from django.shortcuts import render, redirect

# Create your views here.

def landing_page(request):
    return render(request, 'pages/landing_page.html')


def homepage(request):
    if request.user.is_authenticated:
        name = request.user.username
        name += " KAPS"
        c = {
            "abc": name,
            "items": ['shampoo', 'apple', 'orange', 'hear']
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
            print(request.POST)
            return redirect("home")
        else:
            return redirect('analyse_page')
