from django.db import IntegrityError
from django.db.models import Avg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Car
from cars.requests import ApiError, ModelListRequest, ModelListRequestError
from cars.serializers import CarFieldsSerializer


class CarsAPIView(APIView):
    def post(self, request, format=None):
        fields_serializer = CarFieldsSerializer(data=request.data)
        if fields_serializer.is_valid():
            make = fields_serializer.data["make"]
            model = fields_serializer.data["model"]
        else:
            return Response(fields_serializer.errors, status=status.HTTP_403_FORBIDDEN)
        try:
            model_list_request = ModelListRequest(make)
            model_dict = model_list_request.get_car_make_model(model)
            car = Car(
                make_id=model_dict["Make_ID"],
                make=model_dict["Make_Name"],
                model_id=model_dict["Model_ID"],
                model=model_dict["Model_Name"],
            )
            car.save()
            model_dict["id"] = car.id
        except ModelListRequestError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
        except IntegrityError:
            return Response("Record already exists", status=status.HTTP_403_FORBIDDEN)
        except ApiError as e:
            return Response(str(e), status=status.HTTP_502_BAD_GATEWAY)

        return Response(model_dict, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        cars = Car.objects.values().annotate(average_rate=Avg("ratemodel__rate"))
        return Response(cars, status=status.HTTP_200_OK)
