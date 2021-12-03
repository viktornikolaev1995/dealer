from django.urls import path
from .views import DealerList, VehicleList

urlpatterns = [
    path('', DealerList.as_view(), name='dealers'),
    path('vehicles/', VehicleList.as_view(), name='vehicles')
]