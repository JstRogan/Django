from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


POSTS = [
    {
        "id": 1,
        "title": "Первый пост",
        "content": "Знакомство с шаблонами Django.",
        "author": "Студент",
    },
    {
        "id": 2,
        "title": "Второй пост",
        "content": "Работа с циклом for и условием if в шаблонах.",
        "author": "Студент",
    },
    {
        "id": 3,
        "title": "Третий пост",
        "content": "Использование base.html и наследования шаблонов.",
        "author": "Студент",
    },
]


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/home.html")


def post_list(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/post_list.html", {"posts": POSTS})


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = next((item for item in POSTS if item["id"] == post_id), None)
    return render(request, "blog/post_detail.html", {"post": post})
