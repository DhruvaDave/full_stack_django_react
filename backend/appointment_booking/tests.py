from django.utils import timezone
from rest_framework.test import APITestCase

from .models import Appointment, Patient


class AppointmentBookingTestCase(APITestCase):
    def test_appointment_booking(self):
        appointment = Appointment.objects.create(start_time=timezone.now(), end_time=timezone.now())
        patient = Patient.objects.create()
        response = self.client.get(f"/appointments/{appointment.pk}/")
        assert response.json()["pk"] == appointment.pk
        response = self.client.patch(
            f"/appointments/{appointment.pk}/book/", {"patient_pk": patient.pk}, format="json"
        )
        assert response.status_code == 200
        assert response.data["pk"] == appointment.pk
        # TODO: test that the Appointment is now associated with the Patient
