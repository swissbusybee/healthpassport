# Generated by Django 3.0.8 on 2020-08-02 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200802_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccine',
            old_name='reccomended_age',
            new_name='recommended_age',
        ),
    ]