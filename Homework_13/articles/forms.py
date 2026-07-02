from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "author", "image", "category", "content"]
        labels = {
            "title": "Заголовок",
            "author": "Автор",
            "image": "Ссылка на картинку",
            "category": "Категория",
            "content": "Текст статьи",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 10}),
        }
