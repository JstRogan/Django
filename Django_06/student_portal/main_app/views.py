from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


SUBJECTS = [
    {"title": "Python", "teacher": "Анна Петрова"},
    {"title": "Django", "teacher": "Игорь Смирнов"},
    {"title": "SQL", "teacher": "Мария Волкова"},
]


def home(request: HttpRequest) -> HttpResponse:
    context = {"project_name": "Student Portal"}
    return render(request, "main_app/home.html", context)


def subjects_list(request: HttpRequest) -> HttpResponse:
    context = {"subjects": SUBJECTS}
    return render(request, "main_app/subjects_list.html", context)
