from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm
from .models import Article


def article_list(request: HttpRequest) -> HttpResponse:
    return render(request, "articles/article_list.html",
                  {"articles": Article.objects.all()})


def article_detail(request: HttpRequest, article_id: int) -> HttpResponse:
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "articles/article_detail.html", {"article": article})


def article_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article_id=article.pk)
    else:
        form = ArticleForm()
    return render(request, "articles/article_form.html", {"form": form})


def article_react(request: HttpRequest, article_id: int) -> HttpResponse:
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "like":
            article.likes += 1
        elif action == "dislike":
            article.dislikes += 1
        article.save()
    return redirect(request.POST.get("next") or "articles:article_list")
