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
        queryset = Appointment.objects.all()
        appointment = Appointment.objects.get(pk=pk)
        patient = Patient.objects.get(pk=request.data.get("patient_pk"))
        logger.info("Booking appointment %s for patient %s", appointment.pk, patient.pk)
        # TODO: implement appointment booking logic
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
