# Generated by Django 4.1.2 on 2023-04-23 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0029_alter_hos_patient_midname_alter_hos_patient_phno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_address', models.CharField(max_length=200)),
                ('destination_address', models.CharField(max_length=200)),
            ],
        ),
    ]
