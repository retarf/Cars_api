from django.test import TestCase
from rest_framework.test import APIClient

from .models import RateModel


class TestRateEndpoint(TestCase):

    def test_rate_post_request__succeed(self):
        car = {
            'make': 'honda',
            'model': 'CBX'
        }
        asserted_code = 201
        endpoint = '/cars/'
        c = APIClient()
        response = c.post(endpoint, data=car)
        self.assertEqual(asserted_code, response.status_code)

        endpoint = '/rate/'
        data = {
            "car_id": 1,
            "rate": 1
        }
        asserted_response_data = {
            "car_id":1,
            "rate":1
            }
        response = c.post(endpoint, data=data)
        self.assertEqual(asserted_code, response.status_code)
        self.assertEqual(asserted_response_data, response.json())
