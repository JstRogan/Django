from django.contrib import admin
from django.urls import include, path

from hello_app.views import hello_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello_view, name="hello"),
    path("day/", include("day_app.urls")),
    path("quote/", include("quote_app.urls")),
]
