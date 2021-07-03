from rest_framework import serializers

from .models import RateModel
from cars.models import Car

class RateSerializer(serializers.Serializer):
    car_id = serializers.IntegerField(required=True)
    rate = serializers.IntegerField(required=True,
        min_value=1, max_value=5)

    def save(self):
        car_id = self.validated_data['car_id']
        rate = self.validated_data['rate']
        car = Car.objects.get(id=car_id)
        rate_object = RateModel()
        rate_object.rate = rate
        rate_object.car = car
        rate_object.save()


