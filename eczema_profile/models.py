from django.db import models
from django.contrib.auth.models import User

body_parts = ['hands', 'legs', 'back', 'face', 'torso']

# Create your models here.

class EczeProfile(models.Model):
    body_part = models.CharField(max_length=100)

class EczeImage(models.Model):
    image = models.ImageField(upload_to = 'EczeImages')
    profile = models.ManyToManyField(EczeProfile, blank=True)

class PoemScore(models.Model):
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)