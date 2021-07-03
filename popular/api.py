from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

from cars.models import Car


@api_view(['GET'])
def get_popular_cars(request):
    cars = Car.objects.values().annotate(
        rates=Count('ratemodel__rate')).order_by('-rates')

    return Response(cars, status.HTTP_200_OK)
