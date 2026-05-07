from django.urls import path

from .views import random_quote_view


urlpatterns = [
    path("", random_quote_view, name="random_quote"),
]
