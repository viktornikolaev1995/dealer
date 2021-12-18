from django.urls import path, re_path
from .views import (
    DealerList,
    DealerCenterList,
    VehicleNewList,
    VehicleWithMileageList,
    VehicleNewAtDealerCenterList,
    VehicleWithMileageAtDealerCenterList,
    VehicleWithMileageAtDealerCenterDetail,
    DealerCenterDetail,
    VehicleNewAtDealerCenterDetail,
    AddDealerCenterReview,

)

urlpatterns = [
    re_path(r'^$', DealerList.as_view(), name='dealers'),
    re_path(r'^dealer_centers/$', DealerCenterList.as_view(), name='dealer_centers'),
    re_path(r'^dealer_center/(?P<slug>[\D-]+)/$', DealerCenterDetail.as_view(), name='dealer_center'),
    re_path(r'^new_vehicles/$', VehicleNewList.as_view(), name='new_vehicles'),
    re_path(r'^new_vehicles_at_dealer_center/(?P<slug>[\D-]+)/$', VehicleNewAtDealerCenterList.as_view(),
            name='new_vehicles_at_dealer_center'),
    re_path(r'^new_vehicle_at_dealer_center/(?P<slug>[\D-]+)/(?P<slug1>[\D-]+\d{4}(-\d*)?)/$',
            VehicleNewAtDealerCenterDetail.as_view(), name='new_vehicle_at_dealer_center'),
    re_path(r'^vehicles_with_mileage/$', VehicleWithMileageList.as_view(), name='vehicles_with_mileage'),
    re_path(r'^vehicles_with_mileage_at_dealer_center/(?P<slug>[\D-]+)/$',
            VehicleWithMileageAtDealerCenterList.as_view(), name='vehicles_with_mileage_at_dealer_center'),
    re_path(r'^vehicles_with_mileage/(?P<slug>[\D-]+)/(?P<slug1>[\D-]+\d{4}-\d{3,6}(-\d*)?)/$',
            VehicleWithMileageAtDealerCenterDetail.as_view(), name='vehicle_with_mileage_at_dealer_center'),
    re_path(r'^create_review/(\d+)/$', AddDealerCenterReview.as_view(), name='create_review')

]
