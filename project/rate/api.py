from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RateSerializer
from .models import RateModel

class RateView(APIView):

    def post(self, request, format=None):
        print(request.data)
