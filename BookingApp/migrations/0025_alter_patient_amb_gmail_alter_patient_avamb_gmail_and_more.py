# Generated by Django 4.1.2 on 2023-04-09 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0024_patient_user_gmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Amb_gmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingApp.ambulance'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='AvAmb_gmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingApp.av_ambulance'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='User_gmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingApp.user'),
        ),
    ]
