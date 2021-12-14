from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Dealer, DealerCenter, Vehicle
from .forms import DealerCenterReviewForm


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


class DealerCenterList(ListView):
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
        obj = Vehicle.objects.filter(archive=False, vehicle_with_mileage=False)
        if obj.exists():
            return obj
        raise Http404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новые автомобили'
        return context


class VehicleNewAtDealerCenterList(VehicleNewList):

    def get_queryset(self, **kwargs):
        obj = Vehicle.objects.filter(archive=False, vehicle_with_mileage=False, dealer_center__slug=self.kwargs['slug'])
        if obj.exists():
            return obj
        raise Http404


class VehicleWithMileageList(VehicleNewList):

    def get_queryset(self):
        obj = Vehicle.objects.filter(archive=False, vehicle_with_mileage=True)
        if obj.exists():
            return obj
        raise Http404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Автомобили с пробегом'
        return context


class VehicleWithMileageAtDealerCenterList(VehicleWithMileageList):

    def get_queryset(self, **kwargs):
        obj = Vehicle.objects.filter(archive=False, vehicle_with_mileage=True, dealer_center__slug=self.kwargs['slug'])
        if obj.exists():
            return obj
        raise Http404

class DealerCenterDetail(DetailView):
    model = DealerCenter
    template_name = 'dealers_and_dealer_centers/dealer_center_detail.html'
    context_object_name = 'dealer_center'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class VehicleWithMileageAtDealerCenterDetail(DetailView):
    model = Vehicle
    template_name = 'dealers_and_dealer_centers/vehicle_detail.html'
    context_object_name = 'vehicle'
    slug_field = 'slug'
    slug_url_kwarg = 'slug1'


class AddDealerCenterReview(View):
    """Отзывы дилерского центра"""

    def post(self, request, pk):
        form = DealerCenterReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.dealer_center_id = pk
            form.save()

        return redirect("/")


