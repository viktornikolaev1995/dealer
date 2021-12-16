from rest_framework import serializers
from ..models import Dealer, DealerCenter, Vehicle, VehiclePhotos, DealerCenterReviews


class DealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dealer
        fields = '__all__'


class DealerCenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = DealerCenter
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        exclude = ("description", "vehicle_with_mileage", "add_to_dealer", "add_to_dealer_center", "archive")

