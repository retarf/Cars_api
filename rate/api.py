from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Car
from rate.serializers import RateSerializer


class RateView(APIView):
    def post(self, request, format=None):
        rate_serializer = RateSerializer(data=request.data)
        if rate_serializer.is_valid():
            try:
                rate_serializer.save()
            except Car.DoesNotExist:
                car_id = rate_serializer.data["car_id"]
                message = f"Car ID {car_id} does not exist."
                content = {"car_id": [message]}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            return Response(rate_serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(rate_serializer.errors, status.HTTP_403_FORBIDDEN)
