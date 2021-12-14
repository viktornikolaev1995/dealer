# Generated by Django 3.2.9 on 2021-12-14 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealers_and_dealer_centers', '0004_alter_vehiclephotos_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealerCenterReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('text', models.TextField(max_length=2500, verbose_name='Текст отзыва')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('dealer_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealer_center_review', to='dealers_and_dealer_centers.dealercenter', verbose_name='Дилерский центр')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dealers_and_dealer_centers.dealercenterreviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв дилерского центра',
                'verbose_name_plural': 'Отзывы дилерского центра',
            },
        ),
    ]
