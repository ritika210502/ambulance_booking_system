# Generated by Django 4.1.2 on 2023-03-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0013_remove_ambulance_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='usertype',
            field=models.CharField(default='user', max_length=30),
        ),
    ]