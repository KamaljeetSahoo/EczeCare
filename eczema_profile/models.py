from django.db import models

body_parts = ['hands', 'legs', 'back', 'face', 'torso']

# Create your models here.

class EczeProfile(models.Model):
    body_part = models.CharField(max_length=100)

class EczeImage(models.Model):
    image = models.ImageField(upload_to = 'EczeImages')
    profile = models.ManyToManyField(EczeProfile, blank=True, null=True)