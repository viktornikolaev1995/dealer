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
    AddDealerCenterReview,
)

urlpatterns = [
    path('', DealerList.as_view(), name='dealers'),
    re_path(r'^dealer_and_dealer_centers/$', DealerCenterList.as_view(), name='dealer_centers'),
    re_path(r'^new_vehicles/$', VehicleNewList.as_view(), name='new_vehicles'),
    re_path(r'new_vehicles/(?P<slug>[\D-]+)/$', VehicleNewAtDealerCenterList.as_view(),
            name='new_vehicles_at_dealer_center'),
    re_path(r'^vehicles_with_mileage/$', VehicleWithMileageList.as_view(), name='vehicles_with_mileage'),
    re_path(r'^vehicles_with_mileage/(?P<slug>[\D-]+)/$', VehicleWithMileageAtDealerCenterList.as_view(),
            name='vehicles_with_mileage_at_dealer_center'),
    re_path(r'^vehicles_with_mileage/(?P<slug>[\D-]+)/(?P<slug1>\D+-\w+-\D+-\d{4}-\d{6})/$',
            VehicleWithMileageAtDealerCenterDetail.as_view(), name='vehicle_with_mileage_at_dealer_center'),
    path('dealer_and_dealer_centers/<slug:slug>/', DealerCenterDetail.as_view(), name='dealer_center'),
    re_path(r'^add_review/(?P<int>\d+)/$', AddDealerCenterReview.as_view(), name='add_review')

]