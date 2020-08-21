import urllib.request
import json


class ModelListRequest():
    API_URL = 'https://vpic.nhtsa.dot.gov/api'
    ENDPOINT_URL =  '/vehicles/GetModelsForMake/{car_make}?format=json'

    def __init__(self, car_make: str):
        self.car_make = car_make

    @property
    def url(self) -> str:
        endpoint_url = self.ENDPOINT_URL.format(car_make=self.car_make)

        return self.API_URL + endpoint_url

    def get_car_make_model_list(self) -> list:
        response = urllib.request.urlopen(self.url)
        body = response.read()

        return json.loads(body.decode("utf-8"))['Results']
