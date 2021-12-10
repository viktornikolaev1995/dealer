from django.urls import path
from .views import (
    DealerList,
    DealerCenterList,
    VehicleNewList,
    VehicleWithMileageList,
    VehicleNewListAtDealerCenter,
    VehicleWithMileageAtDealerCenterList,
    VehicleWithMileageAtDealerCenterDetail
)

urlpatterns = [
    path('', DealerList.as_view(), name='dealers'),
    path('vehicles_with_mileage/<slug:slug>/', VehicleWithMileageAtDealerCenterDetail.as_view(),
         name='vehicle_with_mileage_at_dealer_center'),
    path('dealer_and_dealer_centers/', DealerCenterList.as_view(), name='dealer_centers'),
    path('new_vehicles/', VehicleNewList.as_view(), name='new_vehicles'),
    path('new_vehicles/<slug:slug>/', VehicleNewListAtDealerCenter.as_view(), name='new_vehicles_at_dealer_center'),
    path('vehicles_with_mileage/', VehicleWithMileageList.as_view(), name='vehicles_with_mileage'),
    path('vehicles_with_mileage/<slug:slug>/', VehicleWithMileageAtDealerCenterList.as_view(),
         name='vehicles_with_mileage_at_dealer_center'),

]