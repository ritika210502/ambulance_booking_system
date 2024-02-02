# Generated by Django 4.1.2 on 2023-02-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0002_ambulance_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='post',
            field=models.CharField(default='user', max_length=30),
        ),
        migrations.AddField(
            model_name='hospital',
            name='post',
            field=models.CharField(default='user', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='post',
            field=models.CharField(default='user', max_length=30),
        ),
    ]
