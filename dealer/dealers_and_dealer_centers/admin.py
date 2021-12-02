from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission
from .models import Dealer, DealerCenter, Vehicle
from django.forms import TextInput, Textarea
from django.db import models


# Unregister the provided model admin
admin.site.unregister(User)

# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    def is_not_superuser(self, request):
        if not request.user.is_superuser:
            return False
        return True
    def has_delete_permission(self, request, obj=None):
        return self.is_not_superuser(request)
    def has_add_permission(self, request):
        return self.is_not_superuser(request)
    def has_change_permission(self, request, obj=None):
        return self.is_not_superuser(request)
    def has_view_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.is_staff = True
            obj.save()
            # Добавление user_permissions c id=28 (codename=view_dealercenter), id=36 (codename=view_dealer) к созданным Users
            permission1 = Permission.objects.get(name='Can view dealer')
            permission2 = Permission.objects.get(name='Can view dealer center')
            obj.user_permissions.add(permission1, permission2)
            obj.save()

class VehicleInline(admin.TabularInline):
    model = Vehicle
    prepopulated_fields = {'slug': ('name',)}

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}

    }


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [VehicleInline]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user).only('name', 'slug', 'image', 'car_saloons')

@admin.register(DealerCenter)
class DealerCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'address', 'telephone_number', 'image')
                    # ('vehicle_sale', 'vehicle_repair', 'composition_of_spare_parts', 'car_warehouse'))
    prepopulated_fields = {'slug': ('name',)}

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user).only('name', 'slug')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'vin', 'brand', 'price', 'image', 'dealer', 'dealer_center')
    fields = (('name', 'slug', 'vin',),
              ('description', 'image'), (),
              ('brand', 'car_model', 'price', 'color'), ('dealer', 'dealer_center', 'add_to_dealer_center'))
    prepopulated_fields = {'slug': ('name',)}

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}

    }