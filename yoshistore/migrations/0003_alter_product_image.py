# Generated by Django 4.0 on 2021-12-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoshistore', '0002_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='yoshistore/static/img/'),
        ),
    ]
