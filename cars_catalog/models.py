from unittest.util import _MAX_LENGTH
from django.db import models
from enum import unique

# Create your models here.

class Car(models.Model):
    palte = models.CharField(max_lenght = 6 , unique = True)
    brand = models.CharField(max_lenght = 30)
    model = models.CharField(max_lenght = 30)
    color = models.CharField(max_lenght = 20)
    transmission = models.CharField(max_lenght = 8)
