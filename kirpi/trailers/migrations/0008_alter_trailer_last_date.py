# Generated by Django 5.0.1 on 2024-01-10 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0007_remove_trailer_created_at_remove_trailer_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 18, 5, 6, 208559), verbose_name='Onceki Tarih'),
        ),
    ]