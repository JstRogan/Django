from django.urls import path

from .views import subjects_list


urlpatterns = [
    path("", subjects_list, name="subjects_list"),
]
