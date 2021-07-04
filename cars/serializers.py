from rest_framework import serializers

from .models import Car


class CarFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["make", "model"]
