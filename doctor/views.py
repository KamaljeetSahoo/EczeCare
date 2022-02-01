from django.shortcuts import redirect, render

# Create your views here.
def doctor_homepage(request):
    if request.user.is_authenticated:
        if 'doctor' in request.user.username.lower():
            return render(request, 'doctor/doctor_homepage.html')
        else:
            return redirect("home")
    else:
        return redirect('login')