# Generated by Django 3.1.4 on 2021-01-04 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicing', '0008_auto_20210104_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_price',
        ),
    ]
