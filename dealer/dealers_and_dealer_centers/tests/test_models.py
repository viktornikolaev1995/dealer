from ..models import Dealer, DealerCenter
from django.test import TestCase


class DealerModelTest(TestCase):

    def test_model_can_create_dealer(self):
        self.dealer_center = DealerCenter.objects.create(
            name="Toyota Lublyano", slug="toyota-lublyano", address="Moscow, st.90", telephone_number="89532271645",
            vehicle_sale=1, vehicle_repair=1, composition_of_spare_parts=1, car_warehouse=1
        )
        self.dealer = Dealer.objects.create(
            name='Toyota',
            slug='toyota')

        self.dealer.car_saloons.add(self.dealer_center)

    def test_name_max_length(self):
        dealer = Dealer.objects.get(id=1)
        max_length = dealer._meta.get_field("name").max_length
        self.assertEqual(max_length, 255)

