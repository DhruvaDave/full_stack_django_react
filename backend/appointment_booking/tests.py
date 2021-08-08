from django.utils import timezone
from rest_framework.test import APITestCase

from .models import Appointment, Patient


class AppointmentBookingTestCase(APITestCase):
    def test_appointment_booking(self):
        appointment = Appointment.objects.create(start_time=timezone.now(), end_time=timezone.now(), patient_pk=None)
        patient = Patient.objects.create()
        response = self.client.get(f"/appointments/{appointment.pk}/")
        assert response.json()["pk"] == appointment.pk
        response = self.client.patch(
            f"/appointments/{appointment.pk}/book/", {"patient_pk": patient.pk}, format="json"
        )
        assert response.status_code == 200
        assert response.data["pk"] == appointment.pk
        assert response.data["patient_pk"] == patient.pk

    def test_already_booked_appointment(self):
        patient = Patient.objects.create()
        appointment = Appointment.objects.create(start_time=timezone.now(), end_time=timezone.now(), patient_pk=patient)
        response = self.client.get(f"/appointments/{appointment.pk}/")
        assert response.json()["pk"] == appointment.pk
        response = self.client.patch(
            f"/appointments/{appointment.pk}/book/", {"patient_pk": patient.pk}, format="json"
        )
        assert response.data["pk"] == appointment.pk
        assert response.data["patient_pk"] == patient.pk
        assert response.status_code == 405


    def test_overlap_appointment_booking(self):
        patient = Patient.objects.create()
        appointment1 = Appointment.objects.create(start_time="2021-08-08 05:53:48.779098+00:00", end_time="2021-08-08 06:53:48.779098+00:00", patient_pk=None)
        appointment2 = Appointment.objects.create(start_time="2021-08-08 05:53:48.779098+00:00", end_time="2021-08-08 06:53:48.779098+00:00", patient_pk=None)
        response = self.client.get(f"/appointments/{appointment1.pk}/")
        assert response.json()["pk"] == appointment1.pk
        response = self.client.patch(
            f"/appointments/{appointment1.pk}/book/", {"patient_pk": patient.pk}, format="json"
        )
        assert response.status_code == 400
        assert response.data["pk"] == appointment1.pk
        assert response.data["patient_pk"] == None