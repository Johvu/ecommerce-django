# Generated by Django 4.0.4 on 2022-06-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_product_discount_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=False, unique=True),
            preserve_default=False,
        ),
    ]
