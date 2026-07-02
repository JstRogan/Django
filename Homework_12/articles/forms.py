from django import forms

from .data import CATEGORIES


class ArticleForm(forms.Form):
    title = forms.CharField(label="Заголовок", max_length=200)
    author = forms.CharField(label="Автор", max_length=50)
    image = forms.URLField(label="Ссылка на картинку")
    category = forms.ChoiceField(label="Категория",
                                 choices=[(name, name) for name in CATEGORIES])
    content = forms.CharField(label="Текст статьи",
                              widget=forms.Textarea(attrs={"rows": 10}))
