from django.urls import path

from articles import views

app_name = "articles"

urlpatterns = [
    path("", views.article_list, name="list"),
    path("articles/create/", views.article_create, name="create"),
    path("articles/<slug:slug>/", views.article_detail, name="detail"),
    path("articles/<slug:slug>/react/", views.react, name="react"),
    path("categories/<slug:slug>/", views.category_detail, name="category_detail"),
]
