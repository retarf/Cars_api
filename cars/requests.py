import json
import urllib.request


class ModelListRequestError(Exception):
    MODEL_DOES_NOT_EXISTS = 1


class ApiError(Exception):
    pass


class ModelListRequest:
    API_URL = "https://vpic.nhtsa.dot.gov/api"
    ENDPOINT_URL = "/vehicles/GetModelsForMake/{car_make}?format=json"

    def __init__(self, car_make: str):
        self.car_make = car_make

    @property
    def url(self) -> str:
        endpoint_url = self.ENDPOINT_URL.format(car_make=self.car_make)

        return self.API_URL + endpoint_url

    def get_car_make_model_list(self) -> list:
        try:
            response = urllib.request.urlopen(self.url)
            body = response.read()
        except Exception as ex:
            raise ApiError(ex)

        return json.loads(body.decode("utf-8"))["Results"]

    def get_car_make_model(self, model_name: str) -> dict:
        error_msg = f"Car make {self.car_make} have not got {model_name} model."
        try:
            model = next(
                (
                    model
                    for model in self.get_car_make_model_list()
                    if model["Model_Name"] == model_name
                )
            )
        except StopIteration:
            raise ModelListRequestError(
                error_msg, ModelListRequestError.MODEL_DOES_NOT_EXISTS
            )

        return model
