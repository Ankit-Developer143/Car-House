# Generated by Django 3.1.4 on 2021-01-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicing', '0014_auto_20210104_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Images',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos'),
        ),
    ]
