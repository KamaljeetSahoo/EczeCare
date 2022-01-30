from django.shortcuts import render
from .models import Questionaire
from django.views.generic import ListView

class QuizListView(ListView):
    model = Questionaire
def quiz_view(request,pk):
    quiz = Questionaire.objects.get(pk=pk)
    return render(request, 'pages/Analyze.html', {'obj' : quiz})
# Create your views here.
