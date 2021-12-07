from django.shortcuts import render
from django.views.generic import ListView
from .models import Dealer, DealerCenter, Vehicle


class DealerList(ListView):
    model = Dealer
    template_name = 'dealers_and_dealer_centers/dealers_list.html'
    context_object_name = 'dealers'

    def get_queryset(self):
        return Dealer.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Дилеры'
        return context


class DealerCenterList(DealerList):
    model = DealerCenter
    template_name = 'dealers_and_dealer_centers/dealer_centers_list.html'
    context_object_name = 'dealer_centers'

    def get_queryset(self):
        return DealerCenter.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Дилерские центры'
        return context


class VehicleNewList(ListView):
    model = Vehicle
    template_name = 'dealers_and_dealer_centers/vehicle_list.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        return Vehicle.objects.filter(archive=False, vehicle_with_mileage=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новые автомобили'
        return context


class VehicleWithMileageList(VehicleNewList):

    def get_queryset(self):
        return Vehicle.objects.filter(archive=False, vehicle_with_mileage=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Автомобили с пробегом'
        return context

