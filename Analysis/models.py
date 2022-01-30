from django.db import models

# Create your models here.
class Questionaire(models.Model):
    Questions = models.CharField(max_length = 100)
    option1 = models.CharField(max_length = 100)
    option2 = models.CharField(max_length = 100)
    option3 = models.CharField(max_length = 100)
    option4 = models.CharField(max_length = 100)
    date = models.CharField(max_length = 100)
    score = models.IntegerField(default=0)