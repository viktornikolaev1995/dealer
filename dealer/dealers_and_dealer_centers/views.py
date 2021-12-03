from django.shortcuts import render
from django.views.generic import ListView
from .models import Dealer, DealerCenter, Vehicle

class DealerList(ListView):
    model = Dealer
    template_name = 'dealers_list.html'
    context_object_name = 'dealers'

    def get_queryset(self):
        return Dealer.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Дилеры'
        return context

class VehicleList(ListView):
    model = Vehicle
    template_name = 'index.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        return Vehicle.objects.filter(archive=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

