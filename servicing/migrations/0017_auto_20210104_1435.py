# Generated by Django 3.1.4 on 2021-01-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicing', '0016_auto_20210104_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Images',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
