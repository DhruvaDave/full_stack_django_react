# Generated by Django 3.2.5 on 2021-08-06 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='appointment_booking.patient'),
        ),
    ]
