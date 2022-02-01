from django.contrib import admin
from .models import EczeImage, EczeProfile, PoemScore, Food, Allergies, ContactAllergens, Product, HealthEvent, Trigger, Activity
# Register your models here.

admin.site.register(EczeImage)
admin.site.register(EczeProfile)
admin.site.register(PoemScore)
admin.site.register(Food)
admin.site.register(Allergies)
admin.site.register(ContactAllergens)
admin.site.register(Product)
admin.site.register(HealthEvent)
admin.site.register(Trigger)
admin.site.register(Activity)