from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import (
    DealerList,
    DealerCenterList,
    DealerCenterDetail,
    VehicleNewList,
    VehicleNewAtDealerCenterList,
    VehicleNewAtDealerCenterDetail,
    VehicleWithMileageList,
    VehicleWithMileageAtDealerCenterList,
    VehicleWithMileageAtDealerCenterDetail
)


class TestUrls(SimpleTestCase):

    def test_dealer_url_is_resolved(self):
        url = reverse('dealers')
        # print(resolve(url))
        print(resolve(url).func.view_class)
        # print(resolve(url).view_name)
        self.assertEqual(resolve(url).func.view_class, DealerList)

    def test_dealer_centers_is_resolved(self):
        url = reverse('dealer_centers')
        self.assertEqual(resolve(url).func.view_class, DealerCenterList)

    def test_dealer_center_is_resolved(self):
        url = reverse('dealer_center', kwargs={'slug': 'toyota-lublyano'})
        self.assertEqual(resolve(url).func.view_class, DealerCenterDetail)

    def test_new_vehicles_is_resolved(self):
        url = reverse('new_vehicles')
        self.assertEqual(resolve(url).func.view_class, VehicleNewList)

    def test_new_vehicles_at_dealer_center_is_resolved(self):
        url = reverse('new_vehicles_at_dealer_center', kwargs={'slug': 'toyota-lublyano'})
        self.assertEqual(resolve(url).func.view_class, VehicleNewAtDealerCenterList)

    def test_new_vehicle_at_dealer_center_is_resolved(self):
        url = reverse('new_vehicle_at_dealer_center', kwargs={'slug': 'toyota-lublyano', 'slug1': 'toyota-camri-2021'})
        self.assertEqual(resolve(url).func.view_class, VehicleNewAtDealerCenterDetail)

    def test_vehicles_with_mileage_is_resolved(self):
        url = reverse('vehicles_with_mileage')
        self.assertEqual(resolve(url).func.view_class, VehicleWithMileageList)

    def test_vehicles_with_mileage_at_dealer_center_is_resolved(self):
        url = reverse('vehicles_with_mileage_at_dealer_center', kwargs={'slug': 'toyota-lublyano'})
        self.assertEqual(resolve(url).func.view_class, VehicleWithMileageAtDealerCenterList)

    def test_vehicle_with_mileage_at_dealer_center_is_resolved(self):
        url = reverse(
            'vehicle_with_mileage_at_dealer_center',
            kwargs={'slug': 'toyota-lublyano', 'slug1': 'toyota-camri-2021-44567'}
        )
        self.assertEqual(resolve(url).func.view_class, VehicleWithMileageAtDealerCenterDetail)





