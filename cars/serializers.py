from rest_framework import serializers

from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model']
