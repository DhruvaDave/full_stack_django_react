import logging

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import routers, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Appointment, Patient
from .serializers import AppointmentSerializer, PatientSerializer, AppointmentBookingSerializer

logger = logging.getLogger(__name__)

# ViewSets define the view behavior.
# https://www.django-rest-framework.org/api-guide/viewsets/#viewsets


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=True, methods=["patch"])
    def book(self, request, pk=None):
        temp = self.get_object()    
        queryset = Appointment.objects.filter(patient_pk=None).exclude(pk=pk)
        print("------queryset---------",queryset)
        appointment = Appointment.objects.get(pk=pk)
        serializer = AppointmentSerializer(appointment)

        print("--------- appointment.patient_pk----------", appointment.patient_pk)
        if appointment.patient_pk:
            # Already booked appointment
            return Response(serializer.data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        patient = Patient.objects.get(pk=request.data.get("patient_pk"))
        logger.info("Booking appointment %s for patient %s", appointment.pk, patient.pk)
        # TODO: implement appointment booking logic
       
        is_overlap = False
        for app in queryset:
            print("-----ap------------",app,app.start_time,"--end",app.end_time)
            print("----main----",appointment.start_time,"--end",appointment.end_time)
            if (appointment.start_time <= app.end_time) and (app.start_time <= appointment.end_time):
                is_overlap = True
                print("--------overlap----__HERER--",is_overlap)
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        print("--------voerlap------",is_overlap)
        if not is_overlap:
            serializer = AppointmentSerializer(appointment, data={'patient_pk': request.data.get("patient_pk")}, partial=True)
            if serializer.is_valid():
                serializer.save()
            
        # serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
