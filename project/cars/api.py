from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CarSerializer
from .requests import ModelListRequest, ModelListRequestError


class CarsAPIView(APIView):

    def post(self, request, format=None):
        car_serializer = CarSerializer(data=request.data)
        make = request.data['make']
        model = request.data['model']
        try:
            model_list_request = ModelListRequest(make)
            model_dict = model_list_request.get_car_make_model(model)
        except ModelListRequestError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

        return Response(model_dict, status=status.HTTP_200_OK)
