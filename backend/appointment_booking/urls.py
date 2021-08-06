from django.urls import include, path
from rest_framework import routers

from .views import AppointmentViewSet, PatientViewSet

# Routers provide an easy way of automatically determining the URL conf.
# https://www.django-rest-framework.org/api-guide/routers/#api-guide

router = routers.DefaultRouter()
router.register(r"appointments", AppointmentViewSet)
router.register(r"patients", PatientViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls), name="appointment-booking"),
]
