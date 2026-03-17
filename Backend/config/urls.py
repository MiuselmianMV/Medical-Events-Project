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

# admin.site.site_header = "Адміністративна панель медичних подій"
# admin.site.index_title = "Медичні події"
# admin.site.site_title = "Медичні події"