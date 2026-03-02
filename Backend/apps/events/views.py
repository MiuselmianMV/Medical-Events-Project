from rest_framework import viewsets, permissions
from .models import Event, Specialty, Card
from .serializers import EventSerializer, SpecialtySerializer, CardSerializer

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.select_related("card_id").prefetch_related("specialties")
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

class SpecialtyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

class CardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"