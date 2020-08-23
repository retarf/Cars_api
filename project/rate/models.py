from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from cars.models import Car


RateModel(models.Model):
    car = models.ManyToMany(Car)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

