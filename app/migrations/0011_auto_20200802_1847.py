# Generated by Django 3.0.8 on 2020-08-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200802_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='required_country',
            field=models.CharField(blank=True, choices=[('Tanzania', 'Tanzania'), ('Ghana', 'Ghana'), ('Mexico', 'Mexico'), ('Switzerland', 'Switzerland')], max_length=200),
        ),
    ]
