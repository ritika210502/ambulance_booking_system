# Generated by Django 4.1.2 on 2023-03-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0010_alter_hospital_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='av_hospital',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('phNo', models.CharField(max_length=10)),
                ('Street', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('Zip', models.CharField(max_length=30)),
            ],
        ),
    ]
