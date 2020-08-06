# Generated by Django 3.0.8 on 2020-08-05 20:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200802_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='vaccine_card_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='vaccine_card_image'),
        ),
    ]
