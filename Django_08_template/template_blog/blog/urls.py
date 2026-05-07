from django.urls import path

from . import views


app_name = "blog"

urlpatterns = [
    path("football", views.football, name="football"),
    path("hockey", views.hockey, name="hockey"),
    path("basketball", views.basketball, name="basketball"),
]
