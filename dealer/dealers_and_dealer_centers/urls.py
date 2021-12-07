from django.urls import path
from .views import DealerList, DealerCenterList, VehicleNewList, VehicleWithMileageList

urlpatterns = [
    path('', DealerList.as_view(), name='dealers'),
    path('dealer_and_dealer_centers/', DealerCenterList.as_view(), name='dealer_centers'),
    path('new_vehicles/', VehicleNewList.as_view(), name='new_vehicles'),
    path('vehicles_with_mileage/', VehicleWithMileageList.as_view(), name='vehicles_with_mileage'),

]