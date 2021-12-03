from django.urls import path
from .views import VehicleAPIList, VehicleAPIDetail

urlpatterns = [
    path('vehicle_list/', VehicleAPIList.as_view(), name='vehicles_api'),
    path('vehicle_detail/<int:pk>/', VehicleAPIDetail.as_view(), name='vehicle_api'),
]