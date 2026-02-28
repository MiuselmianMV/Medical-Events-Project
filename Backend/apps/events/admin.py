from django.contrib import admin

from .models import Specialty, Event, Card


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "photo_url")
    search_fields = ("title", "slug", "photo_url")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("title",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "event_type",
        "status",
        "scheduled_date",
        "scheduled_time",
        "location",
        "duration",
        "card_id",
    )
    list_filter = ("event_type", "status", "scheduled_date", "specialties")
    search_fields = ("title", "description", "slug", "location")
    ordering = ("scheduled_date", "scheduled_time")

    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("specialties",)

    autocomplete_fields = ("card_id",)

    # Чтобы autocomplete по card_id работал, у CardAdmin должны быть search_fields (они есть выше).