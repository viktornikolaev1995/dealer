from rest_framework import serializers
from ..models import Dealer, DealerCenter, Vehicle, VehiclePhotos, DealerCenterReviews


class DealerListSerializer(serializers.ModelSerializer):
    """Список дилеров"""

    car_saloons = serializers.SlugRelatedField(slug_field="slug", many=True, read_only=True)

    class Meta:
        model = Dealer
        exclude = ("user",)


class DealerCenterListSerializer(serializers.ModelSerializer):
    """Список дилерских центров"""

    class Meta:
        model = DealerCenter
        exclude = ("description", "user",)


class DealerCenterCreateReviewSerializer(serializers.ModelSerializer):
    """Создание отзыва дилерского центра"""

    class Meta:
        model = DealerCenterReviews
        fields = "__all__"


class DealerCenterReviewsSerializer(serializers.ModelSerializer):
    """Список отзывов дилерского центра"""

    class Meta:
        model = DealerCenterReviews
        fields = ("name", "email", "text")


class DealerCenterDetailSerializer(serializers.ModelSerializer):
    """Дилерский центр"""

    dealer_center_review = DealerCenterReviewsSerializer(many=True)

    class Meta:
        model = DealerCenter
        exclude = ("description", "user",)


class VehicleNewListSerializer(serializers.ModelSerializer):
    """Список автомобилей нового модельного ряда"""

    dealer = serializers.SlugRelatedField(slug_field="slug", read_only=True)
    dealer_center = serializers.SlugRelatedField(slug_field="slug", read_only=True)

    class Meta:
        model = Vehicle
        exclude = ("description", "vehicle_with_mileage", "add_to_dealer", "add_to_dealer_center", "archive")


class VehicleWithMileageListSerializer(serializers.ModelSerializer):
    """Список автомобилей с пробегом"""

    dealer = serializers.SlugRelatedField(slug_field="slug", read_only=True)
    dealer_center = serializers.SlugRelatedField(slug_field="slug", read_only=True)

    class Meta:
        model = Vehicle
        exclude = ("description", "vehicle_with_mileage", "add_to_dealer", "add_to_dealer_center", "archive")


class VehicleNewDetailSerializer(serializers.ModelSerializer):
    """Автомобиль нового модельного ряда"""

    dealer = serializers.SlugRelatedField(slug_field="slug", read_only=True)
    dealer_center = serializers.SlugRelatedField(slug_field="slug", read_only=True)

    class Meta:
        model = Vehicle
        exclude = ("description", "vehicle_with_mileage", "add_to_dealer", "add_to_dealer_center", "archive")


class VehicleWithMileageDetailSerializer(serializers.ModelSerializer):
    """Автомобиль с пробегом"""

    dealer = serializers.SlugRelatedField(slug_field="slug", read_only=True)
    dealer_center = serializers.SlugRelatedField(slug_field="slug", read_only=True)

    class Meta:
        model = Vehicle
        exclude = ("description", "vehicle_with_mileage", "add_to_dealer", "add_to_dealer_center", "archive")