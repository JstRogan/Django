from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from articles.forms import ArticleForm
from articles.models import Article, ArticleReaction, Category


def article_list(request):
    articles = Article.objects.select_related("category")
    return render(request, "articles/article_list.html", {"articles": articles})


def article_detail(request, slug):
    article = get_object_or_404(Article.objects.select_related("category"), slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, "articles/article_form.html", {"form": form})


@require_POST
def react(request, slug):
    article = get_object_or_404(Article, slug=slug)
    value = request.POST.get("value")
    if value not in [ArticleReaction.LIKE, ArticleReaction.DISLIKE]:
        return redirect("articles:detail", slug=slug)
    if not request.session.session_key:
        request.session.create()
    ArticleReaction.objects.update_or_create(
        article=article,
        session_key=request.session.session_key,
        defaults={"value": value},
    )
    return redirect("articles:detail", slug=slug)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)
    return render(
        request,
        "articles/article_list.html",
        {"articles": articles, "page_title": category.name},
    )
