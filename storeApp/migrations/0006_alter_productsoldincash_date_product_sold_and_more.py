# Generated by Django 4.0.4 on 2022-09-03 19:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0005_alter_productsoldincash_date_product_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsoldincash',
            name='date_product_sold',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 22, 23, 30, 98135)),
        ),
        migrations.AlterField(
            model_name='productsoldincash',
            name='supervisor',
            field=models.ForeignKey(default='Admin', null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeApp.employeedetailinformations'),
        ),
    ]