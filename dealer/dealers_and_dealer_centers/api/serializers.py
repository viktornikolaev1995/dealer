from rest_framework import serializers
from ..models import Dealer, DealerCenter, Vehicle


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
        fields = '__all__'

