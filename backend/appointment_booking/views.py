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
        queryset = Appointment.objects.filter(patient_pk=None).exclude(pk=pk)
        appointment = Appointment.objects.get(pk=pk)
        serializer = AppointmentSerializer(appointment)

        if appointment.patient_pk:
            # Already booked appointment
            logger.info("Appointment is already Booked  %s for patient %s", appointment.pk, appointment.patient_pk)
            return Response(serializer.data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        patient = Patient.objects.get(pk=request.data.get("patient_pk"))
        logger.info("Booking appointment %s for patient %s", appointment.pk, patient.pk)

        is_overlap = False
        for app in queryset:
            if (appointment.start_time <= app.end_time) and (app.start_time <= appointment.end_time):
                is_overlap = True
                logger.info("Overlaping found in booking appointment %s for patient %s", appointment.pk, patient.pk)
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        if not is_overlap:
            serializer = AppointmentSerializer(appointment, data={'patient_pk': request.data.get("patient_pk")}, partial=True)
            if serializer.is_valid():
                serializer.save()

        logger.info("Appointment Booked successfully %s for patient %s", appointment.pk, patient.pk)
        return Response(serializer.data, status=status.HTTP_200_OK)
