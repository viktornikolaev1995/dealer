from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DealerSerializer, DealerCenterSerializer, VehicleSerializer
from ..models import Dealer, DealerCenter, Vehicle




class VehicleNewAPIList(APIView):
    """Вывод автомобилей нового модельного ряда, принадлежащих всем дилерским центрам"""

    def get(self, request):
        vehicle = Vehicle.objects.filter(archive=False, vehicle_with_mileage=False)
        serializer = VehicleSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleNewAtDealerCenterAPIList(APIView):
    """Вывод автомобилей нового модельного ряда, принадлежащих конкретному дилерскому центру"""

    def get(self, request, pk):
        vehicle = Vehicle.objects.filter(archive=False, vehicle_with_mileage=False, dealer_center_id=pk)
        serializer = VehicleSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleNewAtDealerCenterAPIDetail(APIView):
    """Вывод автомобиля с пробегом"""

    def get(self, request, pk):
        vehicle = self.objects.get(archive=False, vehicle_with_mileage=False, id=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)


class VehicleWithMileageAPIList(APIView):
    """Вывод автомобилей с пробегом, принадлежащих всем дилерским центрам"""

    def get(self, request):
        vehicle = Vehicle.objects.filter(archive=False, vehicle_with_mileage=True)
        serializer = VehicleSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleWithMileageAtDealerCenterAPIList(APIView):
    """Вывод автомобилей с пробегом, принадлежащих конкретному дилерскому центру"""

    def get(self, request, pk):
        vehicle = Vehicle.objects.filter(archive=False, vehicle_with_mileage=True, dealer_center_id=pk)
        serializer = VehicleSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleWithMileageAtDealerCenterAPIDetail(APIView):
    """Вывод автомобиля с пробегом"""

    def get(self, request, pk):
        vehicle = self.objects.get(archive=False, vehicle_with_mileage=True, id=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)