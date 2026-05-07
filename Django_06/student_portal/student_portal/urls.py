from django.contrib import admin
from django.urls import include, path

from main_app.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("subjects/", include("main_app.urls")),
]
