from django.urls import path

from . import api

app_name = 'cars'
urlpatterns = [
    path('', api.CarsAPIView.as_view(), name='cars'),
]
