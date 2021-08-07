# Generated by Django 3.2.5 on 2021-08-07 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_booking', '0004_alter_appointment_patient_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_pk',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment_booking.patient'),
        ),
    ]