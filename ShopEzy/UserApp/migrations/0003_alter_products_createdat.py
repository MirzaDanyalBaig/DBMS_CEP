# Generated by Django 4.2.3 on 2023-07-16 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_alter_products_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 16, 0, 9, 13, 659660)),
        ),
    ]
