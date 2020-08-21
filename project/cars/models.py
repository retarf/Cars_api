from django.db import models

class Car(models.Model):
    make_id = models.IntegerField()
    make = models.CharField(max_length=255)
    model_id = models.IngegerField()
    model = models.CharField(max_length=255)
