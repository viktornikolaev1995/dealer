from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DealerSerializer, DealerCenterSerializer, VehicleSerializer
from ..models import Dealer, DealerCenter, Vehicle

class VehicleAPIList(APIView):

    def get(self, request):
        vehicle = Vehicle.objects.filter(archive=False)
        serializer = VehicleSerializer(vehicle, many=True)
        return Response(serializer.data)


class VehicleAPIDetail(APIView):
    """
    Retrieve, update or delete a vehicle instance
    """
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(id=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)