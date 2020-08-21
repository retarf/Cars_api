from django.test import TestCase
from rest_framework.test import APIClient

from .requests import ModelListRequest
from .requests import ModelListRequestError

class TestModelListRequestMethods(TestCase):

    def test_url(self):
        car_make = 'honda'
        models = ModelListRequest(f'{car_make}')
        asserted_url = f'https://vpic.nhtsa.dot.gov/api' \
            f'/vehicles/GetModelsForMake/{car_make}?format=json'
        self.assertEqual(asserted_url, models.url)

    def test_get_car_model_list(self):
        ''' This test check 10-th element of the list '''
        car_make = 'honda'
        asserted_list_element = {
            'Make_ID': 474,
            'Make_Name': 'HONDA',
            'Model_ID': 2128,
            'Model_Name': 'CR-Z'
            }
        list_element = ModelListRequest(f'{car_make}').get_car_make_model_list()[10]
        self.assertEqual(asserted_list_element, list_element)

    def test_get_car_make_model__succeed(self):
        car_make = 'honda'
        model_name = 'CBX'
        asserted_model_dict = {
            'Make_ID': 474,
            'Make_Name': 'HONDA',
            'Model_ID': 27546,
            'Model_Name': 'CBX'
            }
        model_list = ModelListRequest(f'{car_make}')
        model_dict = model_list.get_car_make_model(model_name)
        self.assertEqual(asserted_model_dict, model_dict)

    def test_get_car_make_mode__raise_exception(self):
        car_make = 'honda'
        model_name = 'AAA'
        model_list = ModelListRequest(f'{car_make}')
        self.assertRaises(ModelListRequestError,
            model_list.get_car_make_model, model_name)

class TestCarsEndpoint(TestCase):

    def test_cars_post_request__succeed(self):
        request_data = {
            'make': 'honda',
            'model': 'CBX'
        }
        asserted_response_data = {
            "Make_ID": 474,
            "Make_Name": "HONDA",
            "Model_ID": 27546,
            "Model_Name":"CBX"
        }
        asserted_code = 201
        endpoint = '/cars/'
        c = APIClient()
        response = c.post(endpoint, data=request_data)
        self.assertEqual(asserted_code, response.status_code)
        self.assertEqual(asserted_response_data,
            response.data)


