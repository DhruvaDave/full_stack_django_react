from django.db import models

# https://docs.djangoproject.com/en/3.2/topics/db/models/


class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Appointment(models.Model):
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
    patient_pk = models.ForeignKey(Patient, on_delete=models.CASCADE, default=False, blank=True, null=True)
