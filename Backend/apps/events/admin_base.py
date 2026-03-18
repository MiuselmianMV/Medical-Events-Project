from typing import Any
from django.contrib import admin

class AdminTitleMixin:
    change_title: str | None = None
    add_title: str | None = None

    def change_view(self, request, object_id, form_url="", extra_context=None):
        context: dict[str, Any] = extra_context.copy() if extra_context else {}
        if self.change_title:
            context["title"] = self.change_title
        return super().change_view(request, object_id, form_url, extra_context=context) # type: ignore

    def add_view(self, request, form_url="", extra_context=None):
        context: dict[str, Any] = extra_context.copy() if extra_context else {}
        if self.add_title:
            context["title"] = self.add_title
        return super().add_view(request, form_url, extra_context=context) # type: ignore


class BaseAdmin(AdminTitleMixin, admin.ModelAdmin):
    save_on_top = False
    list_per_page = 20