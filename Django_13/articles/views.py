from django.shortcuts import get_object_or_404, render

from articles.models import Article, Category


def article_list(request):
    articles = Article.objects.select_related("category")
    return render(request, "articles/article_list.html", {"articles": articles})


def article_detail(request, slug):
    article = get_object_or_404(Article.objects.select_related("category"), slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})


def category_list(request):
    categories = Category.objects.all()
    return render(request, "articles/category_list.html", {"categories": categories})
