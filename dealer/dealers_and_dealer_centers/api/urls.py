from django.urls import path, re_path
from .views import (
    DealerList,
    DealerCenterList,
    DealerCenterDetail,
    VehicleNewList,
    VehicleNewAtDealerCenterList,
    VehicleNewAtDealerCenterDetail,
    VehicleWithMileageList,
    VehicleWithMileageAtDealerCenterList,
    VehicleWithMileageAtDealerCenterDetail,
    DealerCenterCreateReview
)

urlpatterns = [

    re_path(r'^$', DealerList.as_view(), name='dealers_api'),
    re_path(r'^dealer_centers/$', DealerCenterList.as_view(), name='dealer_centers_api'),
    re_path(r'^dealer_center/(?P<slug>[\D-]+)/$', DealerCenterDetail.as_view(), name='dealer_center_api'),
    path('new_vehicles/', VehicleNewList.as_view(), name='new_vehicles_api'),
    path('new_vehicles_at_dealer_center/<slug:slug>/', VehicleNewAtDealerCenterList.as_view(),
         name='new_vehicles_at_dealer_center_api'),
    path('new_vehicle_at_dealer_center/<slug:slug>/<slug:slug1>/',
         VehicleNewAtDealerCenterDetail.as_view(), name='new_vehicle_at_dealer_center_api'),
    path('vehicles_with_mileage/', VehicleWithMileageList.as_view(), name='vehicles_with_mileage_api'),
    path('vehicles_with_mileage_at_dealer_center/<slug:slug>/',
         VehicleWithMileageAtDealerCenterList.as_view(), name='vehicles_with_mileage_at_dealer_center_api'),
    path('vehicles_with_mileage_at_dealer_center/<slug:slug>/<slug:slug1>/',
         VehicleWithMileageAtDealerCenterDetail.as_view(), name='vehicle_with_mileage_at_dealer_center_api'),
    re_path(r'^create_review/$', DealerCenterCreateReview.as_view(), name='create_review_api')
]
