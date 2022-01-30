from django.urls import path
from .views import QuizListView,quiz_view

urlpatterns = [
    path('',QuizListView.as_view(), name='view_quiz'),
    path('<pk>/', quiz_view, name ='quiz_view'),

 ]