# Generated by Django 3.1.4 on 2021-01-03 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210103_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_orderd',
            new_name='date_ordered',
        ),
    ]
