from django.db import models
from enum import unique

# Create your models here.

class Car(models.Model):
    palte = models.CharField(max_length = 6 , unique = True)
    brand = models.CharField(max_length = 30)
    model = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    transmission = models.CharField(max_length = 8)
