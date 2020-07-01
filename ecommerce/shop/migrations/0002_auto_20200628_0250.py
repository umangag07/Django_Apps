# Generated by Django 3.0.7 on 2020-06-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to='shop/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_sub_category',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]
