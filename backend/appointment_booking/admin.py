from django.contrib import admin

from .models import Appointment, Patient

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    
    list_display = ('start_time', 'end_time', 'patient_pk')
    exclude = [('id')]
    
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Patient)
