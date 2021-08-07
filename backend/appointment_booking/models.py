from django.db import models
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.db.models import ProtectedError

# https://docs.djangoproject.com/en/3.2/topics/db/models/


class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

# @receiver(pre_delete, sender=Patient)
# def model_delete(sender, instance, **kwargs):
#     print("------delete-------sender-",sender, "---instance---",instance,"--kwargs",kwargs)
#     queryset = Appointment.objects.filter(patient_pk=instance.pk)
#     print("----apointment--------",queryset)
    
#     for obj in queryset:
#         obj.patient_pk = None
        # obj.delete()
        

class Appointment(models.Model):
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
    patient_pk = models.ForeignKey(Patient, on_delete=models.SET_NULL, default=False, blank=True, null=True)


@receiver(pre_delete, sender=Appointment)
def model_delete(sender, instance, **kwargs):
    print("------delete-------sender-",sender, "---instance---",instance,"--kwargs",kwargs)
    print("------instance.patient_pk--------",instance.patient_pk)
    if instance.patient_pk:
        print("-------ig--------")
        raise Exception('Appointments with patients can not be deleted.')
    