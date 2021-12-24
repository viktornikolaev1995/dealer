from django.test import TestCase, Client
from django.urls import reverse

from ..models import (
    Dealer,
    DealerCenter,
    Vehicle
)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.dealers_list_url = reverse('dealers')
        self.dealer_centers_list_url = reverse('dealer_centers')
        self.dealer_center_detail_url = reverse('dealer_center', kwargs={'slug': 'toyota-lublyano'})
        self.dealer_center_1 = DealerCenter.objects.create(
            name='Toyota Любляно',
            slug='toyota-lublyano',
            address='Москва, ул.Полбина 42',
            telephone_number='+796587651635',
            vehicle_sale=1,
            vehicle_repair=1,
            composition_of_spare_parts=0,
            car_warehouse=0
        )

        self.new_vehicles_list_url = reverse('new_vehicles')
        self.new_vehicles_at_dealer_center_list_url = reverse(
            'new_vehicle_at_dealer_center', kwargs={'slug': 'toyota-lublyano', 'slug1': 'toyota-camri-2021'})
        self.dealer_1 = Dealer.objects.create(
            name='Toyota',
            slug='toyota'
        )
        self.dealer_1.car_saloons.add(self.dealer_center_1)

    def test_dealers_list_GET(self):
        response = self.client.get(self.dealers_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dealers_and_dealer_centers/dealers_list.html')

    def test_dealer_centers_list_GET(self):
        response = self.client.get(self.dealer_centers_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dealers_and_dealer_centers/dealer_centers_list.html')

    def test_dealer_center_detail_GET(self):
        response = self.client.get(self.dealer_center_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dealers_and_dealer_centers/dealer_center_detail.html')

    # def test_new_vehicles_list_GET(self):
    #     response = self.client.get(self.new_vehicles_list_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'dealers_and_dealer_centers/vehicle_new_list.html')

