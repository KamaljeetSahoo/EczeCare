from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

body_parts = ['hands', 'legs', 'back', 'face', 'torso']

# Create your models here.

class EczeProfile(models.Model):
    body_part = models.CharField(max_length=100)

class EczeImage(models.Model):
    image = models.ImageField(upload_to = 'EczeImages', null=True)
    processed_image = models.ImageField(upload_to = 'ProcessedEczeImage', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class PoemScore(models.Model):
    q1 = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    q2 = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    q3 = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    q4 = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    q5 = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    q6 = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    q7 = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Food(models.Model):
    food_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.food_name)

class Allergies(models.Model):
    allergy_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.allergy_name)

class ContactAllergens(models.Model):
    c_allergy_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.c_allergy_name)

class Activity(models.Model):
    activity_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.activity_name)

class HealthEvent(models.Model):
    health_event_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.health_event_name)

class Product(models.Model):
    product = models.CharField(max_length=100)

    def __str__(self):
        return str(self.product)

class Trigger(models.Model):
    food = models.ManyToManyField(Food)
    allergy = models.ManyToManyField(Allergies)
    contact = models.ManyToManyField(ContactAllergens)
    activity = models.ManyToManyField(Activity)
    health_event = models.ManyToManyField(HealthEvent)
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
