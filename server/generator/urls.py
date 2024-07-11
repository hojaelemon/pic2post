from django.urls import path

from generator.views import get_image


urlpatterns = [
    path("image", get_image),
]