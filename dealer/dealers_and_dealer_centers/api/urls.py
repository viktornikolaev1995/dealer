from django.urls import path, re_path
from .views import (
    DealerListAPIView,
    DealerCenterListAPIView,
    DealerCenterDetailAPIView,
    VehicleNewListAPIView,
    VehicleNewAtDealerCenterListAPIView,
    VehicleNewAtDealerCenterDetailAPIView,
    VehicleWithMileageListAPIView,
    VehicleWithMileageAtDealerCenterListAPIView,
    VehicleWithMileageAtDealerCenterDetailAPIView,
    DealerCenterCreateReview
)

urlpatterns = [

    re_path(r'^$', DealerListAPIView.as_view(), name='dealers_api'),
    re_path(r'^dealer_centers/$', DealerCenterListAPIView.as_view(), name='dealer_centers_api'),
    re_path(r'^dealer_center/(?P<slug>[\D-]+)/$', DealerCenterDetailAPIView.as_view(), name='dealer_center_api'),
    path('new_vehicles/', VehicleNewListAPIView.as_view(), name='new_vehicles_api'),
    path('new_vehicles_at_dealer_center/<slug:slug>/', VehicleNewAtDealerCenterListAPIView.as_view(),
         name='new_vehicles_at_dealer_center_api'),
    path('new_vehicle_at_dealer_center/<slug:slug>/<slug:slug1>/',
         VehicleNewAtDealerCenterDetailAPIView.as_view(), name='new_vehicle_at_dealer_center_api'),
    path('vehicles_with_mileage/', VehicleWithMileageListAPIView.as_view(), name='vehicles_with_mileage_api'),
    path('vehicles_with_mileage_at_dealer_center/<slug:slug>/',
         VehicleWithMileageAtDealerCenterListAPIView.as_view(), name='vehicles_with_mileage_at_dealer_center_api'),
    path('vehicles_with_mileage_at_dealer_center/<slug:slug>/<slug:slug1>/',
         VehicleWithMileageAtDealerCenterDetailAPIView.as_view(), name='vehicle_with_mileage_at_dealer_center_api'),
    re_path(r'^create_review/$', DealerCenterCreateReview.as_view(), name='create_review_api')
]
