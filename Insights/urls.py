from django.urls import path

from .views import insights_page
urlpatterns = [
    path('insights/', insights_page, name="insights"),
    
]