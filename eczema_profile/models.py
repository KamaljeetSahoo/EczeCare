from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

body_parts = ['hands', 'legs', 'back', 'face', 'torso']

# Create your models here.

class EczeProfile(models.Model):
    body_part = models.CharField(max_length=100)

class EczeImage(models.Model):
    image = models.ImageField(upload_to = 'EczeImages')
    profile = models.ManyToManyField(EczeProfile, blank=True)

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

class Triggers(models.Model):
    food = models.CharField(max_length=100)
    aller = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    health_event = models.CharField(max_length=100)
    prod = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
