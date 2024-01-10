# Generated by Django 5.0.1 on 2024-01-10 13:20

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trailers', '0004_alter_trailer_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=12, null=True, verbose_name='Birim Fiyat')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Katildigi Tarih')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Guncellendigi Tarih')),
            ],
            options={
                'verbose_name': 'Birim Fiyat',
                'verbose_name_plural': 'Birim Fiyatlar',
            },
        ),
        migrations.CreateModel(
            name='ElectricMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=15, null=True, verbose_name='Seri Numarasi')),
                ('t0', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=12, null=True, verbose_name='T0')),
                ('t1', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=12, null=True, verbose_name='T1')),
                ('t2', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=12, null=True, verbose_name='T2')),
                ('t3', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=12, null=True, verbose_name='T3')),
                ('ri', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=12, null=True, verbose_name='ri')),
                ('rc', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=12, null=True, verbose_name='rc')),
                ('price', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=15, null=True, verbose_name='price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Hesaplama Tarihi')),
                ('trailer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trailer_meter', to='trailers.trailer', verbose_name='Karavan')),
            ],
            options={
                'verbose_name': 'Elektrik Sayaci',
                'verbose_name_plural': 'Elektrik Sayaclari',
            },
        ),
    ]
