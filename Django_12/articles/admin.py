from django.contrib import admin

from articles.models import Article, ArticleReaction, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "created_at")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ArticleReaction)
