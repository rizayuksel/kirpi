# Generated by Django 5.0.1 on 2024-01-10 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trailers', '0003_rename_username_trailer_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trailer',
            options={'verbose_name': 'Karavan', 'verbose_name_plural': 'Karavanlar'},
        ),
    ]
