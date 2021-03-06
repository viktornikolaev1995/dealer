from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    DealerListSerializer,
    DealerCenterListSerializer,
    DealerCenterCreateReviewSerializer,
    DealerCenterDetailSerializer,
    VehicleNewListSerializer,
    VehicleNewDetailSerializer,
    VehicleWithMileageListSerializer,
    VehicleWithMileageDetailSerializer
)

from ..models import Dealer, DealerCenter, Vehicle


class DealerList(APIView):
    """Список дилеров"""

    def get(self, request):
        dealer = Dealer.objects.all()
        serializer = DealerListSerializer(dealer, many=True)
        return Response(serializer.data)


class DealerCenterList(APIView):
    """Список дилерских центров"""

    def get(self, request):
        dealer_center = DealerCenter.objects.all()
        serializer = DealerCenterListSerializer(dealer_center, many=True)
        return Response(serializer.data)


class DealerCenterDetail(APIView):
    """Вывод дилерского центра"""

    def get(self, request, slug):
        dealer_center = DealerCenter.objects.get(slug=slug)
        serializer = DealerCenterDetailSerializer(dealer_center)
        return Response(serializer.data)


class VehicleNewList(APIView):
    """Список автомобилей нового модельного ряда, принадлежащих всем дилерским центрам"""

    def get(self, request):
        vehicle = Vehicle.objects.filter(archive=False, vehicle_with_mileage=False)
        serializer = VehicleNewListSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleNewAtDealerCenterList(APIView):
    """Список автомобилей нового модельного ряда, принадлежащих конкретному дилерскому центру"""

    def get(self, request, slug):
        vehicle = Vehicle.objects.filter(archive=False, vehicle_with_mileage=False, dealer_center__slug=slug)
        serializer = VehicleNewListSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleNewAtDealerCenterDetail(APIView):
    """Вывод автомобиля нового модельного ряда"""

    def get(self, request, slug, slug1):
        vehicle = Vehicle.objects.get(archive=False, vehicle_with_mileage=False, dealer_center__slug=slug, slug=slug1)
        serializer = VehicleNewDetailSerializer(vehicle)
        return Response(serializer.data)


class VehicleWithMileageList(APIView):
    """Список автомобилей с пробегом, принадлежащих всем дилерским центрам"""

    def get(self, request):
        vehicle = Vehicle.objects.filter(archive=False, vehicle_with_mileage=True)
        serializer = VehicleWithMileageListSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleWithMileageAtDealerCenterList(APIView):
    """Список автомобилей с пробегом, принадлежащих конкретному дилерскому центру"""

    def get(self, request, slug):
        vehicle = Vehicle.objects.filter(archive=False, vehicle_with_mileage=True, dealer_center__slug=slug)
        serializer = VehicleWithMileageListSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleWithMileageAtDealerCenterDetail(APIView):
    """Вывод автомобиля с пробегом"""

    def get(self, request, slug, slug1):
        vehicle = Vehicle.objects.get(archive=False, vehicle_with_mileage=True, dealer_center__slug=slug, slug=slug1)
        serializer = VehicleWithMileageDetailSerializer(vehicle)
        return Response(serializer.data)


class DealerCenterCreateReview(APIView):
    """Создание отзыва дилерского центра"""

    def post(self, request):
        review = DealerCenterCreateReviewSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)

