# Generated by Django 4.0.4 on 2022-06-01 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0003_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
