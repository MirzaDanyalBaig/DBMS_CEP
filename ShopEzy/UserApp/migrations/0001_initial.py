# Generated by Django 4.2.3 on 2023-07-16 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdID', models.IntegerField()),
                ('PName', models.CharField(max_length=60)),
                ('PPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PQuantity', models.IntegerField()),
                ('PSpecs', models.TextField()),
                ('PImage', models.TextField()),
                ('CreatedAt', models.DateTimeField(default=datetime.datetime(2023, 7, 15, 23, 7, 31, 976565))),
                ('UpdatedAt', models.DateTimeField(default=None)),
                ('DeletedAt', models.DateTimeField(default=None)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]