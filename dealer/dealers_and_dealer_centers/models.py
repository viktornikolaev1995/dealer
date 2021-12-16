import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Dealer(models.Model):
	"""Дилер"""

	name = models.CharField(max_length=255, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание', blank=True)
	slug = models.SlugField(unique=True, verbose_name='Слаг')
	car_saloons = models.ManyToManyField(
		'DealerCenter',
		verbose_name='Дилерские центры',
		related_name='dealer_centers'
	)
	image = models.ImageField(upload_to='dealer/', verbose_name='Изображение', blank=True, null=True)
	user = models.OneToOneField(
		User,
		verbose_name="Пользователь",
		on_delete=models.SET_NULL,
		blank=True, null=True
	)

	class Meta:
		verbose_name = 'Дилер'
		verbose_name_plural = 'Дилеры'

	def __str__(self):
		return self.name


class DealerCenter(models.Model):
	"""Дилерский центр"""

	name = models.CharField(max_length=255, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание', blank=True)
	slug = models.SlugField(unique=True, verbose_name='Слаг')
	address = models.CharField(max_length=255, verbose_name='Адрес', blank=True)
	telephone_number = models.CharField(max_length=50, verbose_name='Официальный номер', blank=True)
	image = models.ImageField(upload_to='dealer_centers/', verbose_name='Изображение', blank=True, null=True)
	vehicle_sale = models.BooleanField(default=False, verbose_name='Продажа транспортных средств')
	vehicle_repair = models.BooleanField(default=False, verbose_name='Ремонт транспортных средств')
	composition_of_spare_parts = models.BooleanField(default=False, verbose_name='Склад запасных частей')
	car_warehouse = models.BooleanField(default=False, verbose_name='Склад автомобилей')
	user = models.ForeignKey(
		User,
		verbose_name="Пользователь",
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)

	class Meta:
		verbose_name = 'Дилерский центр'
		verbose_name_plural = 'Дилерские центры'

	def get_review(self):
		return self.dealer_center_review.filter(parent__isnull=True)

	def get_absolute_url(self):
		return reverse('dealer_center', kwargs={'slug': self.slug})

	def __str__(self):
		return self.name


class Vehicle(models.Model):
	"""Транспортное средство"""

	name = models.CharField(max_length=255, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание', blank=True)
	slug = models.SlugField(unique=True, verbose_name='Слаг')
	vin = models.CharField(max_length=100, unique=True, verbose_name='VIN код')
	brand = models.CharField(max_length=255, verbose_name='Марка')
	car_model = models.CharField(max_length=255, verbose_name='Модель')
	color = models.CharField(max_length=100, verbose_name='Цвет')
	engine = models.CharField(max_length=100, verbose_name='Двигатель')
	transmission = models.CharField(max_length=100, verbose_name='Трансмиссия')
	year_of_release = models.PositiveSmallIntegerField(verbose_name="Год выпуска")
	vehicle_with_mileage = models.BooleanField(default=False, verbose_name='С пробегом')
	vehicle_mileage = models.PositiveIntegerField(verbose_name="Пробег", blank=True, null=True)
	type_of_vehicle_passport = models.CharField(max_length=100, verbose_name='Тип ПТС', blank=True)
	owners = models.PositiveSmallIntegerField(verbose_name="Количество владельцев", blank=True, null=True)
	image = models.ImageField(upload_to='vehicle/%Y/%m/%d/', verbose_name='Изображение', blank=True, null=True)
	price = models.PositiveIntegerField(verbose_name='Стоимость')
	add_to_dealer = models.DateTimeField(auto_now_add=True, verbose_name='Дата первичного поступления к дилеру')
	add_to_dealer_center = models.DateTimeField(verbose_name='Дата поступления в дилерский центр', blank=True, null=True)
	dealer = models.ForeignKey(
		Dealer,
		verbose_name='Наименование дилера',
		on_delete=models.PROTECT,
		related_name='vehicle_dealer',
		blank=True,
		null=True
	)
	dealer_center = models.ForeignKey(
		DealerCenter,
		verbose_name='Наименование дилерского центра',
		on_delete=models.PROTECT,
		related_name='vehicle_dealer_center',
		blank=True,
		null=True
	)
	archive = models.BooleanField(default=False, verbose_name='Архив')

	class Meta:
		verbose_name = 'Транспортное средство'
		verbose_name_plural = 'Транспортные средства'
		unique_together = [['dealer', 'vin']]

	def __str__(self):
		return self.name


class VehiclePhotos(models.Model):
	"""Фотографии транспортного средства"""

	title = models.CharField(max_length=255, verbose_name='Заголовок')
	image = models.ImageField(upload_to="vehicle_photos/%Y/%m/%d/", verbose_name="Фотография")
	vehicle = models.ForeignKey(
		Vehicle,
		on_delete=models.CASCADE,
		verbose_name="Транспортное средство",
		related_name='vehicle_images',
		blank=True,
		null=True
	)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Фотография транспортного средства'
		verbose_name_plural = 'Фотографии транспортного средства'


class DealerCenterReviews(models.Model):
	"""Отзывы дилерского центра"""

	name = models.CharField(max_length=255, verbose_name="Имя")
	text = models.TextField(max_length=2500, verbose_name="Текст отзыва")
	email = models.EmailField(verbose_name="Почта")
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата написания отзыва')
	parent = models.ForeignKey(
		'self',
		on_delete=models.SET_NULL,
		verbose_name="Родитель",
		blank=True,
		null=True
	)
	dealer_center = models.ForeignKey(
		DealerCenter,
		on_delete=models.CASCADE,
		verbose_name="Дилерский центр",
		related_name="dealer_center_review"
	)

	def get_all_children(self):
		return DealerCenterReviews.objects.filter(parent_id=self.id).order_by("id")

	def __str__(self):
		return f'{self.name}-{self.dealer_center}'

	class Meta:
		verbose_name = "Отзыв дилерского центра"
		verbose_name_plural = "Отзывы дилерского центра"
