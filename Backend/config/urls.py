from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.events.urls")),  # Подключаем URL-ы приложения events
    path("health/", health),
]
