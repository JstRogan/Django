from django.urls import path

from .views import current_day_view


urlpatterns = [
    path("", current_day_view, name="current_day"),
]
