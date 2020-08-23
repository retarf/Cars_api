from django.urls import path

from . import api

app_name = 'rate'
urlpatterns = [
    path('', api.RateView.as_view(), name='rate'),
]
