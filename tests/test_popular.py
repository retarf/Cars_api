from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.

class PopularTestCase(TestCase):

    def test_popular__succeed(self):
        car_make = 'honda'
        model_name_list = ['CBX', 'Accord', 'CR-V', 'HR-V']

        c = APIClient()
        endpoint = '/cars/'
        model_dict = {}
        for model in model_name_list:
            car = {
                'make': car_make,
                'model': model
            }
            response = c.post(endpoint, data=car)
            model_dict[model] = response.data['id']

        # Rates generation
        endpoint = '/rate/'
        for i in range(1, 6):
            data = {
                "car_id": model_dict['CBX'],
                "rate": i
            }
            c.post(endpoint, data=data)
        for i in range(1, 5):
            data = {
                "car_id": model_dict['Accord'],
                "rate": i
            }
            c.post(endpoint, data=data)
        for i in range(1, 4):
            data = {
                "car_id": model_dict['CR-V'],
                "rate": i
            }
            c.post(endpoint, data=data)

        # List of 3 most popular models
        cbx = {
            "id" : model_dict['CBX'],
            "make" : "HONDA",
            "make_id" : 474,
            "model" : "CBX",
            "model_id" : 27546,
            "rates" : 5
        }
        accord = {
            "id" : model_dict['Accord'],
            "make" : "HONDA",
            "make_id" : 474,
            "model" : "Accord",
            "model_id" : 1861,
            "rates" : 4
        }
        cr_v = {
            "id" : model_dict['CR-V'],
            "make" : "HONDA",
            "make_id" : 474,
            "model" : "CR-V",
            "model_id" : 1865,
            "rates" : 3
        }
        asserted_list = [cbx, accord, cr_v]

        endpoint = '/popular/'
        asserted_code = 200
        response = c.get(endpoint)
        self.assertEqual(asserted_code, response.status_code)
        self.assertEqual(asserted_list, response.data[:3])
