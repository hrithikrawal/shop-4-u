# Generated by Django 3.1.4 on 2021-01-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
