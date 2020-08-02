# Generated by Django 3.0.8 on 2020-08-02 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200725_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='isChild',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='isParent',
        ),
        migrations.AddField(
            model_name='profile',
            name='family_member_type',
            field=models.CharField(choices=[('PARENT', 'parent'), ('CHILD', 'child')], default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='vaccine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Vaccine'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='familygroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FamilyGroup'),
        ),
    ]
