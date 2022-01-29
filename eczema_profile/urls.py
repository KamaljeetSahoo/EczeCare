from django.urls import path

from .views import homepage, landing_page

urlpatterns = [
    path('home/', homepage, name="home"),
    path('', landing_page, name="landing_page")
]
