from django.urls import path, re_path
from .views import (
    VehicleNewAPIList,
    VehicleNewAtDealerCenterAPIList,
    VehicleNewAtDealerCenterAPIDetail,
    VehicleWithMileageAPIList,
    VehicleWithMileageAtDealerCenterAPIList,
    VehicleWithMileageAtDealerCenterAPIDetail
)

urlpatterns = [

    # re_path(r'^$', DealerList.as_view(), name='dealers'),
    # re_path(r'^dealer_centers/$', DealerCenterList.as_view(), name='dealer_centers'),
    # re_path(r'^dealer_center/(?P<slug>[\D-]+)/$', DealerCenterDetail.as_view(), name='dealer_center'),
    re_path(r'^new_vehicles/$', VehicleNewAPIList.as_view(), name='new_vehicles_api'),
    re_path(r'^new_vehicles_at_dealer_center/(\d+)/$', VehicleNewAtDealerCenterAPIList.as_view(),
            name='new_vehicles_at_dealer_center_api'),
    re_path(r'^new_vehicle_at_dealer_center/(\d+)/(\d+)/$',
            VehicleNewAtDealerCenterAPIDetail.as_view(), name='new_vehicle_at_dealer_center_api'),
    re_path(r'^vehicles_with_mileage/$', VehicleWithMileageAPIList.as_view(), name='vehicles_with_mileage_api'),
    re_path(r'^vehicles_with_mileage_at_dealer_center/(\d+)/$',
            VehicleWithMileageAtDealerCenterAPIList.as_view(), name='vehicles_with_mileage_at_dealer_center_api'),
    re_path(r'^vehicles_with_mileage/(\d+)/(\d+)/$',
            VehicleWithMileageAtDealerCenterAPIDetail.as_view(), name='vehicle_with_mileage_at_dealer_center_api'),
    # re_path(r'^add_review/(\d+)/$', AddDealerCenterReview.as_view(), name='add_review')
]
