from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission
from django.template.defaultfilters import default_if_none
from django.utils.safestring import mark_safe
from .models import Dealer, DealerCenter, Vehicle, VehiclePhotos, DealerCenterReviews
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
            # Добавление user_permissions к созданным Users
            try:
                permission1 = Permission.objects.get(name='Can view Дилер')
                permission2 = Permission.objects.get(name='Can view Дилерский центр')
                obj.user_permissions.add(permission1, permission2)
                obj.save()
            except Exception:
                pass


class VehicleInline(admin.TabularInline):
    model = Vehicle
    extra = 1
    readonly_fields = ('get_image',)
    prepopulated_fields = {'slug': ('name', 'color', 'year_of_release', 'vehicle_mileage')}

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}
    }

    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src={obj.image.url} width="100" height="85"')
        else:
            return mark_safe(f'<img src="#"')

    get_image.short_description = "Изображение"


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_image')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [VehicleInline]
    readonly_fields = ('get_image',)

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 6, 'cols': 100})}
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user).only('name', 'slug', 'image', 'car_saloons')

    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src={obj.image.url} width="100" height="85"')
        else:
            return mark_safe(f'<img src="#"')

    get_image.short_description = "Изображение"


@admin.register(DealerCenter)
class DealerCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'address', 'telephone_number', 'get_image')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('get_image',)

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user).only('name', 'slug')

    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src={obj.image.url} width="100" height="85"')
        else:
            return mark_safe(f'<img src="#"')

    get_image.short_description = "Изображение"


class VehiclePhotosInline(admin.TabularInline):
    model = VehiclePhotos
    extra = 1
    readonly_fields = ('get_image',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }

    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src={obj.image.url} width="100" height="85"')
        else:
            return mark_safe(f'<img src="#"')

    get_image.short_description = "Фотография"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'brand', 'car_model', 'price', 'vin', 'get_image', 'dealer', 'dealer_center')
    fields = (
        ('name', 'slug', 'vin',),
        ('description', 'image',),
        ('brand', 'car_model', 'price', 'color'),
        ('engine', 'transmission', 'year_of_release', 'vehicle_with_mileage'),
        ('vehicle_mileage', 'type_of_vehicle_passport', 'owners'),
        ('dealer', 'dealer_center'),
        ('add_to_dealer_center', 'archive'), 'get_image'
              )
    prepopulated_fields = {'slug': ('name', 'color', 'year_of_release', 'vehicle_mileage')}
    readonly_fields = ('get_image',)
    inlines = [VehiclePhotosInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}
    }

    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src={obj.image.url} width="100" height="85"')
        else:
            return mark_safe(f'<img src="#"')

    get_image.short_description = "Изображение"


@admin.register(VehiclePhotos)
class VehiclePhotosAdmin(admin.ModelAdmin):
    list_display = ('title', 'vehicle', 'get_image')
    fields = (
        'title', 'vehicle', 'image', 'get_image'
    )
    readonly_fields = ('get_image',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    }

    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src={obj.image.url} width="100" height="85"')
        else:
            return mark_safe(f'<img src="#"')

    get_image.short_description = "Фотография"


@admin.register(DealerCenterReviews)
class DealerCenterReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'dealer_center')
    fields = (
        ('name', 'email'), 'text', ('dealer_center', 'parent')
    )


admin.site.site_title = 'Дилеры и их дилерские центры'
admin.site.site_header = 'Дилеры и их дилерские центры'
