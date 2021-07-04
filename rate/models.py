from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from cars.models import Car


class RateModel(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
