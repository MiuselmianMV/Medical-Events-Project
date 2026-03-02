from rest_framework import serializers
from .models import Specialty, Event, Card


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ["id", "name", "slug"]
        read_only_fields = ["slug"]


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "title", "photo_url", "slug"]
        read_only_fields = ["slug"]


class EventSerializer(serializers.ModelSerializer):
    specialties = SpecialtySerializer(many=True, read_only=True)
    card_id = CardSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "scheduled_date",
            "scheduled_time",
            "location",
            "duration",
            "specialties",
            "card_id",
            "event_type",
            "status",
        ]
        read_only_fields = ["slug"]

