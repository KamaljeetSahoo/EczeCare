from django.urls import path

from .views import homepage, landing_page, analyse_page, analyse_poem,triggers,eczeImagePage,eczeImageUpload, add_trigger
from .views import add_element_page,add_element

urlpatterns = [
    path('home/', homepage, name="home"),
    path('', landing_page, name="landing_page"),
    path('analyse/', analyse_page, name="analyse_page"),
    path('poem_analyse/', analyse_poem),
    path('triggers/', triggers, name ="triggers"),
    path('ecze_image/', eczeImagePage, name="ecze_image"),
    path('image_upload/', eczeImageUpload),
    path('add_trigger/', add_trigger),
    path('add_element_page/<slug:element>/', add_element_page),
    path('add_element/<slug:element>/', add_element)
]
