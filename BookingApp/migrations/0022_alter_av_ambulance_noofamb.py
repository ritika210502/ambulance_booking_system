# Generated by Django 4.1.2 on 2023-03-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0021_alter_ambulance_usertype_alter_hospital_usertype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='av_ambulance',
            name='NoOfAmb',
            field=models.CharField(max_length=3),
        ),
    ]
