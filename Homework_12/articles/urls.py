from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("article/<int:article_id>/", views.article_detail, name="article_detail"),
    path("article/<int:article_id>/react/", views.article_react, name="article_react"),
    path("add/", views.article_create, name="article_create"),
]
