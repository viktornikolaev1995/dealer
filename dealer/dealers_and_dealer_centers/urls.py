from django.urls import path
from .views import VehicleList

urlpatterns = [
    path('', VehicleList.as_view(), name='main')
]