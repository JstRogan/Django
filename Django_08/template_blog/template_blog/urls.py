from django.contrib import admin
from django.urls import include, path

from blog.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("posts/", include("blog.urls")),
]
