# Generated by Django 5.0.4 on 2024-06-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
    ]
