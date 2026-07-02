from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from . import data
from .forms import ArticleForm


def article_list(request: HttpRequest) -> HttpResponse:
    return render(request, "articles/article_list.html",
                  {"articles": data.ARTICLES})


def article_detail(request: HttpRequest, article_id: int) -> HttpResponse:
    article = next((item for item in data.ARTICLES if item["id"] == article_id), None)
    if article is None:
        return redirect("articles:article_list")
    return render(request, "articles/article_detail.html", {"article": article})


def article_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data.copy()
            article["id"] = max(item["id"] for item in data.ARTICLES) + 1
            article["created_at"] = timezone.now().strftime("%Y-%m-%d")
            article["likes"] = 0
            article["dislikes"] = 0
            data.ARTICLES.insert(0, article)
            return redirect("articles:article_detail", article_id=article["id"])
    else:
        form = ArticleForm()
    return render(request, "articles/article_form.html", {"form": form})


def article_react(request: HttpRequest, article_id: int) -> HttpResponse:
    article = next((item for item in data.ARTICLES if item["id"] == article_id), None)
    if request.method == "POST" and article is not None:
        action = request.POST.get("action")
        if action == "like":
            article["likes"] += 1
        elif action == "dislike":
            article["dislikes"] += 1
    return redirect(request.POST.get("next") or "articles:article_list")
