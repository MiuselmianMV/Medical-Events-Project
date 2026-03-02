import django_filters
from django.utils import timezone
from .models import Event

class EventFilter(django_filters.FilterSet):
    upcoming = django_filters.BooleanFilter(method="filter_upcoming")
    specialties = django_filters.BaseInFilter(field_name="specialties__id", lookup_expr="in")

    class Meta:
        model = Event
        fields = ["status", "event_type", "card_id", "scheduled_date"]

    def filter_upcoming(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(
            status=Event.Status.PLANNED,
            scheduled_date__gte=timezone.localdate()
        )