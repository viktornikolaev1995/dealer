from django.shortcuts import render
from django.views.generic import ListView
from .models import Vehicle


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

