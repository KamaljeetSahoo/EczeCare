from django.urls import path

from .views import homepage, landing_page, analyse_page, analyse_poem, eczeImagePage, eczeImageUpload

urlpatterns = [
    path('home/', homepage, name="home"),
    path('', landing_page, name="landing_page"),
    path('analyse/', analyse_page, name="analyse_page"),
    path('poem_analyse/', analyse_poem),
    path('ecze_image/', eczeImagePage, name="ecze_image"),
    path('image_upload/', eczeImageUpload)
]
