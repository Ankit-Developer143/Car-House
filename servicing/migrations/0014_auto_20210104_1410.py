# Generated by Django 3.1.4 on 2021-01-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicing', '0013_auto_20210104_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Images',
            field=models.ImageField(default='car.jpg', upload_to='photos'),
        ),
    ]
