# Generated by Django 4.0.4 on 2022-09-01 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0003_shopstable_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsoldincash',
            name='date_product_sold',
            field=models.DateTimeField(auto_now=True),
        ),
    ]