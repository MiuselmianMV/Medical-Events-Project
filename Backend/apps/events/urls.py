from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, SpecialtyViewSet, CardViewSet

router = DefaultRouter()

router.register(r"events", EventViewSet, basename="event")
router.register(r"specialties", SpecialtyViewSet, basename="specialty")
router.register(r"cards", CardViewSet, basename="card")

urlpatterns = [
    path("", include(router.urls)),
]

