from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Specialty, Event, Card
from .s3_service import upload_card_photo_to_s3
from .admin_base import BaseAdmin
from .forms import CardAdminForm

admin.site.index_title = "Керування контентом сайту"


@admin.register(Specialty)
class SpecialtyAdmin(BaseAdmin):
    change_title = "Редагування спеціальності"
    add_title = "Додавання спеціальності"

    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("slug",)

    fieldsets = (
        ("Основна інформація", {
            "fields": ("name", "slug")
        }),
    )




@admin.register(Card)
class CardAdmin(BaseAdmin):
    change_title = "Редагування картки"
    add_title = "Додавання картки"

    form = CardAdminForm
    list_display = ("title", "image_preview", "photo_link")
    search_fields = ("title",)
    ordering = ("title",)
    readonly_fields = ("image_preview_large",)

    fieldsets = (
        ("Основна інформація", {
            "fields": ("title",)
        }),
        ("Зображення", {
            "fields": ("photo", "image_preview_large"),
            "description": "Оберіть файл "
        }),
    )

    def save_model(self, request, obj, form, change):
        photo = form.cleaned_data.get("photo")
        if photo:
            obj.photo_url = upload_card_photo_to_s3(photo, key_prefix="cards")
        super().save_model(request, obj, form, change)

    @admin.display(description="Превʼю")
    def image_preview(self, obj):
        if obj.photo_url:
            return format_html(
                '<img src="{}" style="height:60px; width:auto; border-radius:8px;" />',
                obj.photo_url
            )
        return "Немає зображення"

    @admin.display(description="Посилання")
    def photo_link(self, obj):
        if obj.photo_url:
            return format_html('<a href="{}" target="_blank">Відкрити</a>', obj.photo_url)
        return "Немає посилання"

    @admin.display(description="Поточне зображення")
    def image_preview_large(self, obj):
        if obj and obj.photo_url:
            return format_html(
                '<img src="{}" style="max-height:220px; width:auto; border-radius:10px; border:1px solid #ddd;" />',
                obj.photo_url
            )
        return "Зображення ще не завантажене"


@admin.register(Event)
class EventAdmin(BaseAdmin):
    change_title = "Редагування події"
    add_title = "Додавання події"

    list_display = (
        "title",
        "scheduled_datetime",
        "location",
        "event_type",
        "status",
        "display_specialties",
        "card_preview",
        "form_link",
    )
    list_filter = ("event_type", "status", "scheduled_date", "specialties")
    search_fields = ("title", "description", "location")
    ordering = ("scheduled_date", "scheduled_time")
    filter_horizontal = ("specialties",)
    autocomplete_fields = ("card",)

    fieldsets = (
        ("Основна інформація", {
            "fields": ("title", "description")
        }),
        ("Дата та місце проведення", {
            "fields": ("scheduled_date", "scheduled_time", "duration", "location")
        }),
        ("Тип події та статус", {
            "fields": ("event_type", "status")
        }),
        ("Категорії та картка", {
            "fields": ("specialties", "card")
        }),
        ("Додатково", {
            "fields": ("form_url",),
        }),
    )

    @admin.display(description="Дата і час")
    def scheduled_datetime(self, obj):
        return f"{obj.scheduled_date} {obj.scheduled_time.strftime('%H:%M')}"

    @admin.display(description="Спеціальності")
    def display_specialties(self, obj):
        return ", ".join(s.name for s in obj.specialties.all()) or "Не вибрано"

    @admin.display(description="Картка")
    def card_preview(self, obj):
        if obj.card and obj.card.photo_url:
            return format_html(
                '<img src="{}" style="height:45px; width:auto; border-radius:6px;" />',
                obj.card.photo_url
            )
        if obj.card:
            return obj.card.title
        return "Не вибрано"

    @admin.display(description="Форма")
    def form_link(self, obj):
        if obj.form_url:
            return format_html('<a href="{}" target="_blank">Відкрити</a>', obj.form_url)
        return "Немає посилання"