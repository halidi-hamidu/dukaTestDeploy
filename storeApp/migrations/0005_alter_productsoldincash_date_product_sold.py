# Generated by Django 4.0.4 on 2022-09-03 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0004_alter_productsoldincash_date_product_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsoldincash',
            name='date_product_sold',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 22, 18, 4, 766482)),
        ),
    ]
