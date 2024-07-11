from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from server.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path("generator/", include(("generator.urls", "generator"))),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
