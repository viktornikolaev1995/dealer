from django.contrib.auth.models import User
from django.db import models


class Dealer(models.Model):
	"""Дилер"""

	name = models.CharField(max_length=255, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание', blank=True)
	slug = models.SlugField(unique=True, verbose_name='Слаг')
	image = models.ImageField(upload_to='dealer/', verbose_name='Изображение', blank=True, null=True)
	car_saloons = models.ManyToManyField(
		'DealerCenter',
		verbose_name='Дилерские центры',
		related_name='dealer_centers')
	user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.PROTECT)

	def __str__(self):
		return self.name

class DealerCenter(models.Model):
	"""Дилерский центр"""

	name = models.CharField(max_length=255, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание', blank=True)
	slug = models.SlugField(unique=True, verbose_name='Слаг')
	address = models.CharField(max_length=255, verbose_name='Адрес')
	telephone_number = models.CharField(max_length=50, verbose_name='Официальный номер')
	image = models.ImageField(upload_to='dealer_centers/', verbose_name='Изображение', blank=True, null=True)
	vehicle_sale = models.BooleanField(default=False, verbose_name='Продажа транспортных средств')
	vehicle_repair = models.BooleanField(default=False, verbose_name='Ремонт транспортных средств')
	composition_of_spare_parts = models.BooleanField(default=False, verbose_name='Склад запасных частей')
	car_warehouse = models.BooleanField(default=False, verbose_name='Склад автомобилей')
	user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT)

	def __str__(self):
		return self.name

class Vehicle(models.Model):
	"""Транспортное средство"""

	name = models.CharField(max_length=255, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание', blank=True)
	slug = models.SlugField(unique=True, verbose_name='Слаг')
	vin = models.CharField(max_length=100, unique=True, verbose_name='VIN код')
	brand = models.CharField(max_length=255, verbose_name='Марка')
	price = models.IntegerField(verbose_name='Стоимость')
	image = models.ImageField(upload_to='vehicle/%Y/%m/%d/', verbose_name='Изображение')
	car_model = models.CharField(max_length=255, verbose_name='Модель')
	color = models.CharField(max_length=100, verbose_name='Цвет')
	add_to_dealer = models.DateTimeField(auto_now_add=True, verbose_name='Дата первичного поступления к дилеру')
	add_to_dealer_center = models.DateTimeField(verbose_name='Дата поступления в дилерский центр', blank=True, null=True)
	dealer = models.ForeignKey(
		Dealer,
		verbose_name='Наименование дилера',
		on_delete=models.CASCADE,
		related_name='vehicle_dealer',
		blank=True,
		null=True)
	dealer_center = models.ForeignKey(
		DealerCenter,
		verbose_name='Наименование дилерского центра',
		on_delete=models.CASCADE,
		related_name='vehicle_dealer_center',
		blank=True,
		null=True)

	class Meta:
		unique_together = [['dealer', 'vin']]

	def __str__(self):
		return self.name



