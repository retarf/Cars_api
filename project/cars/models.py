from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
