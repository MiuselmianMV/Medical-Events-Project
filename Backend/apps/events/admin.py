from django import forms
from django.contrib import admin

from .models import Specialty, Event, Card
from .s3_service import upload_card_photo_to_s3

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)

class CardAdminForm(forms.ModelForm):
    photo = forms.ImageField(
        required=False,
        help_text="Выбери изображение — оно загрузится в S3, а ссылка сохранится в поле photo_url."
    )

    class Meta:
        model = Card
        fields = ("title", "slug")
    

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    form = CardAdminForm

    list_display = ("id", "title", "slug", "photo_url")
    search_fields = ("title", "slug", "photo_url")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("title",)

    def save_model(self, request, obj, form, change):
        photo = form.cleaned_data.get("photo")
        if photo:
            obj.photo_url = upload_card_photo_to_s3(photo, key_prefix="cards")

        super().save_model(request, obj, form, change)
    

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
