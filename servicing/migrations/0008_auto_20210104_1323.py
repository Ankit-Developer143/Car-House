# Generated by Django 3.1.4 on 2021-01-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicing', '0007_auto_20210104_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_price',
            field=models.IntegerField(default=True, null=True),
        ),
    ]
