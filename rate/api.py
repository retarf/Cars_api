from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RateSerializer
from .models import RateModel
from cars.models import Car

class RateView(APIView):

    def post(self, request, format=None):
        rate_serializer = RateSerializer(data=request.data)
        if rate_serializer.is_valid():
            rate_serializer.save()
            return Response(rate_serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(rate_serializer.errors, status.HTTP_403_FORBIDDEN)
