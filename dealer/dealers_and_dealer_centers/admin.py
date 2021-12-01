from django.contrib import admin
from .models import Dealer, DealerCenter, Vehicle

@admin.register(Dealer)

class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name',)}

@admin.register(DealerCenter)

class DealerCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'address', 'telephone_number')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Vehicle)

class DealerCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'vin', 'brand', 'price', 'image')
    prepopulated_fields = {'slug': ('name',)}