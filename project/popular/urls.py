from django.urls import path

from . import api

app_name = 'popular'
urlpatterns = [
    path('', api.get_popular_cars, name='popular'),
]
